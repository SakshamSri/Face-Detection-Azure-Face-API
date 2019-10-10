import cognitive_face as cf
import credentials


cf.BaseUrl.set(credentials.face_api_base_url)
cf.Key.set(credentials.face_api_key)

