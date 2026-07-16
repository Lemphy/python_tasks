# Светофор (Переключатель состояний)
# Создай функцию traffic_light(). Возвращаемая функция при каждом вызове должна переключать состояние
# светофора по кругу: "Red" -> "Yellow" -> "Green" -> "Red".
# При первом вызове должен возвращаться "Red".

def traffic_light():
    colors = ['Red', 'Yellow', 'Green', 'Blue', 'Pink']
    index = 0
    def temp():
        nonlocal index
        if index < len(colors):
            current_index = index
            index += 1
            return colors[current_index]
        else:
            current_index = 0
            index = 1
            return colors[current_index]
    return temp

func = traffic_light()
for i in range(10):
    print(func())