init -100:
    # Styles.
    # style.readback_window.xmaximum  760
    # style.readback_window.ymaximum  500
    style readback_window align  (.5, .5)
    style readback_window ysize  None
    style readback_window background  "#000b"

    style readback_frame background  None
    style readback_frame xfill  True
    style readback_frame xpadding  10
    style readback_frame ypadding  10
    style readback_frame xmargin  0
    style readback_frame ymargin  0

    style readback_text color  "#fff"

    style readback_button idle_background  None
    style readback_button insensitive_background  None
    # style readback_button hover_background

    # style.create("readback_button_text", "readback_text")
    # style.readback_button_text.selected_color  "#f12"
    # style.readback_button_text.hover_color  "#f12"

    style readback_label_text bold  True

init -100 python:
    # starts adding new config variables
    config.locked = False

    # Configuration Variable for Text History
    config.readback_buffer_length = 100 # number of lines stored
    config.readback_full = False # completely replaces rollback, False = readback accessible from game menu only (dev mode)
    config.readback_scroll_step = 300 
    config.readback_disallowed_tags = ["size"] # a list of tags that will be removed in the text history
    config.readback_choice_prefix = "{size=40}Вы выбрали{/size}"   # this is prefixed to the choices the user makes in readback
    config.readback_space_after_nvl_clear = True   # optionally add a sort of paragraph break when "nvl clear" is used
    config.readback_nvl_page = True  # Make scrolling use NVL pages rather than "smooth" scrolling
    config.readback_max_line = 7  # if config.readback_nvl_page is True, the max lines on one page
    config.readback_max_page = 100 # if config.readback_nvl_page is True, the max pages
    config.readback_rollback = True #if True and readback_nvl_page is True, allow rollback from 'readback' screen
    config.store_save_info = 20 # if not 0, this number of characters in current line is assigned to save_name
    # end
    config.locked = True

    # This doesn't work in main menu.
    class ReadBack(Action):
        def __init__(self):
            self.screen = "text_history"

        def get_sensitive(self):
            return not renpy.context()._main_menu

        def predict(self):
            if renpy.has_screen(self.screen):
                renpy.predict_screen(self.screen)

        def __call__(self):
            global readback_yvalue
            if not self.get_sensitive():
                return
            readback_yvalue = 1.0
            ShowMenu('text_history')()

        def get_selected(self):
            return renpy.get_screen(self.screen)

