label splashscreen:
    scene black
    with Pause(1)

    show text "Apresentamos" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    scene black
    with Pause(1)

    show text "Two Minutes to Midnight" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    play movie "video/rain.ogv" loop
    show movie with dissolve
    #with dissolve
    play sound "audio/rain.mp3" loop fadeout 1.0 fadein 1.0
    #p "..."

    with dissolve

    show text "Clique para continuar" with dissolve
    $ renpy.pause
    $ renpy.pause(50.0)
    hide text with dissolve


    return


#Teclas
init -5 python:
    style.timebar = Style(style.default)
    style.timebar.left_bar = Frame("ui/interface/timerfull.png", 0, 0)
    style.timebar.right_bar = Frame("ui/interface/timerempty.png", 0, 0)
    style.timebar.xmaximum = 695
    style.timebar.ymaximum = 27


screen battletime:
    timer 0.1 repeat True action If(time > 0, true=SetVariable('time', time - 0.02), false = [Hide('battletime'), Jump(timerjump)])    #Первый тайм - пауза между снятием времени, Второй тайм - минус времени     #####     Jump(timerjump)]) - командой этой мы обозначаем каким кодом мы будем вызывать переход если не успеет по времени персонаж сделать выбор

    bar:
     style "timebar"
     value time
     xalign 0.5 yalign 0.2



screen my_scr:

    timer 1.0 action If(my_timer>1, [SetVariable("my_timer", my_timer-1), Return("smth")], Return("loser")) repeat True

    text u"Tempo: [my_timer] s" size 30 color "ff0" xalign 0.0 yalign 0.1
    text u"Score - [score]" size 40 color "00c" xalign 0.5 yalign 0.1
    text u"Repetições - [counter]" size 20 color "c00"xalign 1.0 yalign 0.1


    key "d" action Return(u"d")
    key "j" action Return(u"j")
    key "k" action Return(u"k")
    key "l" action Return(u"l")


transform my_transform:
    on show:
        xalign 0.5 yalign 0.5
        alpha 0.0
        parallel:
            linear 0.2 zoom 10.0
        parallel:
            linear 0.1 alpha 1.0
            linear 0.1 alpha 0.0



label balbes:
    hide screen battletime
    hide screen timeout_event2
    pause 0.1
    "Вот и стой у разбитого корыта"
    return

#fim teclas

init python:
    # variáveis globais, serão alteradas dinamicamente
    felizAmizade = 0
    pontoAnterior = 0

define p = Character ("[nomeP]")
define a = Character ("[nomeApelido]")
define r = Character ("[nomeAlegre]")
define t = Character ("[nomeFofa]")
define m = Character ("[nomeTriste]")
define v = Character ("Televisão")
#Personagens
#image feliz = "images/feliz.png"
# The game starts here.
init python:
    import os, subprocess
    desktop = os.path.join(os.environ['HOMEPATH'], 'Desktop')
    def create_desktop_folder(folder):
        create_path = os.path.join(desktop, folder)
        if not os.path.isdir(create_path):
            os.mkdir(create_path)

    def copy_to_desktop(file_path, folder):
        copy_path = os.path.join(desktop, folder, os.path.basename(file_path))
        copy_file = renpy.file(file_path)
        f = open(copy_path, 'wb')
        f.write(copy_file.read())
        f.close()

    def open_in_explorer(folder):
        open_path = os.path.join(desktop, folder)
        subprocess.call(['explorer', open_path], shell=True)

    from ctypes import windll
    MB_OK = 0x0
    MB_OKCXL = 0x01
    MB_YESNOCXL = 0x03
    MB_YESNO = 0x04
    MB_HELP = 0x4000
    ICON_EXLAIM = 0x30
    ICON_INFO = 0x40
    ICON_STOP = 0x10

    def message_box(msg, title, flags):
        return windll.user32.MessageBoxW(0, msg, title, flags)

    def error_message(msg, title):
        return message_box(msg, title, ICON_STOP)

label error_message(msg, title='Two Minutes to Midnight'):
    $ error_message(msg, title)
    return

image movie = Movie(size=(1920, 1080), xpos=0, ypos=0, xanchor=0, yanchor=0)

label start:
    $ score = 0
    $ prev_hit = "nothing"
    $ counter = 0
    $ contador = 0
    "Algumas informações devem ser inseridas para uma melhor experiência:"
    $nomeP = renpy.input("{size=50}{font=Computerfont.ttf}Qual é o seu nome?{/font}{/size}")
    $nomeApelido = renpy.input("{size=50}{font=Computerfont.ttf}Qual é o seu apelido?{/font}{/size}")
    $nomeAlegre = renpy.input("{size=50}{font=Computerfont.ttf}Um nome para sua amiga mais alegre{/font}{/size}")
    $nomeTriste = renpy.input("{size=50}{font=Computerfont.ttf}Um nome para sua amiga séria{/font}{/size}")
    $nomeFofa = renpy.input("{size=50}{font=Computerfont.ttf}Um nome para sua amiga mais fofa{/font}{/size}")

    play movie "video/matrix.ogv" loop
    show movie with dissolve
    "{size=50}{font=Computerfont.ttf}Você sabe o que é tempo?{/font}{/size}"
    menu tempo:
        "Sim":
            "{size=50}{font=Computerfont.ttf}Você deve achar que essa é uma pergunta idiota{/font}{/size}"
            "{size=50}{font=Computerfont.ttf}Que todos os seres humanos sabem o significado{/font}{/size}"
            "{size=50}{font=Computerfont.ttf}Mas na verdade...{/font}{/size}"

        "Não":
            "{size=50}{font=Computerfont.ttf}Muitos acham que todo ser humano sabe o significado{/font}{/size}"
            "{size=50}{font=Computerfont.ttf}Mas na verdade...{/font}{/size}"

    "{size=50}{font=Computerfont.ttf}O tempo é a duração relativa das coisas que cria no ser humano a ideia de presente, passado e futuro{/font}{/size}"
    "{size=50}{font=Computerfont.ttf}É o período contínuo no qual os eventos se sucedem.{/font}{/size}"
    "{size=50}{font=Computerfont.ttf}Uma roda em movimento.{/font}{/size}"


"{size=50}{font=Computerfont.ttf}Tudo isso inscrito em vários papéis chamados 'vida'{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Que é o que liga tudo.{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Linhas{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Círculos.{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Espirais girando sem parar{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Como as engrenagens de um relógio{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Onde tudo está em seu devido lugar.{/font}{/size}"
"{size=50}{font=Computerfont.ttf}...{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Em mil novecentos e quarenta e sete, o Comitê do Boletim de Cientistas Atômicos criou o 'Relógio do Juízo Final'{/font}{/size}"
"{size=50}{font=Computerfont.ttf}o símbolo apocalíptico nasceu no contexto da corrida nuclear que se materializou em agosto de  mil novecentos e quarenta e cinco{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Com as bombas lançadas pelos Estados Unidos sobre as cidades japonesas de Hiroshima e Nagasaki.{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Quando começou, o ponteiro do relógio{/font}{/size}"
"{size=50}{font=Computerfont.ttf}uma metáfora visual do perigo de uma destruição deliberada do planeta, marcava sete minutos para a meia-noite.{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Agora, estamos a dois minutos.{/font}{/size}"
"{size=50}{font=Computerfont.ttf}...{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Você gostaria de mudar o futuro, [nomeP]?{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Ou melhor...{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Mudar o tempo?{/font}{/size}"
menu qualquercoisa:
    "Sim":
        "{size=50}{font=Computerfont.ttf}Ótimo!{/font}{/size}"
        "{size=50}{font=Computerfont.ttf}Todos desejam isso{/font}{/size}"

    "Não":
        "{size=50}{font=Computerfont.ttf}Você não precisa mentir para mim{/font}{/size}"
        "{size=50}{font=Computerfont.ttf}Todos desejam isso{/font}{/size}"

