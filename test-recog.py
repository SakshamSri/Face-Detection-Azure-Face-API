import speech_recognition as sr
import testcv2 as tcv
# import os
import time
# import subprocess

#from os import path
#AUDIO_FILE = os.path.abspath('test.wav')
#command = "sudo arecord -D plughw:1,0 test.wav"
while True:
    res = None
    r = sr.Recognizer()
    
    '''
    print('before subprocess call')
    process = subprocess.Popen(command.split(), shell=True)
    print('after subprocess call')
    time.sleep(5)
    process.kill()
    '''
    
    m = sr.Microphone(sample_rate=48000, chunk_size=1024)
    
    
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
    
    # break

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
    print('Sending data to cloud...')
    try:
        res = r.recognize_google(audio, language='en-IN')
        print(res)
    except sr.UnknownValueError:
        print("Couldn't understand")
    except sr.RequestError as e:
        print("Error {0}".format(e))
        # print("Google thinks you said " + )
    #res = "Hello"
    # res = res.lower()
    try:
        if "garage" in res.lower():
        #os.system("su")
            os.system('espeak "Please look in the camera." --stdout|aplay')
            tcv.run_video_capture()
    except Exception as e:
        print(e)
    time.sleep(1)