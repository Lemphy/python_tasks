# «Генератор паролей»: Создайте класс PasswordGenerator.
# Метод-генератор должен выдавать случайные пароли заданной длины.
import string
import random

class PasswordGenerator:
    symbols = string.ascii_letters + string.digits + '!?'

    def generate_password(self, length):
        while True:
            yield ''.join(random.choice(self.symbols) for _ in range(length))

object1 = PasswordGenerator()
passwords = object1.generate_password(20)
for password in passwords:
    print(password)