"{size=50}{font=Computerfont.ttf}Mas nem todos têm essa chance...{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Eu queria fazer alguma coisa.{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Algo que eu pudesse olhar e ver que fiz a diferença{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Foi assim que surgiu o Two Minutes to Midnight.{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Primeiro, eu precisava de um Receptor Vivente{/font}{/size}"
menu receptor:
    "Então você precisa de mim?":
        "{size=50}{font=Computerfont.ttf}Sim, [nomeP].{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Mas este é um caminho sem volta{/font}{/size}"
"{size=50}{font=Computerfont.ttf}e nem todos querem fazer parte de algo maior{/font}{/size}"
"{size=50}{font=Computerfont.ttf}por isso eu busco ajuda.{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Isso será doloroso{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Não será fácil.{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Viver não é fácil{/font}{/size}"
"{size=50}{font=Computerfont.ttf}E a morte é mais difícil ainda{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Para uma melhor experiência,será criada uma pasta em sua área de trabalho{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Deste modo, posso te enviar mensagens durante por lá{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Sinta-se livre para checar a pasta{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Mas é claro, nada será feito sem sua permissão{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Você aceita os termos para continuar?{/font}{/size}"
menu criarpasta:
    "{size=50}{font=Computerfont.ttf}Aceito{/font}{/size}":
        "{size=50}{font=Computerfont.ttf}Sempre tive uma boa percepção sobre você.{/font}{/size}"
        $ minutes_folder = 'Two Minutes to Midnight'
        $ create_desktop_folder(minutes_folder)
        "{size=50}{font=Computerfont.ttf}A pasta foi criada com sucesso!{/font}{/size}"
        "{size=50}{font=Computerfont.ttf}Deseja abrir a pasta?{/font}{/size}"
        menu:
            "Sim":
                $ open_in_explorer(minutes_folder)
                "{size=50}{font=Computerfont.ttf}Prontinho!{/font}{/size}"


            "Não":
                "{size=50}{font=Computerfont.ttf}Certo! Vamos continuar!{/font}{/size}"

    "{size=50}{font=Computerfont.ttf}Não aceito{/font}{/size}":
        "{size=50}{font=Computerfont.ttf}Two Minutes to Midnight se trata de um jogo interativo{/font}{/size}"
        "{size=50}{font=Computerfont.ttf}Com a intenção de melhorar a experiência do jogador com mecânicas diferentes :){/font}{/size}"
        "{size=50}{font=Computerfont.ttf}Falamos sobre fontes de energia sustentáveis e formas de ajudar o mundo!{/font}{/size}"
        "{size=50}{font=Computerfont.ttf}Sua experiência será diferenciada com essa escolha{/font}{/size}"
        "{size=50}{font=Computerfont.ttf}Mas não faremos nada sem sua permissão{/font}{/size}"


"{size=50}{font=Computerfont.ttf}Não se esqueça que suas decisões têm consequências{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Há anos eu estudo como essas consequências podem mudar o mundo.{/font}{/size}"
"{size=50}{font=Computerfont.ttf}E em todo lugar existem sistemas complexos e dinâmicos rigorosamente deterministas{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Mas que apresentam um fenômeno fundamental de instabilidade chamado sensibilidade às condições iniciais.{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Tais fenômenos, modulando uma propriedade suplementar de recorrência, torna-os não previsíveis na prática a longo prazo.{/font}{/size}"
"{size=50}{font=Computerfont.ttf}A alta sensibilidade às condições inciais, porém, dá ao sistema não linear a característica de instabilidade{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Que faz com que seja incorretamente confundido com um sistema aleatório.{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Você acredita que tudo acontece por acaso?{/font}{/size}"
menu acredita:
    "Sim":
        "{size=50}{font=Computerfont.ttf}Bem,{/font}{/size}"

    "Não":
        "{size=50}{font=Computerfont.ttf}Bem,{/font}{/size}"
"{size=50}{font=Computerfont.ttf}a formação de uma nuvem no céu, por exemplo, pode ser desencadeada e se desenvolver com base em centenas de fatores{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Como o calor{/font}{/size}"
"{size=50}{font=Computerfont.ttf}A pressão{/font}{/size}"
"{size=50}{font=Computerfont.ttf}A evaporação da água{/font}{/size}"
"{size=50}{font=Computerfont.ttf}condições do Sol{/font}{/size}"
"{size=50}{font=Computerfont.ttf}eventos sobre a superfície...{/font}{/size}"
"{size=50}{font=Computerfont.ttf}inúmeros outros.{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Se as condições de todos estes fatores forem conhecidas com exatidão no momento presente, o exato formato de uma nuvem no futuro pode ser previsto com exatidão.{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Porém, como as condições atuais exatas não são conhecidas, o comportamento futuro também é difícil de prever.{/font}{/size}"
menu consequencia:
    "E qual seria a consequência disso?":
        "{size=50}{font=Computerfont.ttf}Como Consequência,{/font}{/size}"
"{size=50}{font=Computerfont.ttf}A instabilidade dos resultados é que mesmo sistemas determinísticos{/font}{/size}"
"{size=50}{font=Computerfont.ttf}os sistemas têm resultados determinados por leis de evolução bem definidas{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Apresentam uma grande sensibilidade a perturbações e erros, levando a resultados que são, na prática, imprevisíveis{/font}{/size}"
"{size=70}{font=Computerfont.ttf}Embora não sejam aleatórios.{/size}"
"{size=50}{font=Computerfont.ttf}Enquanto o comportamento futuro do sistema caótico pode ser determinado se as condições iniciais forem perfeitamente conhecidas{/font}{/size}"
"{size=50}{font=Computerfont.ttf}o mesmo não ocorre com um sistema aleatório.{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Mesmo em sistemas nos quais não há erros, inexatidões microscópicas na determinação do estado inicial e atual do sistema podem ser amplificados{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Levando a um comportamento futuro difícil de prever.{/font}{/size}"
"{size=50}{font=Computerfont.ttf}É o que se chama de Caos Determinístico{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Você tem um grande poder em suas mãos{/font}{/size}"
"{size=50}{font=Computerfont.ttf}A chance de mudar Tudo{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Eu sei que as coisas parecem confusas agora{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Mas logo, fará sentido{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Obrigada por querer ajudar.{/font}{/size}"
menu denada:
    "De nada!":
        "{size=50}{font=Computerfont.ttf}:){/font}{/size}"
