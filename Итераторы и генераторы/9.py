# «Читатель файлов»: Создайте класс FileReader, который принимает путь к текстовому файлу.
# Реализуйте метод-генератор read_lines(),
# который поочередно выдает строки файла, очищенные от пробелов по краям.

class FileReader:
    def read_lines(self, filepath: str):
        with open(filepath, 'r', encoding = 'UTF-8') as file:
            for line in file:
                yield line.strip()

object1 = FileReader()
for line in object1.read_lines('file1.txt'):
    print(line)