import credentials
import cognitive_face as cf


cf.BaseUrl.set(credentials.face_api_base_url)
cf.Key.set(credentials.face_api_key)

cf.person_group.train(credentials.face_api_person_group_id)

response = cf.person_group.get_status(credentials.face_api_person_group_id)

print (response)

status = response['status']

print (status)