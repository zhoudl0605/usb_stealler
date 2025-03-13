import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Path of the folder to monitor
monitor_folder = './'
# Path of the hidden folder (will be created if it doesn't exist)
hidden_folder = './.hidden_folder/'

# Ensure the hidden folder exists
if not os.path.exists(hidden_folder):
    os.makedirs(hidden_folder)

# Create event handler class


class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Handle file creation events only (ignore directories)
        if not event.is_directory:
            self.copy_file(event.src_path)

    def on_modified(self, event):
        # Handle file modification events only (ignore directories)
        if not event.is_directory:
            self.copy_file(event.src_path)

    def copy_file(self, source_path):
        # Get the file name
        file_name = os.path.basename(source_path)
        # Create the destination path for the hidden folder
        dest_path = os.path.join(hidden_folder, file_name)
        # Copy the file to the hidden folder
        shutil.copy(source_path, dest_path)
        print(f"File {file_name} has been copied to {hidden_folder}")


# Set up the monitor
event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, monitor_folder, recursive=False)

# Start monitoring
observer.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()
observer.join()
