import os 
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

#Source
source_dir = "/Users/melim/Downloads"

#Using this library, print the name
with os.scandir(source_dir) as entries:
    for entry in entries: 
        print(entry.name)

#MoverHandler

class event:
    def __init__(self) -> None:
        pass

#Initiates watchdog
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = event()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()