"{size=50}{font=Computerfont.ttf}Eu passei muito tempo tentando achar uma resposta{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Mas não era só eu que precisava mudar{/font}{/size}"
"{size=50}{font=Computerfont.ttf}...{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Não há mais tempo.{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Não há como facilitar as coisas para você{/font}{/size}"
"{size=50}{font=Computerfont.ttf}A mudança deve partir de nós mesmos{/font}{/size}"
"{size=50}{font=Computerfont.ttf}E eu espero que isso ajude em alguma coisa.{/font}{/size}"


"{size=50}{font=Computerfont.ttf}...{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Tudo acabará bem{/font}{/size}"

stop music
"{size=50}{font=Computerfont.ttf}Eu tenho que ir.{/font}{/size}"
"{size=50}{font=Computerfont.ttf}Você precisa ajudá-las.{/font}{/size}"
"{size=50}{font=Computerfont.ttf}É engraçado como pode-se colocar uma ideia na cabeça de alguém...{/font}{/size}"

hide movie with dissolve
stop movie

#scene bg

#hide black

#scene bg sala
play movie "video/rain.ogv" loop
show movie with dissolve
#with dissolve
#play sound "audio/rain.mp3" loop fadeout 1.0 fadein 1.0
play music "audio/primeiracena.mp3" fadeout 1.0 fadein 1.0
#p "..."

with dissolve

show text "{size=+50}Ato 1 - o sonho{/size}" with dissolve
$ renpy.pause
$ renpy.pause(3.0)
hide text with dissolve

p "Oh!"
p "Que sonho estranho!"
p "Há muito tempo eu não sonhava com minha irmã..."
p "Desde que ela terminou seus estudos, quase não nos falamos mais."
p "Ela anda muito ocupada trabalhando em uma empresa de tecnologia"
p "Mas nunca nos conta exatamente sobre o que faz..."
p "Espero que não seja nada ilegal!"
p "Acho que o barulho dos raios acabou me acordando..."
p "Apesar de eu sempre gostar da chuva"
p "É ótima para dormir"
p "E me dá uma sensação de calma"
p "Pegar num sono durante uma tempestade me traz o sentimento de lucidez"
p "Como se fosse possível ter uma recordação muito clara do que está acontecendo lá fora e em meu inconsciente"
p "Assim eu consigo atingir minha paz"
p "Mas..."
p "Qual foi o meu sonho mesmo?"
stop movie
hide bg sala with dissolve
p "Meu Deus!"
p "Eu acabei dormindo demais!"
p "De novo!"
p "Mas dessa vez acordei cansada..."
p "Ah, não importa!"
p "O tempo assim é tão bom para dormir..."
p "Acho que vou ficar deitada mais um pouco"
#p "hoje é o dia"
#p "..."
#p "Há dois anos, tudo mudou."
#p "O acidente mudou não apenas minha vida, mas a de todos a sua volta."
#p "A usina Kanashimi realizava seus trabalhos como de costume"
#p "até que uma falha no sistema ocasionou a exposição de milhares de pessoas, animais e plantas à alta radiação"
#p "extinguindo toda a forma de vida da pequena cidade"
#p "entre elas, minha família."
#p "Os impactos são incalculáveis"
#p "Toda a região foi contaminada, vazando material radioativo para a atmosfera e ocasionando centenas de casos de câncer entre as comunidades vizinhas."
#p "Tudo o que conhecia foi reduzido a nada."
#p "..."
#p "Não posso me perdoar."
#p "Eu não estava lá"
#p "Quanto mais tenho que sofrer até que eu possa os encontrar novamente?"
#p "Estou sempre procurando suas imagens em algum lugar"
#p "mas é impossível."
#p "não há mais nada que posso fazer, a não ser continuar."

stop sound
"..."
show feliz alegre with dissolve

play music "audio/tamau01.mp3" fadeout 1.0 fadein 1.0

r "[nomeP]!"
scene quarto luz acesa
with dissolve
show feliz pensativa at center:
    linear .25 zoom 1.08
r "O que você ainda tá fazendo em casa??"
show feliz pensativa at center:
    linear .25 zoom 1.00
"Mudei de país aos 19 anos."
"Desde então, moro com outras três garotas e divido as despesas da casa."
"[nomeAlegre] é uma de minhas colegas"
"A mais animada, eu diria"
"Ela estuda o mesmo que minha irmã, apesar de não ser tão focada quanto ela."
"De certa forma, isso faz eu me sentir um pouco mais próxima de casa."

show feliz alegre at center:
    linear .25 zoom 1.08
r "[nomeP], levanta logoooooooooooo"
show feliz pensativa at center:
    linear .25 zoom 1.08
r "Ué, você tava falando com quem?"
show feliz alegre at center:
    linear .25 zoom 1.08
r "Você combinou de sair com a gente e não vai escapar dessa vez"
r "Levanta logo daí e se arruma, quem sabe dessa vez você não encontra o..."

#call krix
#pause 1
#centered "{size=52}Você fez {color=#f2b627}[pointk] pontos!"


show feliz alegre2 at center:
    linear .25 zoom 1.00
p "Cala a boca e me deixa dormir"
show feliz pensativa at center:
    linear .25 zoom 1.08
r "Vamos, por favooooooooooor"
show feliz pensativa at center:
    linear .25 zoom 1.00
p "Tá chovendo, a gente podia ficar em casa assistindo uns filmes..."
show feliz brava at center:
    linear .25 zoom 1.08
r "NÃO, é já é a milésima vez que você usa essa desculpa."
r "Eu não vou sair daqui até você levantar"
show feliz alegre at center:
    linear .25 zoom 1.08
r "Vai vai vai"
r "Anda"
r "Levanta"
show feliz alegre2 at center:
    linear .25 zoom 1.08
r "Bom, parece que eu vou ter que fazer cócegas em você..."


hide black
with dissolve

