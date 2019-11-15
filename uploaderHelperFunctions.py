import datetime
import requests
import cognitive_face as cf
import credentials
import os

'''
#connection function
def BlockStorageConnection(storage_account_name, storage_account_key):

    return BlockBlobService(storage_account_name, storage_account_key)
'''
'''
#Uploader function
def uploadfile(block_blob_service,
               storage_container_name,
               filename,
               local_file_name,
               file_content_type):

    print ("\n*****UPLOADING FILE*****")
    print (local_file_name)
    print ('\n')

    #uploading file
    block_blob_service.retry = no_retry

    block_blob_service.create_blob_from_path(storage_container_name,
                                filename,
                                local_file_name,
                                content_settings=ContentSettings(
                                        content_type=file_content_type),
                                if_none_match='*',
                                timeout='30'
                              )
    print ("\n*****FILE UPLOADED*****")
#uploader function end
'''

def getTimeForFile():

    return datetime.datetime.now().strftime('%B %d, %Y %H:%M:%S.%f')


def checkNetwork():

    try:
        response = requests.get("http://www.google.com")
        print (("\nRESPONSE CODE: " + str(response.status_code)))
        return True
    except requests.ConnectionError:
        print ("\nCOULD NOT CONNECT. ERROR IN CHECKNETWORK()...")
        return False


def testImage(src_path):
    print('first line testImage()')
    if not checkNetwork():
        return

    cf.BaseUrl.set(credentials.face_api_base_url)

    cf.Key.set(credentials.face_api_key)

    # generator = get_list_blobs(blob_service, credentials.storage_container_name)

    # lst = list(generator)
    '''
    get_blob_from_storage(blob_service,
        credentials.storage_container_name,
        lst,
        credentials.face_api_downloaded_blob_loc)
    '''
    print(datetime.datetime.now())
    response = detect(src_path)

    face_ids = [d['faceId'] for d in response]
    if len(face_ids)==0:
        # os.system('espeak "No Face Detected " --stdout|aplay')
        print('deleting...')            
        delete_file(src_path)
        return
    print('Face IDS:\n')
    print(face_ids)
    print('\n')
    
    identified_faces = cf.face.identify(face_ids, credentials.face_api_person_group_id)
    print('Identified Faces:\n')
    print(identified_faces)
    print('\n')
    if identified_faces is not None:
        person_lists = get_person_lists(credentials.face_api_person_group_id)

        identified_persons = []

        for face in identified_faces:
            temp_list = face['candidates']
            for content in temp_list:
                identified_persons.append(content['personId'])

        print ('\n\n')
        
        if len(identified_persons)==0:
            os.system('espeak "Sorry. I do not know you. Please register yourself first. " --stdout|aplay')
            # last_person = []
            print('deleting...')            
            delete_file(src_path)
            return
        
        known_list = []
        
        for person in person_lists:
            if person['personId'] in identified_persons:
                print ((person['name']))
                print(datetime.datetime.now())
                known_list.append(person['name'])                
                '''
                current_person = current_person + person['name'] + " "
                if last_time == "" and last_person == "":
                    last_person = last_person + person['name'] + " "
                    last_time = datetime.datetime.now()
                # last_person = person['name']
                if last_person == current_person AND:
                '''
                
                '''
                myText = 'Welcome to IOT Garage Mister' + person['name']
                language = 'en'
                output = gTTS(text=myText, lang=language, slow=False)
                output.save('person.mp3')
                os.system('mpg123 -vC person.mp3')
                '''
        '''
        current_time = datetime.datetime.now()
        
        flag = False
        if len(last_person)==0:
            last_person = known_list.copy()
            last_time = current_time
            for person in known_list:
                os.system('espeak "Hello {}." --stdout|aplay'.format(person))
            os.system('espeak "Welcome to I.O.T Garage." --stdout|aplay')
            return last_person, last_time
        
        print('before known list copy')
        known_list_copy = known_list.copy()
        known_list_copy.sort()
        last_person.sort()
        
        print('before compare lists')
        if known_list_copy != last_person:
            flag = True
        print('before computing current time')
        
        print('after computing current')
        diff = (current_time - last_time)
        diff1 = diff.total_seconds()
        print('after computing diff')
        '''
        #if flag == True :
        for person in known_list:
            os.system('espeak "Hello {}." --stdout|aplay'.format(person))
        os.system('espeak "Welcome to I.O.T Garage." --stdout|aplay')
        '''
        else:
            last_person = known_list.copy()
            last_time = current_time
            
                # print(datetime.datetime.now())
        '''
        '''
        if len(face_ids)>len(identified_persons):
            diff = len(face_ids)-len(identified_persons)
            if diff==1:
                os.system('espeak "Sorry. There is {} person I do not know." --stdout|aplay'.format(str(diff)))
            else:
                os.system('espeak "Sorry. There are {} people I do not know." --stdout|aplay'.format(str(diff)))
        ''' 
                
    print('deleting...')            
    delete_file(src_path)
    
    return

'''
def get_list_blobs(blob_service, storage_container_name):

    try:
        generator = blob_service.list_blobs(storage_container_name)
        return generator
    except:
        print ('\nERROR IN RETRIEVING LIST OF BLOBS...')
'''

def identify(face_ids, face_api_person_group_id):

    try:
        identified_faces = cf.face.identify(face_ids, face_api_person_group_id)
        return identified_faces
    except:
        print ('\nNO ONE IDENTIFIED...')
        return None


def detect(src_path):

    try:
        response = cf.face.detect(src_path)
        return response
    except:
        print ('\nERROR IN DETECTING IMAGE...(RESPONSE)...')


def get_person_lists(face_api_person_group_id):

    try:
        person_lists = cf.person.lists(face_api_person_group_id)
        return person_lists
    except:
        print ('\nERROR IN RETRIEVING PERSONS\' LISTS...')

'''
def get_blob_from_storage(blob_service,
    storage_container_name,
    lst,
    downloaded_blob_loc):

    try:
        blob_service.get_blob_to_path(storage_container_name,
            lst[-1].name,
            downloaded_blob_loc + lst[-1].name)
    except:
        print ('\nERROR IN RETRIEVING BLOB FROM STORAGE...')
'''

def delete_file(file_path):

    try:
        os.remove(file_path)
        print ('\nDELETED...')
    except:
        print ('\nERROR IN DELETING FILE...')