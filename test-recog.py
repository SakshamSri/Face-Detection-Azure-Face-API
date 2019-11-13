import speech_recognition as sr
import testcv2 as tcv
import os
import time
import subprocess

#from os import path
#AUDIO_FILE = os.path.abspath('test.wav')
#command = "sudo arecord -D plughw:1,0 test.wav"
while True:
    r = sr.Recognizer()
    
    '''
    print('before subprocess call')
    process = subprocess.Popen(command.split(), shell=True)
    print('after subprocess call')
    time.sleep(5)
    process.kill()
    '''
    
    m = sr.Microphone()
    
    
    with m as source:
        print('Say Something')
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
    
    
    '''
    with m as source:
        print('Say Something')
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
        
    with open('raw-audio.wav', 'wb') as f:
        f.write(audio.get_wav_data())
    '''
    
    #break

    '''
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)    
    '''
    
    '''
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Couldn't understand")
    except sr.RequestError as e:
        print("Error {0}".format(e))
    '''
    
    try:
        res = r.recognize_google(audio, language='en-IN')
        print(res)
    except sr.UnknownValueError:
        print("Couldn't understand")
    except sr.RequestError as e:
        print("Error {0}".format(e))
        # print("Google thinks you said " + )
    res = "Hello"
    if res == "Hello":
        #os.system("su")
        tcv.run_video_capture()
