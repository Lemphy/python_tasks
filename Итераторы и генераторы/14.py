# «Студенческая база»: Напишите класс University. В нем хранится список студентов
# (у каждого есть имя и средний балл). Реализуйте метод-генератор honors_students(),
# который возвращает только отличников (балл > 4.5).

class University:
    def __init__(self, students: dict[str, float | int]):
        self.students = students

    def honors_students(self, score = 4.5):
        for k, v in self.students.items():
            if v >= score:
                yield k,v

obj = University({'Сергей': 5.4, 'Стас': 5, 'Антон': 3.5, 'Алексей':8, 'Михаил': 10.2})
for student, score in obj.honors_students():
    print(f'Студент - {student}, средний балл - {score}')