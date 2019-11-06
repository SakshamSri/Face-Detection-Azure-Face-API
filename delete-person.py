import credentials
import cognitive_face as cf


cf.BaseUrl.set(credentials.face_api_base_url)
cf.Key.set(credentials.face_api_key)
idp = ''
lt = cf.person.lists(credentials.face_api_person_group_id)
for per in lt:
    response = cf.person.delete(credentials.face_api_person_group_id, per['personId'])
print(lt)
# name = 'Thakur'
# name_data = "TMH2KOR"
# response = cf.person.delete(credentials.face_api_person_group_id, idp)
print (response)