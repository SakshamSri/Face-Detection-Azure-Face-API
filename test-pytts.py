import os

person = {}
person['name'] = 'Saksham Srivastava'
os.system('espeak "Hello {}" --stdout|aplay'.format(person['name']))