init -99 python:
    # Two custom characters that store what they said
    class ReadbackADVCharacter(ADVCharacter):
        def do_done(self, who, what):
            store_say(who, what)
            store.current_voice = ''
            super(ReadbackADVCharacter, self).do_done(who, what)
            return

        def do_extend(self):
            delete_last_line()
            super(ReadbackADVCharacter, self).do_extend()
            return

    class ReadbackNVLCharacter(NVLCharacter):
        def do_done(self, who, what):
            store_say(who, what, True)
            store.current_voice = ''
            super(ReadbackNVLCharacter, self).do_done(who, what)
            return

        def do_extend(self):
            delete_last_line()
            super(ReadbackNVLCharacter, self).do_extend()
            return

    # this enables us to show the current line in readback without having to bother the buffer with raw shows
    def say_wrapper(who, what, **kwargs):
        store_current_line(who, what)
        return renpy.show_display_say(who, what, **kwargs)

    def store_current_line(who, what, nvl=False):
        global current_line, current_voice, save_name
        if preparse_say_for_store(what):
            current_line = (preparse_say_for_store(who), preparse_say_for_store(what), current_voice, -1, nvl)
            if config.store_save_info > 0:
                save_name = preparse_say_for_store(what)[:config.store_save_info]
    
    # config.nvl_show_display_say = say_wrapper # doesn't work if nvl screen exists
    
    adv = ReadbackADVCharacter(show_function=say_wrapper)
    nvl = ReadbackNVLCharacter()
    narrator = Character(None, kind=adv, what_style='say_thought')
    name_only = adv
    NVLCharacter = ReadbackNVLCharacter

    # rewriting voice function in 00voice.rpy to replay voice files when you clicked dialogues in text history screen
    def voice(filename, tag=None):
        if not config.has_voice:
            return
        
        fn = config.voice_filename_format.format(filename=filename)
        _voice.play = fn
        
        store.current_voice = fn

    # overwriting standard menu handler
    # Overwriting menu functions makes Text History log choice which users choose.
    def menu(items, **add_input):
        global rollback_num, current_line
        if renpy.get_screen('say') and config.skipping != 'fast':
            rollback_num -= 1
        if readback_buffer and readback_buffer[-1] and readback_buffer[-1][-1][:3] != current_line[:3]:
            current_line = readback_buffer[-1][-1] # for fast skip

        rollback_num += 1
        rv = renpy.display_menu(items, **add_input)
        rollback_num -= 1
        # logging menu choice label.
        for label, val in items:
            if rv == val:
                store.current_voice = ''
                store_say(None, config.readback_choice_prefix + label)
        return rv

    # Overwriting nvl menu in 00nvl_mode.rpy function
    builtin_nvl_menu = nvl_menu
    def nvl_menu(items):
        global rollback_num, current_line
        if renpy.get_screen('nvl') and menu is not nvl_menu and config.skipping != 'fast':
            rollback_num -= 1
        if readback_buffer and readback_buffer[-1] and readback_buffer[-1][-1][:3] != current_line[:3]:
            current_line = readback_buffer[-1][-1] # for fast skip

        # logging menu choice label.
        rollback_num += 1
        rv = builtin_nvl_menu(items)
        rollback_num -= 1
        for label, val in items:
            if rv == val:
                store.current_voice = ''
                store_say(None, config.readback_choice_prefix + label, True)
        return rv

    # nvl_menu has reload error?
    def menu_to_nvl(mode, old_modes):
        global rollback_num
        if old_modes[0] == "menu":
            if mode == "nvl" or mode == "nvl_menu":
                rollback_num -= 1
    config.mode_callbacks.append(menu_to_nvl)

    builtin_nvl_clear = nvl_clear
    # Overwriting nvl_clear in 00nvl_mode.rpy function
    def nvl_clear():
        global readback_lock
        builtin_nvl_clear()
        readback_lock = False
        if config.readback_nvl_page:
            readback_buffer.append([])
        elif config.readback_space_after_nvl_clear:
            readback_buffer.append((None, "", ""))

    builtin_nvl_show_core = nvl_show_core
    # Overwriting nvl_show_core in 00nvl_mode.rpy function
    def nvl_show_core(who=None, what=None):
        store_current_line(who, what, True)
        return builtin_nvl_show_core(who, what)

    # Overwriting pause in exports.py function
    # builtin_pause = renpy.pause # reload causes infinite loop.
    # def overriding_pause(delay=None, music=None, with_none=None, hard=False, checkpoint=None):
    #     global rollback_num
    #     if checkpoint or delay is None:
    #         rollback_num += 1
    #     builtin_pause(delay, music, with_none, hard, checkpoint)
    def overriding_pause(delay=None, music=None, with_none=None, hard=False, checkpoint=None):

        if checkpoint is None:
            if delay is not None:
                checkpoint = False
            else:
        #############################
                if renpy.config.skipping != "fast":
                    renpy.store.rollback_num += 1
        #############################
                checkpoint = True

        if renpy.config.skipping == "fast":
            return False

        roll_forward = renpy.exports.roll_forward_info()
        if roll_forward not in [ True, False ]:
            roll_forward = None

        renpy.exports.mode('pause')

        if music is not None:
            newdelay = renpy.audio.music.get_delay(music)

            if newdelay is not None:
                delay = newdelay

        if renpy.game.after_rollback and roll_forward is None:
            delay = 0

        if hard:
            renpy.ui.saybehavior(dismiss='dismiss_hard_pause')
        else:
            renpy.ui.saybehavior()

        if delay is not None:
            renpy.ui.pausebehavior(delay, False)

        rv = renpy.ui.interact(mouse='pause', type='pause', roll_forward=roll_forward)

        if checkpoint:
            renpy.exports.checkpoint(rv, keep_rollback=True)

        if with_none is None:
            with_none = renpy.config.implicit_with_none

        if with_none:
            renpy.game.interface.do_with(None, None)

        return rv
    renpy.pause = overriding_pause

    def readback_reset():
        global readback_buffer, current_line, current_voice, rollback_num, readback_lock, readback_rollback_block
        current_line = None
        current_voice = None
        rollback_num = 0
        readback_lock = False
        readback_rollback_block = 0

        if config.readback_nvl_page:
            readback_buffer = [ [] ]
        else:
            readback_buffer = [ ]

    readback_reset()
    config.start_callbacks.append(readback_reset)

    def store_say(who, what, nvl=False):
        global readback_buffer, current_voice, rollback_num, readback_lock, readback_rollback_block
        if preparse_say_for_store(what):
            if nvl and config.nvl_paged_rollback and not readback_lock:
                if config.skipping != 'fast':
                    rollback_num += 1
                readback_lock = True
            elif not nvl or not config.nvl_paged_rollback:
                if config.skipping != 'fast':
                    rollback_num += 1
                if readback_lock:
                    readback_lock = False
                    # if config.nvl_paged_rollback:
                    #     readback_rollback_block = rollback_num
            if config.skipping == 'fast':
                new_line = (preparse_say_for_store(who), preparse_say_for_store(what), current_voice, -2, nvl)
            elif readback_buffer[-1] and readback_buffer[-1][-1][3] == -2:
                rollback_num += 1
                new_line = (preparse_say_for_store(who), preparse_say_for_store(what), current_voice, -3, nvl)
            else:
                new_line = (preparse_say_for_store(who), preparse_say_for_store(what), current_voice, rollback_num, nvl)

            if config.readback_nvl_page:
                if len(readback_buffer[-1]) == config.readback_max_line:
                    readback_buffer.append([new_line])
                else:
                    readback_buffer[-1].append(new_line)
            else:
                readback_buffer.append(new_line)
            readback_prune()

    def delete_last_line():
        global readback_buffer
        if config.readback_nvl_page:
            del readback_buffer[-1][-1]
        else:
            del readback_buffer[-1]

    # remove text tags from dialogue lines
    disallowed_tags_regexp = ""
    for tag in config.readback_disallowed_tags:
        if disallowed_tags_regexp != "":
            disallowed_tags_regexp += "|"
        disallowed_tags_regexp += "{"+tag+"=.*?}|{"+tag+"}|{/"+tag+"}"

    import re
    readback_remove_tags_expr = re.compile(disallowed_tags_regexp) # remove tags undesirable in readback
    def preparse_say_for_store(input):
        global readback_remove_tags_expr
        if input:
            return re.sub(readback_remove_tags_expr, "", input)

    def readback_prune():
        global readback_buffer
        if config.readback_nvl_page:
            while len(readback_buffer) > config.readback_max_page:
                del readback_buffer[0]
        else:
            while len(readback_buffer) > config.readback_buffer_length:
                del readback_buffer[0]

    # keymap overriding to show text_history.
    def readback_catcher():
        ui.add(renpy.Keymap(rollback=(SetVariable("readback_yvalue", 1.0), ShowMenu("text_history"))))
        ui.add(renpy.Keymap(rollforward=ui.returns(None)))

    if config.readback_full:
        config.rollback_enabled = True
        config.overlay_functions.append(readback_catcher)

