import os

person = {}
person['name'] = 'Thakur'
os.system('espeak "Hello {}" --stdout|aplay'.format(person['name']))