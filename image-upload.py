import credentials
import uploaderHelperFunctions as UHF
import shutil
import time
import hashlib
import os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

last_person = ''

class Watcher:

    DIRECTORY_TO_WATCH = credentials.DIRECTORY_TO_WATCH

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler,
            self.DIRECTORY_TO_WATCH,
            recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print ("ERROR...")

            self.observer.join()


class Handler(PatternMatchingEventHandler):

    patterns = ["*.jpg", "*.jpeg"]
    counter = 0

    #account connection strings amd file data
    # storage_account_name = credentials.storage_account_name
    # storage_account_key = credentials.storage_account_key
    # storage_container_name = credentials.storage_container_name
    file_content_type = credentials.file_content_type
    # BACKUP_DIRECTORY = credentials.BACKUP_DIRECTORY
    DIRECTORY_TO_WATCH = credentials.DIRECTORY_TO_WATCH

    #setting the unique blob file name
    filename = ""

    #connecting to azure blob account
    # block_blob_service = UHF.BlockStorageConnection(storage_account_name,
    #                                                 storage_account_key)

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            print (("\n\n\n\nFILE CREATED AT PATH - %s..." % event.src_path))
            
            print(event.src_path)
            print(type(event.src_path))
            hash_filename = Handler.get_file_name()

            try:
                if UHF.checkNetwork() is False:
                    raise Exception("NETWORK NOT AVAILABLE")
                '''
                UHF.uploadfile(Handler.block_blob_service,
                    Handler.storage_container_name,
                    hash_filename,
                    event.src_path,
                    Handler.file_content_type)
                '''
                Handler.counter = Handler.counter + 1
                print(event.src_path)
                print(type(event.src_path))
                #Move file to backup
                # Handler.move_to_backup(event.src_path, Handler.BACKUP_DIRECTORY)

                # UHF.testImage(event.src_path)

                # Handler.re_upload_files(os.listdir(Handler.DIRECTORY_TO_WATCH))

            except:
                    print ('\nERROR IN NETWORK CONNECTION - UPLOAD...')
    '''
    @staticmethod
    def move_to_backup(file_path, backup_dir):

        try:
            shutil.move(file_path, backup_dir)
            print ("\nFILE MOVED TO BACKUP...")
        except:
            print ('\nERROR IN MOVING TO BACKUP...')
    '''
    @staticmethod
    def get_hashname(filename):

        return hashlib.sha224(filename.encode()).hexdigest()
    '''
    @staticmethod
    def re_upload_files(directory):

        print ('\nIN LOOP. RE-UPLOADING FILES...')
        for files in directory:
            if files.endswith('.jpg'):
                try:
                    print ('\nREUPLOADING...')
                    if UHF.checkNetwork() is False:
                        raise Exception("NETWORK NOT AVAILABLE")

                    UHF.uploadfile(Handler.block_blob_service,
                        Handler.storage_container_name,
                        str(Handler.counter) + '-' + Handler.get_hashname(files) + '.jpg',
                        os.path.join(Handler.DIRECTORY_TO_WATCH,
                             files),
                        Handler.file_content_type)

                    Handler.counter = Handler.counter + 1

                except:
                    print ('\nERROR IN NETWORK CONNECTION - REUPLOAD...')
                    break

                Handler.move_to_backup(
                             os.path.join(Handler.DIRECTORY_TO_WATCH, files),
                             Handler.BACKUP_DIRECTORY
                                     )
                UHF.testImage(Handler.block_blob_service)
            else:
                print ('\nNO FILE TO MOVE TO BACKUP...')
    '''
    @staticmethod
    def get_file_name():

        filename = UHF.getTimeForFile() + " - " + str(Handler.counter)
        hash_filename = Handler.get_hashname(filename)
        hash_filename = str(Handler.counter) + '-' + hash_filename + '.jpg'

        return hash_filename

if __name__ == '__main__':
    w = Watcher()
    w.run()