init -98 python:
    readback_yvalue = 1.0

    # support routines for scrolling screen

    class ReadbackAdj(ui.adjustment):
        def change(self,value):
            if value > self._range and self._value == self._range:
                return Return()
            else:
                return ui.adjustment.change(self, value)

    # support routines for paged screen

    def readback_change_page(y):
        global readback_yvalue
        readback_yvalue = int(y)
        renpy.restart_interaction()

    def readback_paged_max():
        max = len(readback_buffer) - 1
        if max > 0 and len(readback_buffer[max]) == 0:
            max = max - 1
        if current_line and not (len(readback_buffer[-1]) > 0 and current_line[:3] == readback_buffer[-1][-1][:3]) and len(readback_buffer[-1]) == config.readback_max_line:
                max += 1
        return max

    def readback_fix_yvalue():
        global readback_yvalue
        if not isinstance(readback_yvalue, int):
            readback_yvalue = readback_paged_max()

    def readback_show_start():
        global readback_yvalue
        readback_yvalue = 0
        renpy.restart_interaction()

    def readback_show_end():
        global readback_yvalue
        readback_yvalue = readback_paged_max()
        renpy.restart_interaction()

    def readback_show_prev_page():
        global readback_yvalue
        if (readback_yvalue > 0):
            readback_yvalue -= 1
            renpy.restart_interaction()

    def readback_show_next_page():
        global readback_yvalue
        if (readback_yvalue < readback_paged_max()):
            readback_yvalue += 1
            renpy.restart_interaction()
        else:
            return True

    class ReadbackScrollStart(Action):
        def __init__(self, adj):
            self.adj = adj
        def __call__(self):
            rv = self.adj.change(0)
            if rv is not None:
                return rv
            else:
                raise renpy.display.core.IgnoreEvent()

    class ReadbackScrollEnd(Action):
        def __init__(self, adj):
            self.adj = adj
        def __call__(self):
            rv = self.adj.change(self.adj.range)
            if rv is not None:
                return rv
            else:
                raise renpy.display.core.IgnoreEvent()

    class ReadbackScrollUp(Action):
        def __init__(self, adj):
            self.adj = adj
        def __call__(self):
            rv = self.adj.change(self.adj.value - self.adj.step)
            if rv is not None:
                return rv
            else:
                raise renpy.display.core.IgnoreEvent()

    class ReadbackScrollDown(Action):
        def __init__(self, adj):
            self.adj = adj
        def __call__(self):
            rv = self.adj.change(self.adj.value + self.adj.step)
            if rv is not None:
                return rv
            else:
                raise renpy.display.core.IgnoreEvent()

    def can_rollback(checkpoints):

        if not renpy.store._rollback or renpy.store._in_replay:
            return False

        # if not renpy.game.context().rollback:
        #     return False
        #
        if not renpy.config.rollback_enabled:
            return False

        revlog = []
        while renpy.game.log.log:
            rb = renpy.game.log.log.pop()
            revlog.append(rb)

            if rb.checkpoint:
                checkpoints -= 1

            if checkpoints <= 0:
                if renpy.game.script.has_label(rb.context.current):
                    revlog.reverse()
                    renpy.game.log.log = renpy.game.log.log + revlog
                    return True
        else:
            revlog.reverse()
            renpy.game.log.log = renpy.game.log.log + revlog
            return False

