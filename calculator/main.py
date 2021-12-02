import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
class Handler(FileSystemEventHandler):
    """Class implements watch dog to watch a folder and move the input file to another folder"""
    def on_modified(self,event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + '/' + filename
            new_dest = folder_destination + '/' + filename
            os.rename(src, new_dest)

folder_to_track = 'input'
folder_destination = 'done'
observer = Observer()
event_handler = Handler()
observer.schedule(event_handler, folder_to_track)
print("watchDog starts")
observer.start()
print("watchdog After the start")
try:
    while True:
        time.sleep(1)
        print("timer")
except KeyboardInterrupt:
    observer.stop()

observer.join()
