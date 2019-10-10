import credentials
import cognitive_face as cf


cf.BaseUrl.set(credentials.face_api_base_url)
cf.Key.set(credentials.face_api_key)

response = cf.face.detect('/home/pi/images/test/rgnmx.jpeg')

#print (response)

face_ids = [d['faceId'] for d in response]

#print (face_ids)

identified_faces = cf.face.identify(face_ids, credentials.face_api_person_group_id)
print (identified_faces)

person_lists = cf.person.lists(credentials.face_api_person_group_id)

#print ('\n\n')
#print (type(response))
#print (type(identified_faces))

identified_persons = []

for face in identified_faces:
    temp_list = face['candidates']
    for content in temp_list:
        identified_persons.append(content['personId'])

#print (identified_persons)

print ('\n\n')

for person in person_lists:
    if person['personId'] in identified_persons:
        print (person['name'])