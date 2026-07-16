# Динамический средний балл
# Создай функцию grade_tracker(). Возвращаемая функция принимает оценку (число от 1 до 5).
# Если оценка некорректна, она её игнорирует. Функция должна возвращать текущий средний
# балл ученика на основе всех корректно введенных оценок.

def grade_tracker():
    scores = []
    def get_avg_score(score):
        if 1 <= score <= 5:
            scores.append(score)
            return sum(scores) / len(scores)
        else:
            return sum(scores) / len(scores)
    return get_avg_score

func = grade_tracker()
for i in range(10):
    print(func(int(input('Value: '))))