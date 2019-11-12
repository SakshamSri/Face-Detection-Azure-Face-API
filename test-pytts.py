import os
from gtts import gTTS

myText = 'Welcome to IOT Garage Mister Raghuu Raam Jooshii'
language = 'en'
output = gTTS(text=myText, lang=language, slow=False)
output.save('person.mp3')
os.system('mpg321 -vC /home/pi/Face-Detection-Azure-Face-API/person.mp3')