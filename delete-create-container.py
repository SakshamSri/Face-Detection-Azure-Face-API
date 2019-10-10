import time
import credentials
import uploaderHelperFunctions as UHF

blob_service = UHF.BlockBlobService(credentials.storage_account_name,
                                    credentials.storage_account_key)

blob_service.delete_container(credentials.storage_container_name)
time.sleep(50)
blob_service.create_container(credentials.storage_container_name)


