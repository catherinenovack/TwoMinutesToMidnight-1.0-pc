set o = CreateObject("WScript.Network")
dim speechobject
set speechobject=createobject("sapi.spvoice")
speechobject.speak "Voc� � um covarde"
speechobject.speak "Voc� acha que eu n�o tenho controle aqui?"
speechobject.speak "Eu tenho acesso a todo esse computador"
speechobject.speak(o.ComputerName)
speechobject.speak "Talvez seu nome seja"
speechobject.speak(o.UserName)
speechobject.speak "E eu sei que a� fora � dia"
speechobject.speak Date
speechobject.speak "E s�o"
speechobject.speak Time
speechobject.speak "voc�"
speechobject.speak "n�o"
speechobject.speak "pode"
speechobject.speak "me"
speechobject.speak "enganar"
speechobject.speak "Eu n�o preciso da ajuda de algu�m como voc�."