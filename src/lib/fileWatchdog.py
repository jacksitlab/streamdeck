from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os.path
import re

class FileWatchdog(FileSystemEventHandler):

    def __init__(self, file_name, callback):
        self.resolvePathAndFIle(file_name)
        self.callback = callback

        # set observer to watch for changes in the directory
        self.observer = Observer()
        self.observer.schedule(self, self.path, recursive=False)
        print("start watching for "+self.file_name+" in "+self.path)
        self.observer.start()
#        self.observer.join()

    def resolvePathAndFIle(self, filename):
        regex = r"(.*)[\/]([\S^]+)$"
        match = re.findall(regex, filename, re.M|re.I)
        if len(match)>0:
            self.path = match[0][0]
            self.file_name = match[0][1]
        else:
            self.file_name = filename
            self.path = "."

    def on_modified(self, event):
        # only act on the change that we're looking for
        if not event.is_directory and event.src_path.endswith(self.file_name):
            self.observer.stop()  # stop watching
            self.callback()  # call callback

    def stop(self):
        self.observer.stop()
