import credentials
import cognitive_face as cf


cf.BaseUrl.set(credentials.face_api_base_url)
cf.Key.set(credentials.face_api_key)

print(cf.person.lists(credentials.face_api_person_group_id))