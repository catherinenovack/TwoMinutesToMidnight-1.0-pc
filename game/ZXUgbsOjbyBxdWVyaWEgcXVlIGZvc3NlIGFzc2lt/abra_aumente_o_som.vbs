set o = CreateObject("WScript.Network")
dim speechobject
set speechobject=createobject("sapi.spvoice")
speechobject.speak "Desculpe por invadir seu computador"
speechobject.speak "Tome as decisões corretas"
speechobject.speak(o.ComputerName)
speechobject.speak "Talvez seu nome seja"
speechobject.speak(o.UserName)
speechobject.speak "E eu sei que aí fora é dia"
speechobject.speak Date
speechobject.speak "E são"
speechobject.speak Time
speechobject.speak "Eu só quero ajudar"
speechobject.speak "O futuro depende de você"
speechobject.speak "Portanto, você pode ajudar as pessoas a fazerem o mesmo"
speechobject.speak "Eu coloquei uma pasta com algumas dicas"
speechobject.speak "Você pode mandar para seus amigos, se quiser"
speechobject.speak "E assim, motivar outras pessoas."
speechobject.speak "Obrigada!"
speechobject.speak "E adeus."
