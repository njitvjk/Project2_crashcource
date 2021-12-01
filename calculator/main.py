import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + '/' + filename
            new_dest = folder_destination + '/' + filename
            os.rename(src, new_dest)


folder_to_track = 'C:/Users/thiya/PycharmProjects/Project2_crashcource/input'
folder_destination = 'C:/Users/thiya/PycharmProjects/Project2_crashcource/done'
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
