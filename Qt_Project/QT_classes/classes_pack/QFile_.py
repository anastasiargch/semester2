from PyQt6.QtCore import QFile, QIODevice

# Создание объекта QFile для чтения
file = QFile("example.txt")

# Открытие файла в режиме чтения
if not file.open(QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text):
    print("Не удалось открыть файл для чтения")
else:
    # Чтение содержимого файла
    text = file.readAll().data().decode()
    print("Содержимое файла:")
    print(text)
    file.close()

# Создание объекта QFile для записи
file = QFile("example_write.txt")

# Открытие файла в режиме записи
if not file.open(QIODevice.OpenModeFlag.WriteOnly | QIODevice.OpenModeFlag.Text):
    print("Не удалось открыть файл для записи")
else:
    # Запись данных в файл
    text = "Hello, QFile!"
    file.write(text.encode())
    file.close()
    print("Данные записаны в файл")




'''
Открытие файла:

QFile.open(mode): Открывает файл в указанном режиме. mode задается с использованием флагов QFile.OpenModeFlag (например, ReadOnly, WriteOnly, ReadWrite).
Чтение файла:

QFile.read(size): Читает size байт из файла. Если size не указан, читается весь файл.
QFile.readAll(): Читает весь файл и возвращает его содержимое.
Запись в файл:

QFile.write(data): Записывает data в файл. data должно быть типа bytes или bytearray.
Закрытие файла:

QFile.close(): Закрывает файл.
Проверка состояния файла:

QFile.exists(): Проверяет, существует ли файл.
QFile.remove(): Удаляет файл.
'''