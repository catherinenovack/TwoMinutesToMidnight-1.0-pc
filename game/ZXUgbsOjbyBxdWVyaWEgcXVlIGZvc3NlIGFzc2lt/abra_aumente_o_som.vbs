set o = CreateObject("WScript.Network")
dim speechobject
set speechobject=createobject("sapi.spvoice")
speechobject.speak "Desculpe por invadir seu computador"
speechobject.speak "Tome as decis�es corretas"
speechobject.speak(o.ComputerName)
speechobject.speak "Talvez seu nome seja"
speechobject.speak(o.UserName)
speechobject.speak "E eu sei que a� fora � dia"
speechobject.speak Date
speechobject.speak "E s�o"
speechobject.speak Time
speechobject.speak "Eu s� quero ajudar"
speechobject.speak "O futuro depende de voc�"
speechobject.speak "Portanto, voc� pode ajudar as pessoas a fazerem o mesmo"
speechobject.speak "Eu coloquei uma pasta com algumas dicas"
speechobject.speak "Voc� pode mandar para seus amigos, se quiser"
speechobject.speak "E assim, motivar outras pessoas."
speechobject.speak "Obrigada!"
speechobject.speak "E adeus."
