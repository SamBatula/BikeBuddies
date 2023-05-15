from gtts import gTTS
from playsound import playsound

mytext = 'Person detected.'

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("demo.mp3")

playsound('demo.mp3')