init -97:
    # Text History Screen.
    screen text_history:

        tag menu

        if config.readback_nvl_page:
            if not current_line and len(readback_buffer[0]) == 0:
                $ lines_to_show = [[]]
                
            elif current_line and len(readback_buffer[0]) == 0:
                $ lines_to_show = [[current_line]]
                
            elif current_line and not (len(readback_buffer[-1]) > 0 and current_line[:3] == readback_buffer[-1][-1][:3]):
                if len(readback_buffer[-1]) < config.readback_max_line:
                    $ lines_to_show = readback_buffer[:-1] + [readback_buffer[-1] + [current_line]]
                else:
                    $ lines_to_show = readback_buffer + [[current_line]]
                
            else:
                $ lines_to_show = readback_buffer

            $ readback_fix_yvalue()
            $ adj = ReadbackAdj(value=readback_yvalue, changed = readback_change_page, step = 1, page=1, range=readback_paged_max() )

            window:
                style_group "readback"

                side "c r":

                    frame:
                        yfill True
                        has vbox

                        null height 10

                        for line in lines_to_show[readback_yvalue]:

                            $ num = rollback_num - line[3] + 1
                            if len(readback_buffer[-1]) > 0 and config.nvl_paged_rollback and readback_buffer[-1][-1][4] and current_line[4]:
                                $ num -= 1
                            if line[3] == -1:
                                $ num = 0
                            if readback_buffer[-1] and readback_buffer[-1][-1][:3] == current_line[:3]:
                                $ num -= 1
                            if readback_buffer[-1] and readback_buffer[-1][-1][3] == -2:
                                $ num += 1

                            if config.readback_rollback:
                                button action [SensitiveIf(num >= 0 and
                                    rollback_num >= num and # for current_line
                                     can_rollback(num) and
                                     rollback_num -  readback_rollback_block >= num and # for nvl_paged_rollback
                                     not (readback_buffer[-1] and readback_buffer[-1][-1][3] == -2 and line[3] == -1) ), #for fast skip
                                    Function(renpy.rollback, False, num, True), Return()]:
                                    vbox:
                                        xfill True
                                        if line[0]:
                                            $ name = line[0]
                                            # label line[0]
                                        else:
                                            $ name = ""
                                        # $ name += str(num) # for debug

                                        text name + " " + line[1]
                                        # plays voice when clicked
                                        if line[2]:
                                            textbutton "voice" action Play("voice", line[2] ) xalign 1.0

                                        null height 10
                            else:
                                button action IF(line[2], true=Play("voice", line[2]), false=None):
                                    vbox:
                                        xfill True
                                        if line[0]:
                                            $ name = line[0]
                                        else:
                                            $ name = ""

                                        text name + " " + line[1]

                                        null height 10
                    bar adjustment adj style 'bbar'
                # $ nowpage = str(readback_yvalue + 1) + "/" + str(readback_paged_max() + 1)
                # text nowpage align (.80, 1.0) 
                textbutton _("Return") action Return() align (.97, 1.0)

            key "K_HOME" action readback_show_start
            key "K_END"  action readback_show_end
            key "rollback" action readback_show_prev_page
            key "rollforward" action readback_show_next_page

        else:

            if not current_line and len(readback_buffer) == 0:
                $ lines_to_show = []
            elif current_line and len(readback_buffer) == 0:
                $ lines_to_show = [current_line]
            elif current_line and not ( ( len(readback_buffer) == 3 and current_line[:3] == readback_buffer[-2][:3]) or current_line[:3] == readback_buffer[-1][:3]):  
                $ lines_to_show = readback_buffer + [current_line]
            else:
                $ lines_to_show = readback_buffer

            $ adj = ReadbackAdj(changed = readback_change_page, step = config.readback_scroll_step, page=1)

            window:
                style_group "readback"

                side "c r":

                    frame:
                        viewport:
                            mousewheel True
                            draggable True
                            yinitial readback_yvalue
                            yadjustment adj

                            vbox:
                                null height 10

                                for line in lines_to_show:

                                    if line[0]:
                                        label line[0]

                                    # if there's no voice just log a dialogue
                                    if not line[2]:
                                        text line[1]
                                    # else, dialogue will be saved as a button of which plays voice when clicked
                                    else: 
                                        textbutton line[1] action Play("voice", line[2] )

                                    null height 10

                    bar adjustment adj style 'bbar'
                textbutton _("Return") action Return() align (.97, 1.0)

            key "K_HOME"    action ReadbackScrollStart(adj)
            key "K_END" action ReadbackScrollEnd(adj)
            key "rollback"    action ReadbackScrollUp(adj)
            key "rollforward" action ReadbackScrollDown(adj)
init -2:
    python:
        style.create("bbar", "bar")
        style.setts_bar.ymaximum = 600
        style.bbar.xalign = 0.96
        style.bbar.left_bar = "images/bar_full.png"
        style.bbar.right_bar = "images/bar_full.png"
        style.bbar.xmaximum = 15
        style.bbar.left_gutter = 0
        style.bbar.right_gutter = 0
        style.bbar.top_gutter = 0
        style.bbar.bottom_gutter = 0
        style.bbar.thumb = None
        style.bbar.thumb_offset = 0
