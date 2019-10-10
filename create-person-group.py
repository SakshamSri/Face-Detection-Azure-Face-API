import cognitive_face as cf
import credentials


cf.BaseUrl.set(credentials.face_api_base_url)
cf.Key.set(credentials.face_api_key)

cf.person_group.create(credentials.face_api_person_group_id, 'IOT-GARAGE-FRESH')