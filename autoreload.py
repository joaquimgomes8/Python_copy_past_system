# autoreload.py

import subprocess
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Monitor(FileSystemEventHandler):

    def __init__(self):
        self.processo = None
        self.iniciar()

    def iniciar(self):
        print("Iniciando aplicação...")
        self.processo = subprocess.Popen([sys.executable, "app.py"])

    def reiniciar(self):
        print("Alteração detectada! Reiniciando...")

        self.processo.terminate()
        self.processo.wait()

        time.sleep(0.5)

        self.iniciar()

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            self.reiniciar()


monitor = Monitor()

observer = Observer()
observer.schedule(monitor, ".", recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()

observer.join()