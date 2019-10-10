from azure.storage.blob import BlockBlobService
import credentials

blob_service = BlockBlobService(credentials.storage_account_name, credentials.storage_account_key)

print("\nList blobs in the container")
generator = blob_service.list_blobs(credentials.storage_container_name)
print (type(generator))
lst = list(generator)
print (type(lst))
print (lst[-1].name)
print (lst[-1].properties.last_modified)

'''
for blob in generator:
    print("\t Blob name: " + blob.name)
'''