menu fight:
    "Se render":
        python:
            felizAmizade += 30
        call chamarBarraMais(felizAmizade) from _call_chamarBarraMais

        p "Ok, ok, você venceu"
        p "Se eu for, você para de me irritar?"
        r "CLAAAAAAAROOOOO que sim, prometo que nunca mais vou chegar perto do seu quarto"
        p "Como se isso fosse verdade..."
        r "Vamos descer, as meninas já estão esperando"

        scene sala
        with dissolve

        show rosto triste at left with dissolve
        show fofa alegre at right with dissolve
        show feliz pensativa at center with dissolve

        show rosto triste at left:
            linear .25 zoom 1.08
        m "Então [nomeAlegre], o que você queria falar com a gente?"

        "[nomeTriste] é três anos mais velha. É um pouco tímida, mas sempre sabe o que dizer e conforta todas nós"

        show fofa alegre at right:
            linear .25 zoom 1.00
        show feliz alegre at center:
            linear .25 zoom 1.08
        show rosto triste at left:
            linear .25 zoom 1.08
        show rosto triste at left:
            linear .25 zoom 1.00
        r "Ah hahahahahaha daquilo, lembra?"
        show rosto triste at left:
            linear .25 zoom 1.08
        show feliz alegre at center:
            linear .25 zoom 1.00
        show fofa desconfiada at right:
            linear .25 zoom 1.00
        show rosto triste at left:
            linear .25 zoom 1.00
        t "Aquilo o que?"

        "[nomeFofa] é minha melhor amiga. Foi a primeira da casa a fazer amizade comigo."
        show feliz alegre at center:
            linear .25 zoom 1.08
        show rosto triste at left:
            linear .25 zoom 1.00
        show fofa desconfiada at right:
            linear .25 zoom 1.00
        r "Nós íamos sair..."
        show feliz alegre at center:
            linear .25 zoom 1.00
        show rosto triste at left:
            linear .25 zoom 1.08
        m "Íamos?"
        #show rosto triste at left:
        #    linear .25 zoom 1
        r "Bom, a [nomeP] já está pronta pra gente ir então vamos..."
        show feliz alegre at center:
            linear .25 zoom 1.00
        p "Eu não concordei com isso"
        show rosto triste confuso at left:
            linear .25 zoom 1.08
        m "Ahh [nomeAlegre], você fez isso de novo?"
        show rosto triste confuso at left:
            linear .25 zoom 1.00
        show feliz alegre at center:
            linear .25 zoom 1.08
        r "Mas é claro, vocês nunca saem de casa"
        show fofa alegre at right:
            linear .25 zoom 1.08
        show feliz alegre at center:
            linear .25 zoom 1.00
        t "Tudo bem, a gente pode sair dessa vez"
        show rosto triste confuso at left:
            linear .25 zoom 1.00
        t "Até porque, a [nomeP] finalmente vai com a gente!"
        show fofa alegre at right:
            linear .25 zoom 1.00
        show rosto triste at left:
            linear .25 zoom 1.08
        m "Tudo bem, eu estava pensando em sair mesmo"
        show rosto triste at left:
            linear .25 zoom 1.00
        show feliz alegre at center:
            linear .25 zoom 1.08
        r "EBAAAAAAAAAAAAAA"
        r "Parou de chover, onde vocês querem ir?"

        menu sairq:
            "Café":
                scene cafe with dissolve
                show rosto triste at left with dissolve
                show fofa alegre at right with dissolve
                show feliz pensativa at center with dissolve
                "Esse café é bem perto de casa. Adoro ficar aqui para fazer meus trabalhos."
                p "[nomeApelido], o que você tá esperando?"
                m "Realmente, você anda muito estranha..."
                p "Vocês ouviram esse barulho?"

                jump morte

            "Bar":
                scene bar1 with dissolve
                show rosto triste at left with dissolve
                show fofa alegre at right with dissolve
                show feliz pensativa at center with dissolve
                p "Enfim, estamos no bar"
                p "[nomeApelido], o que você tá esperando?"
                m "Realmente, você anda muito estranha..."

                jump morte


            "Parque":
                scene parque with dissolve
                show rosto triste at left with dissolve
                show fofa alegre at right with dissolve
                show feliz pensativa at center with dissolve
                p "Enfim, estamos no parque"
                p "[nomeApelido], o que você tá esperando?"
                m "Realmente, você anda muito estranha..."

                menu morte:
                    "E foi assim que tudo aconteceu...":
                        "Como assim?"
                        scene black
                        stop music
                        play sound "audio/boom.mp3" loop fadeout 1.0 fadein 1.0
                        #play movie "video/destruicao.ogv" loop
                        #show movie with dissolve
                        play movie "video/destruicao.ogv" loop
                        show movie with dissolve
                        "{size=50}{font=Computerfont.ttf}A morte...{/font}{/size}"
                        "A discussão em torno da utilização de energia nuclear é muita."
                        "De um lado os governos afirmam que esta é uma alternativa segura, eficiente e que não polui."
                        "De outro, encontram-se ambientalistas que alertam sobre o perigo da poluição nuclear e de possíveis desvios dos materiais físseis por terroristas"
                        "além dos acidentes com o transporte de materiais radioativos."
                        "E foi deste modo que minha irmã morreu."

                        "O acidente mudou não apenas minha vida, mas a de todos a sua volta."
                        "A usina realizava seus trabalhos como de costume"
                        "até que uma falha no sistema ocasionou a exposição de milhares de pessoas, animais e plantas à alta radiação"
                        "extinguindo toda a forma de vida da pequena cidade"
                        "entre elas, minha irmã e suas amigas."
                        "Os impactos são incalculáveis"
                        "Toda a região foi contaminada, vazando material radioativo para a atmosfera e ocasionando centenas de casos de câncer entre as comunidades vizinhas."
                        "Tudo o que conhecia foi reduzido a nada..."

                        call error_message('AJUDE-AS') from _call_error_message_6
                        stop sound
                        stop movie
                        scene black

                        menu posmorte:
                            "E foi assim...":
                                p "Eu estarei aqui."
                                show text "{size=+50}Ato 2 - Pós morte. Algum tempo antes{/size}" with dissolve
                                $ renpy.pause
                                $ renpy.pause(3.0)
                                hide text with dissolve

                        scene sala with dissolve
                        play music "audio/televisao.mp3" fadeout 1.0 fadein 1.0
                        v "Com a criação de novas usinas termonucleares para geração de energia"
                        v "a quantidade de resíduos que deverá ser estocada, também aumentará."
                        m "Alguém desliga essa TV! Eu quero dormirrrrrrrr!"
                        menu television:
                                "Desligar":
                                    stop music
                                    p "Ahh, ok. Acho que vou dormir"

                                    #call error_message('Infelizmente você fracassou') from _call_error_message_5

                                    "Você tem uma nova mensagem"
                                    scene black

                                    $ sms_text = []

                                    $ sms_name = "IA"

                                    $ sms_on()

                                    #"Você possui uma nova mensagem"

                                    "{#l}{size=20}Embora possua muitas vantagens e países interessados na geração de energia nuclear, a sua produção apresenta diversos riscos ao meio ambiente e seres vivos, já que se baseia na manipulação de produtos radioativos muito nocivos à vida e ao ambiente.”{/size}"

                                    "{#l}{size=20}Diante desses riscos, a produção de energia nuclear exige um grande controle para evitar qualquer tipo de vazamento ou acidente envolvendo produtos radioativos{/size}"
                                    $ sms_clear()
                                    "{#l}{size=20}já que a contaminação radioativa pode ocasionar inúmero impactos{/size}"

                                    "{#l}{size=20}Mas ainda há como mudar{image=smile.png}{/size}"
                                    "{#l}{size=20}E eu posso mostrar como!{/size}"
                                    "{#l}{size=20}Não desista{/size}"
                                    "{#l}{size=20}Tente novamente!{/size}"
                                    $ sms_clear()
                                    "{#l}{size=20}Com pequenas escolhas, você pode mudar o mundo!{/size}"
                                    $ sms_clear()
                                    pause 1.0
                                    #"{#r}{size=20}Bem também.{/size}"
                                    #"Muito legal esse teste"
                                    #"{#l}{size=20}Pois é...{/size}"

                                    #menu uaiodasjids:
                                    #    "Sim":
                                    #        "{#r}Olá! Como vai?"
                                    #        "{#l}Vou bem, e você?{image=smile.png}"
                                    #    "Não":
                                    #        "{#r}Bem também."

                                    $ sms_clear()
                                    pause 1.0

                                    $ sms_off()

                                    "Volteremos para o menu"
                                    "Tente novamente"
                                    return


                                    #FIM DO CELULAR

                                    #jump television




                                    #$ copy_to_desktop('ZXUgbsOjbyBxdWVyaWEgcXVlIGZvc3NlIGFzc2lt/aaaaaaaaaaaaaaaaa.txt', minutes_folder)


                                "Prestar atenção":
                                    p "Acho que tenho que ouvir isso..."

                                    v "o lixo nuclear possui a capacidade de permanecer ativo por milhares de anos"
                                    v "exigindo o monitoramento constante e,"
                                    v "no caso de acidentes as conseqüências são muito piores"
                                    v "podendo causar danos por várias gerações"
                                    v "Só o Japão produz anualmente mais de uma tonelada de resíduos radioativos"
                                    v "que são enviados para França e Reino Unido para o reprocessamento."
                                    v "Ou seja, a energia nuclear polui."
                                    v "Diante de vários riscos, a produção de energia nuclear exige um grande controle"
                                    v "para evitar qualquer tipo de vazamento ou acidente envolvendo produtos radioativos,"
                                    v "já que a contaminação radioativa pode ocasionar"
                                    v "Escassez de solo, ar e água adequados para a agricultura e para a manutenção da vida na área afetada"
                                    v "Mutação genética de espécies de plantas, insetos e animais"
                                    v "Queimaduras, alterações na produção do sangue"
                                    v "Diminuição da resistência imunológica"
                                    v "Surgimento de diversas doenças, como o câncer, alterações gastrintestinais, problemas na medula óssea"
                                    v "Infertilidade e má-formação dos órgãos reprodutores e de fetos submetidos à alta radiação"

                                    show rosto triste at left:
                                        linear .25 zoom 1.08
                                    stop music


                                    m "E é por isso que eu acho que todo mundo deve morrer..."
                                    m "É por isso que sou adepta ao Movimento Voluntário de Extinção Humana"

                                    "Deseja abrir uma página em seu navegador?"

                                    menu abrirvhemt:
                                        "Sim":
                                            python:
                                                import webbrowser
                                                webbrowser.open('http://www.vhemt.org/pindex.htm')

                                        "Não":
                                            "Você recebeu uma mensagem"
                                            #AQUI VAI O CELULAR

                                            scene black

                                            $ sms_text = []

                                            $ sms_name = "IA"

                                            $ sms_on()

                                            #"SMS text."

                                            "{#l}{size=20}O Movimento de Extinção Humana Voluntária utiliza a frase “Que possamos viver muito, e desaparecer”{/size}"

                                            "{#l}{size=20}Assim, acreditam que suprimir a raça humana ao, voluntariamente, deixar de procriar, permitirá à biosfera terrestre retornar à boa saúde.{/size}"
                                            "{#l}{size=20}Condições sufocadas e escassez de recursos apresentarão melhora à medida que nos tornarmos menos densos.{/size}"
                                            $ sms_clear()
                                            "{#l}{size=20}Mas ainda há como mudar{image=smile.png}{/size}"
                                            "{#l}{size=20}E eu posso mostrar como!{/size}"
                                            "{#l}{size=20}Não desista{/size}"

                                            pause 1.0
                                            #"{#r}{size=20}Bem também.{/size}"
                                            #"Muito legal esse teste"
                                            #"{#l}{size=20}Pois é...{/size}"

                                            #menu uaiodasjids:
                                            #    "Sim":
                                            #        "{#r}Olá! Como vai?"
                                            #        "{#l}Vou bem, e você?{image=smile.png}"
                                            #    "Não":
                                            #        "{#r}Bem também."

                                            $ sms_clear()
                                            pause 1.0

                                            $ sms_off()
                                            "..."

                                            #FIM DO CELULAR


                                    m "O ser humano apenas destrói a natureza"


                                    menu final:
                                                "Concordar":
                                                    show rosto triste at left:
                                                        linear .25 zoom 1.00
                                                    p "Realmente. a humanidade não tem mais jeito"
                                                    p "Não há mais o que fazer, apenas desistir"
                                                    p "E esperar para morrer..."

                                                    call error_message('Infelizmente você fracassou') from _call_error_message_20

                                                    "Deseja abrir uma página em seu navegador?"

                                                    menu pagina:
                                                        "Sim":


                                                    #$ copy_to_desktop('ZXUgbsOjbyBxdWVyaWEgcXVlIGZvc3NlIGFzc2lt/aaaaaaaaaaaaaaaaa.txt', minutes_folder)

                                                            python:
                                                                import webbrowser
                                                                webbrowser.open('https://brasilescola.uol.com.br/geografia/principais-riscos-geracao-energia-nuclear-para-meio-ambiente.htm')

                                                                "Pense mais sobre isso e tente novamente!"

                                                        "Não":
                                                            "Você recebeu uma mensagem"
                                                        #AQUI VAI O CELULAR

                                                            scene black

                                                            $ sms_text = []

                                                            $ sms_name = "IA"

                                                            $ sms_on()

                                                            #"SMS text."

                                                            "{#l}{size=20}Existe várias formas de mudar o mundo{/size}"

                                                            "{#l}{size=20}Ainda há solução!{/size}"
                                                            "{#l}{size=20}Por exemplo, Aaproveite a claridade do sol, abrindo janelas, cortinas e persianas.{/size}"
                                                            "{#l}{size=20}Separe os lixos (vidro, papel, metal e plástico) e coloque na rua no dia da coleta seletiva em seu bairro{/size}"

                                                            $ sms_clear()
                                                            "{#l}{size=20}ainda há como mudar{image=smile.png}{/size}"
                                                            "{#l}{size=20}E eu posso mostrar como!{/size}"
                                                            "{#l}{size=20}Não desista{/size}"
                                                            pause 1.0
                                                            #"{#r}{size=20}Bem também.{/size}"
                                                            #"Muito legal esse teste"
                                                            #"{#l}{size=20}Pois é...{/size}"

                                                            #menu uaiodasjids:
                                                            #    "Sim":
                                                            #        "{#r}Olá! Como vai?"
                                                            #        "{#l}Vou bem, e você?{image=smile.png}"
                                                            #    "Não":
                                                            #        "{#r}Bem também."

                                                            $ sms_clear()
                                                            pause 1.0

                                                            $ sms_off()
                                                            "..."

                                                            #FIM DO CELULAR

                                                            "Deseja que eu envie a cópia de dicas para seu desktop?"
                                                            menu copia:
                                                                    "Sim":
                                                                        $ copy_to_desktop('ZXUgbsOjbyBxdWVyaWEgcXVlIGZvc3NlIGFzc2lt/sssssssss.txt', minutes_folder)
                                                                        "Pense nisso!"
                                                                        "Tente novamente"
                                                                        return


                                                                    "Não":
                                                                        "Pense nisso!"
                                                                        "Tente novamente"
                                                                        return


                                                        "Pense mais sobre isso e tente novamente!"



                                                "Discordar":
                                                    show rosto triste at center:
                                                        linear .25 zoom 1.00
                                                    p "Eu não acho isso"
                                                    p "Ainda tem como mudar"
                                                    p "Existem muitas fontes de energia renováveis"
                                                    p "A luz solar, por exemplo"
                                                    p "é um recurso natural mais abundante e com maior disponibilidade em todo o planeta"
                                                    p "Um painel solar, por exemplo, possui grande eficiência energética."
                                                    p "Ou a energia eólica, através da força dos ventos,"
                                                    p "gerando energia através da força motriz gerada nas turbinas."
                                                    p "Nós podemos fazer algo para mudar!"

                                                    show rosto triste at center:
                                                        linear .25 zoom 1.08
                                                    m "Mas como?"
                                                    show rosto triste at center:
                                                        linear .25 zoom 1.00
                                                    p "Se nós juntarmos e mostrasse para as pessoas que ainda dá tempo"

                                                    "Deseja abrir páginas em seu navegador?"

                                                    menu abir:
                                                        "Sim":
                                                            python:
                                                                import webbrowser
                                                                webbrowser.open('https://world.mongabay.com/brazilian/610.html')
                                                        "Não":
                                                            "Sim, ainda há um resto de esperança em mim..."


                                                    show rosto triste at center:
                                                        linear .25 zoom 1.08

                                                    m "Como você está dizendo para essa pessoa que está jogando?"

                                                    show rosto triste at center:
                                                        linear .25 zoom 1.00

                                                    p "Exato"

                                                    p "Com os avanços tecnológicos, o ser humano esquece que é dependente da natureza"

                                                    p "Portanto temos que usar a tecnologia a nosso favor"

                                                    p "Para ver se conseguimos chamar a atenção das pessoas"

                                                    p "Olhe a sua volta agora"

                                                    p "Nós tivemos que criar um jogo desse jeito para ver se você se tocasse"

                                                    show rosto triste at center:
                                                        linear .25 zoom 1.08

                                                    m "Metalinguístico. Gostei!"

                                                    show rosto triste at center:
                                                        linear .25 zoom 1.00

                                                    p "Eu sei que você pode fazer mais do que isso"

                                                    p "E não salvar apenas garotas em um jogo"

                                                    p "Mas sim"

                                                    p "Se salvar"

                                                    "Deseja abrir páginas em seu navegador?"

                                                    menu paginasnafosfd:
                                                        "Sim":

                                                            python:
                                                                import webbrowser
                                                                webbrowser.open('http://meioambiente.culturamix.com/natureza/cuidados-com-o-meio-ambiente')

                                                            python:
                                                                import webbrowser
                                                                webbrowser.open('https://escolakids.uol.com.br/10-maneiras-preservar-meio-ambiente.htm')

                                                            python:
                                                                import webbrowser
                                                                webbrowser.open('http://meioambiente.culturamix.com/ecologia/cuidados-com-a-natureza')

                                                            p "Por que você não tira um tempo para ler sobre isso?"

                                                            p "Não depende de mim, [nomeP]"

                                                            p "Eu sou apenas programada para dizer isso"

                                                            p "Mas você sim"

                                                            p "Pode levantar da cadeira agora"

                                                            p "E fazer a diferença"

                                                            p "Ou nada irá mudar..."

                                                            p "Quando você deixa de fazer algo para ajudar a todos"

                                                            p "Ou quando você utiliza materiais poluentes"

                                                            p "Você está matando todos aos poucos"

                                                            p "Até mesmo você"

                                                            p "Quem você ama"

                                                            p "Aproveite enquanto ainda dá tempo"

                                                            p "E não use a desculpa que você não vai estar aqui quando o pior acontecer"

                                                            p "Pois quem você ama, vai"

                                                            p "E toda a humanidade"

                                                            p "Que depende de você"

                                                            p "Desculpe por ser dura demais"

                                                            p "Eu carrego seu nome, mas sou apenas mais alguém tentando mudar"

                                                            p "Espero que isso ajude em algo"

                                                            call error_message('Obrigada por jogar!') from _call_error_message23

                                                            #$ copy_to_desktop('ZXUgbsOjbyBxdWVyaWEgcXVlIGZvc3NlIGFzc2lt/sssssssss.txt', minutes_folder)

                                                            #$ open_in_explorer(minutes_folder)

                                                            "O jogo será fechado, fique a vontade para tentar outras escolhas :)"

                                                            "Obrigada!"

                                                            $ renpy.quit()

                                                        "Não":
                                                            p "Não depende de mim, [nomeP]"

                                                            p "Eu sou apenas programada para dizer isso"

                                                            p "Mas você sim"

                                                            p "Pode levantar da cadeira agora"

                                                            p "E fazer a diferença"

                                                            p "Ou nada irá mudar..."

                                                            p "Quando você deixa de fazer algo para ajudar a todos"

                                                            p "Ou quando você utiliza materiais poluentes"

                                                            p "Você está matando todos aos poucos"

                                                            p "Até mesmo você"

                                                            p "Quem você ama"

                                                            p "Aproveite enquanto ainda dá tempo"

                                                            p "E não use a desculpa que você não vai estar aqui quando o pior acontecer"

                                                            p "Pois quem você ama, vai"

                                                            p "E toda a humanidade"

                                                            p "Que depende de você"

                                                            p "Desculpe por ser dura demais"

                                                            p "Eu carrego seu nome, mas sou apenas mais alguém tentando mudar"

                                                            p "Espero que isso ajude em algo"

                                                            call error_message('Obrigada por jogar!') from _call_error_message500

                                                            #$ copy_to_desktop('ZXUgbsOjbyBxdWVyaWEgcXVlIGZvc3NlIGFzc2lt/sssssssss.txt', minutes_folder)

                                                            #$ open_in_explorer(minutes_folder)

                                                            "O jogo será fechado, fique a vontade para tentar outras escolhas :)"

                                                            "Obrigada!"




































    "Expulsar [nomeAlegre]":
            show feliz at center:
                zoom 1.08
            with dissolve
            python:
                felizAmizade += 1
            call chamarBarraMais(felizAmizade) from _call_chamarBarraMais_2
            p "Eu não quero saber dessas suas brincadeiras idiotas"
            p "Sai do meu quarto agora"
            p "Você tem que parar com essa sua infantilidade e achar que todo mundo faz o que você manda"
            p "E é por isso que eu quero ir logo embora daqui"
            r "d-desculpe"
            r "Não vou mais te incomodar"
            show rosto triste at left:
                linear .25 zoom 1.08
            m "Que gritaria é essa aqui?"
            show rosto triste at left:
                linear .25 zoom 1.00
            show feliz at center:
                zoom 1.00
            p "A [nomeAlegre] não para de me irritar!"
            show rosto triste at left:
                linear .25 zoom 1.08
            m "O que aconteceu dessa vez?"
            show feliz at center:
                zoom 1.08
            r "Eu só queria deixar todas mais próximas, faz muito tempo que não saímos juntas..."
            r "Além disso, queria contar uma coisa para vocês..."
            show feliz at center:
                zoom 1.00
            p "Ok, ok, você venceu"
            p "Mas só porque a [nomeTriste] ta aqui."
            p "Se eu for, você para de me irritar?"
            show feliz at center:
                zoom 1.08
            r "CLAAAAAAAROOOOO que sim, prometo que nunca mais vou chegar perto do seu quarto"
            show feliz at center:
                zoom 1.00
            p "Como se isso fosse verdade..."
            show rosto triste at left:
                linear .25 zoom 1.08
            m "Vamos descer logo, as meninas já estão esperando"

            scene sala
            with dissolve

            show rosto triste at left with dissolve
            show fofa alegre at right with dissolve
            show feliz pensativa at center with dissolve

            show rosto triste at left:
                linear .25 zoom 1.08
            m "Então [nomeAlegre], o que você queria falar com a gente?"

            "[nomeTriste] é três anos mais velha. É um pouco tímida, mas sempre sabe o que dizer e conforta todas nós"

            show fofa alegre at right:
                linear .25 zoom 1.00
            show feliz alegre at center:
                linear .25 zoom 1.08
            show rosto triste at left:
                linear .25 zoom 1.08
            show rosto triste at left:
                linear .25 zoom 1.00
            r "Ah hahahahahaha daquilo, lembra?"
            show rosto triste at left:
                linear .25 zoom 1.08
            show feliz alegre at center:
                linear .25 zoom 1.00
            show fofa desconfiada at right:
                linear .25 zoom 1.00
            show rosto triste at left:
                linear .25 zoom 1.00
            t "Aquilo o que?"

            "[nomeFofa] é minha melhor amiga. Foi a primeira da casa a fazer amizade comigo."
            show feliz alegre at center:
                linear .25 zoom 1.08
            show rosto triste at left:
                linear .25 zoom 1.00
            show fofa desconfiada at right:
                linear .25 zoom 1.00
            r "Nós íamos sair..."
            show feliz alegre at center:
                linear .25 zoom 1.00
            show rosto triste at left:
                linear .25 zoom 1.08
            m "Íamos?"
            #show rosto triste at left:
            #    linear .25 zoom 1
            r "Bom, a [nomeP] já está pronta pra gente ir então vamos..."
            show feliz alegre at center:
                linear .25 zoom 1.00
            p "Eu não concordei com isso"
            show rosto triste confuso at left:
                linear .25 zoom 1.08
            m "Ahh [nomeAlegre], você fez isso de novo?"
            show rosto triste confuso at left:
                linear .25 zoom 1.00
            show feliz alegre at center:
                linear .25 zoom 1.08
            r "Mas é claro, vocês nunca saem de casa"
            show fofa alegre at right:
                linear .25 zoom 1.08
            show feliz alegre at center:
                linear .25 zoom 1.00
            t "Tudo bem, a gente pode sair dessa vez"
            show rosto triste confuso at left:
                linear .25 zoom 1.00
            t "Até porque, a [nomeP] finalmente vai com a gente!"
            show fofa alegre at right:
                linear .25 zoom 1.00
            show rosto triste at left:
                linear .25 zoom 1.08
            m "Tudo bem, eu estava pensando em sair mesmo"
            show rosto triste at left:
                linear .25 zoom 1.00
            show feliz alegre at center:
                linear .25 zoom 1.08
            r "EBAAAAAAAAAAAAAA"
            r "Parou de chover, onde vocês querem ir?"

            jump sairq



    "Lutar":
            python:
                felizAmizade += 5
            call chamarBarraMais(felizAmizade) from _call_chamarBarraMais_3

            call error_message('Não faça isso com seus amiguinhos') from _call_error_message
            call error_message('Violência nunca é a solução!') from _call_error_message_1

            p "Agora você vai ver só!"
            r "Mas [nomeApelido]..."
            p "Eu já disse que não vou sair!"
            p "Toma isso!"
            show feliz brava at center:
                linear .25 zoom 1.08
            r "Acho que você anda lendo mangás demais!"
            r "Eu só queria ser legal"
            r "Se você não queria, era só dizer!"
            show feliz brava at center:
                linear .25 zoom 1.00
            p "E adianta falar com você, [nomeAlegre]?"
            show feliz brava at center:
                linear .25 zoom 1.08
            r "Claro que sim, você sempre fica nesse quarto e não fala com ninguém"
            r "Agora quer discutir comigo, só porque eu sou uma pessoa muito mais legal, querida e divertida que você"
            p "Ahh, então isso é o que você acha de mim?"
            show rosto triste at left:
                linear .25 zoom 1.08
            m "Que gritaria é essa aqui?"
            show rosto triste at left:
                linear .25 zoom 1.00
            show feliz at center:
                zoom 1.00
            p "A [nomeAlegre] não para de me irritar!"
            show rosto triste at left:
                linear .25 zoom 1.08
            m "O que aconteceu dessa vez?"
            show feliz at center:
                zoom 1.08
            r "Eu só queria deixar todas mais próximas, faz muito tempo que não saímos juntas..."
            r "Além disso, queria contar uma coisa para vocês..."
            show feliz at center:
                zoom 1.00
            p "Ok, ok, você venceu"
            p "Mas só porque a [nomeTriste] ta aqui."
            p "Se eu for, você para de me irritar?"
            show feliz at center:
                zoom 1.08
            r "CLAAAAAAAROOOOO que sim, prometo que nunca mais vou chegar perto do seu quarto"
            show feliz at center:
                zoom 1.00
            p "Como se isso fosse verdade..."
            show rosto triste at left:
                linear .25 zoom 1.08
            m "Vamos descer logo, as meninas já estão esperando"

            scene sala
            with dissolve

            show rosto triste at left with dissolve
            show fofa alegre at right with dissolve
            show feliz pensativa at center with dissolve

            show rosto triste at left:
                linear .25 zoom 1.08
            m "Então [nomeAlegre], o que você queria falar com a gente?"

            "[nomeTriste] é três anos mais velha. É um pouco tímida, mas sempre sabe o que dizer e conforta todas nós"

            show fofa alegre at right:
                linear .25 zoom 1.00
            show feliz alegre at center:
                linear .25 zoom 1.08
            show rosto triste at left:
                linear .25 zoom 1.08
            show rosto triste at left:
                linear .25 zoom 1.00
            r "Ah hahahahahaha daquilo, lembra?"
            show rosto triste at left:
                linear .25 zoom 1.08
            show feliz alegre at center:
                linear .25 zoom 1.00
            show fofa desconfiada at right:
                linear .25 zoom 1.00
            show rosto triste at left:
                linear .25 zoom 1.00
            t "Aquilo o que?"

            "[nomeFofa] é minha melhor amiga. Foi a primeira da casa a fazer amizade comigo."
            show feliz alegre at center:
                linear .25 zoom 1.08
            show rosto triste at left:
                linear .25 zoom 1.00
            show fofa desconfiada at right:
                linear .25 zoom 1.00
            r "Nós íamos sair..."
            show feliz alegre at center:
                linear .25 zoom 1.00
            show rosto triste at left:
                linear .25 zoom 1.08
            m "Íamos?"
            #show rosto triste at left:
            #    linear .25 zoom 1
            r "Bom, a [nomeP] já está pronta pra gente ir então vamos..."
            show feliz alegre at center:
                linear .25 zoom 1.00
            show rosto triste at left:
                linear .25 zoom 1.00
            p "Eu não concordei com isso"
            show rosto triste confuso at left:
                linear .25 zoom 1.08
            m "Ahh [nomeAlegre], você fez isso de novo?"
            show rosto triste confuso at left:
                linear .25 zoom 1.00
            show feliz alegre at center:
                linear .25 zoom 1.08
            r "Mas é claro, vocês nunca saem de casa"
            show fofa alegre at right:
                linear .25 zoom 1.08
            show feliz alegre at center:
                linear .25 zoom 1.00
            t "Tudo bem, a gente pode sair dessa vez"
            show rosto triste confuso at left:
                linear .25 zoom 1.00
            t "Até porque, a [nomeP] finalmente vai com a gente!"
            show fofa alegre at right:
                linear .25 zoom 1.00
            show rosto triste at left:
                linear .25 zoom 1.08
            m "Tudo bem, eu estava pensando em sair mesmo"
            show rosto triste at left:
                linear .25 zoom 1.00
            show feliz alegre at center:
                linear .25 zoom 1.08
            r "EBAAAAAAAAAAAAAA"
            r "Parou de chover, onde vocês querem ir?"

            jump sairq




    "Tentar resistir a cócegas":
                "*para parar [nomeAlegre], você deve marcar 100 pontos, pressionando rapidamente as teclas D, J, K e L alternadamente (pressionar a mesma tecla dá cada vez menos e menos pontos)*"
                $ time = 1
                $ timerjump = "balbes"
                $ my_timer = 5
                show screen my_scr
                label loop_one:
                    $ res = ui.interact()
                    if res == "loser":
                        hide screen my_scr
                        $ renpy.pause(0.1, hard=True)
                        p "HAHAHAHAHAAH [nomeAlegre] EU NÃO AGUENTO MAIS, PARA POR FAVOR"
                        $ score = 0
                        jump fight

                    if res not in u"djkl":
                        $ renpy.pause(0.1, hard=True)
                        jump loop_one

                    hide text
                    show text("[res]") at my_transform

                    if res == prev_hit:
                        $ counter += 1
                    else:
                        $ prev_hit = res
                        $ counter = 0

                    if counter < 3:
                        $ score += (3 - counter)
                    $ renpy.pause(0.1, hard=True)

                    if score > 99:
                        hide screen my_scr
                        $ renpy.pause(0.1, hard=True)
                        $ renpy.pause(0.0, hard=True)
                        $ renpy.pause(0.0, hard=True)
                        jump far_away

                    jump loop_one

                    label far_away:
                    hide screen battletime
                    hide screen timeout_event2
                    p "HAHAHAHAHA hahaha ha"
                    p "Isso não teve graça"
                    r "Ah, você até que gostou disso, vai!"
                    show feliz alegre at center:
                        linear .25 zoom 1.08

                    r "Você vai sair com a gente ou não?"
                    menu sair:
                        "Vamos!":
                            p "Vamos logo, antes que eu mude de ideia"

                        "Não vou não!":
                            p "ME DEIXA DORMIIIIIIIIIIIIIIIIR!"
                            r "VOCÊ VAI SIM!"
                            r "Eu deixo você escolher um lugar..."


                            jump sairq


                    scene sala
                    with dissolve

                    show rosto triste at left with dissolve
                    show fofa alegre at right with dissolve
                    show feliz pensativa at center with dissolve

                    show rosto triste at left:
                        linear .25 zoom 1.08
                    m "Então [nomeAlegre], o que você queria falar com a gente?"
                    show rosto triste at left:
                        linear .25 zoom 1.00
                    show feliz alegre at center:
                        linear .25 zoom 1.08
                    r "Ah hahahahahaha daquilo, lembra?"
                    show rosto triste at left:
                        linear .25 zoom 1.00
                    show feliz alegre at center:
                        linear .25 zoom 1.00
                    show fofa desconfiada at right:
                        linear .25 zoom 1.08
                    t "Aquilo o que?"
                    show feliz alegre at center:
                        linear .25 zoom 1.08
                    show rosto triste at left:
                        linear .25 zoom 1.00
                    show fofa desconfiada at right:
                        linear .25 zoom 1.00
                    r "Nós íamos sair, lembra?"

                    #show rosto triste at left:
                    #    linear .25 zoom 1
                    r "Bom, a [nomeP] já está pronta pra gente sair então vamos..."
                    show feliz alegre at center:
                        linear .25 zoom 1.00
                    p "Eu não concordei com isso"
                    show rosto triste at left:
                        linear .25 zoom 1.08
                    m "Ahh [nomeAlegre], você fez isso de novo?"
                    show rosto triste at left:
                        linear .25 zoom 1.00
                    show feliz alegre at center:
                        linear .25 zoom 1.08
                    r "Mas é claro, vocês nunca saem de casa"
                    show fofa alegre at right:
                        linear .25 zoom 1.08
                    t "Tudo bem, a gente pode sair dessa vez"
                    t "Até porque, a [nomeP] finalmente vai ir com a gente!"
                    show fofa alegre at right:
                        linear .25 zoom 1.00
                    show rosto triste at left:
                        linear .25 zoom 1.08
                    m "Tudo bem, eu estava pensando em sair mesmo"
                    show rosto triste at left:
                        linear .25 zoom 1.00
                    show feliz alegre at center:
                        linear .25 zoom 1.08
                    r "EBAAAAAAAAAAAAAA"
                    r "Parou de chover, onde vocês querem ir?"
                    jump sairq



        #python:
        #    felizAmizade += 5
        #call chamarBarraMais(felizAmizade) from _call_chamarBarraMais_1
        #show feliz at center:
        #    zoom 1.25
        #with dissolve

    #p "Desculpa, não estou bem"
    #p "Vou ficar aqui mais um pouco"
    #p "Depois vou descer para falar com vocês..."
    #r "Oh, eu entendo"
    #r "Vou ficar em casa então..."
    #r "Se precisar de algo, é só me chamar"


return

label chamarBarraMais(valorBarra):
$pontoAnterior = valorBarra
while contador < valorBarra:
    $contador += 1
    show screen barraAmizade(contador)
    pause 0.001
$renpy.pause(2)
hide screen barraAmizade
return

label chamarBarraMenos(valorBarra):
if valorBarra > 100:
    $valorBarra = 100
if(valorBarra < pontoAnterior):
    $contador = pontoAnterior
    while contador > valorBarra:
        $contador -= 1
        show screen barraAmizade(contador)
        pause 0.001
    $renpy.pause(1)
    hide screen barraPontos

elif(valorBarra > pontoAnterior):
    $contador = pontoAnterior
    while contador < valorBarra:
        $contador += 1
        show screen barraAmizade(contador)
        pause 0.001
    $renpy.pause(2)
    hide screen barraPontos
return

screen barraAmizade(amizade):
        frame:
            hbox:
                spacing 20
                vbox:
                    spacing 10
                    text "Amizade"

                    $ ui.vbar(100, amizade, xmaximum=5, ymaximum=200, top_bar=Frame("gui/bar/top.png", 25, 25), bottom_bar=Frame("gui/bar/bottom.png", 25, 25), xalign=0.5, yalign=0.5)
