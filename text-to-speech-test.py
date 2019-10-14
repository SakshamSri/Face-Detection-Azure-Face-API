from gtts import gTTS
import os

myText = 'Text to Speech for IOT Garage'
language = 'en'

output = gTTS(text=myText, lang=language, slow=False)

output.save('test.mp3')

os.system('mpg123 -vC test.mp3')