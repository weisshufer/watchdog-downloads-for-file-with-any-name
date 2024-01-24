import time
import os
import platform
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class DownloadFolderHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Получаем полное имя файла
        filename = os.path.basename(event.src_path)

        # Waiting for file with
        if "Abtretungserklärung_signiert_" in filename:
            # Выполнение команды
            print(f"Обнаружен файл: {filename}. Выполняется команда...")


# Определение пути к папке Downloads для разных операционных систем
downloads_path = ""
if platform.system() == "Windows":
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
elif platform.system() == "Darwin":  # Darwin это MacOS
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

# Создание и запуск наблюдателя
observer = Observer()
event_handler = DownloadFolderHandler()
observer.schedule(event_handler, downloads_path, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
