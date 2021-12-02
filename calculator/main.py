"""Watchdog module"""
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    """Class implements watch dog to watch a folder and move the input file to another folder"""

    def on_modified(self, event):
        for filename in os.listdir(FOLDER_TO_TRACK):
            src = FOLDER_TO_TRACK + '/' + filename
            new_dest = FOLDER_DESTINATION + '/' + filename
            os.rename(src, new_dest)


FOLDER_TO_TRACK = 'input'
FOLDER_DESTINATION = 'done'
observer = Observer()
event_handler = Handler()
observer.schedule(event_handler, FOLDER_TO_TRACK)
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
