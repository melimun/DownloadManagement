from fileinput import filename
import os 
import sys
import shutil
import time
import logging
from os.path import splitext, exists, join
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#Sources
source_dir = "/Users/melim/Downloads"
video_dir = "/Users/melim/Videos"
image_dir = "/Users/melim/Pictures"
document_dir = "/Users/melim/Documents"
music_dir = "/Users/melim/Music"

#Using this library, print the name
with os.scandir(source_dir) as entries:
    for entry in entries: 
        print(entry.name)

#Moving Action Class
class MoveHandler(FileSystemEventHandler):
    def on_modified(self,event):
        with os.scandir(source_dir) as entries:
            #For loop of all the files in downloads
            for entry in entries:
                name = entry.name 
                source = source_dir 
                #Conditionals
                if name.endswith('.mp4') or name.endswith('.avi'):
                    source = video_dir
                    move_action(source, entry, name)
                elif name.endswith('.jpeg') or name.endswith('png') or name.endswith('.jpg'):
                    source = image_dir
                    move_action(source, entry, name)
                elif name.endswith('.pdf'):
                    source = document_dir
                    move_action(source, entry, name)
                elif name.endswith('.wav') or name.endswith('.mp3'):
                    source = music_dir
                    move_action(source, entry, name)

#makes a unique name if already exists
def make_name(destination, name):
    filename, extension = splitext(name)
    counter = 1
    #If file exists, add a number to the end of the filename
    while exists(f"{destination}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
    return name

#performs the move action
def move_action(destination, entry, name):
    #Does this file already exist?
    file_exists = os.path.exists(destination + "/" + name)
    if file_exists:
        unique_name = make_name(name)
        os.rename(entry, unique_name)
    #if it does not exist, this will run. (moves the file)
    shutil.move(entry, destination)


#Initiates watchdog
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoveHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

    