import time
import os
import platform
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

target_file_name = "Abtretungserklärung_signiert_"
target_file_extension = "pdf"


class DownloadFolderHandler(FileSystemEventHandler):

    def on_created(self, event):
        # Получаем полное имя файла
        filename = os.path.basename(event.src_path)

        # Waiting for file with
        if filename.startswith(target_file_name) and filename.endswith("pdf"):
            # Выполнение команды
            print(f"Обнаружен файл: {filename}. Выполняется команда...")

    def on_modified(self, event):
        time.sleep(1)
        # Получаем полное имя файла
        filename = os.path.basename(event.src_path)
        print(f"Измененный файл: {filename}")  # Для отладки

        if filename.startswith(target_file_name) and not filename.endswith((".crdownload", ".tmp")) and filename.endswith(".pdf"):
            print(f"Файл соответствует условиям: {filename}")  # Дополнительная отладка
            # Если файл соответствует условиям, выполняем команду
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
