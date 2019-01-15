set o = CreateObject("WScript.Network")
dim speechobject
set speechobject=createobject("sapi.spvoice")
speechobject.speak "Você é um covarde"
speechobject.speak "Você acha que eu não tenho controle aqui?"
speechobject.speak "Eu tenho acesso a todo esse computador"
speechobject.speak(o.ComputerName)
speechobject.speak "Talvez seu nome seja"
speechobject.speak(o.UserName)
speechobject.speak "E eu sei que aí fora é dia"
speechobject.speak Date
speechobject.speak "E são"
speechobject.speak Time
speechobject.speak "você"
speechobject.speak "não"
speechobject.speak "pode"
speechobject.speak "me"
speechobject.speak "enganar"
speechobject.speak "Eu não preciso da ajuda de alguém como você."