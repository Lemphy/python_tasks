# Последние три сообщения (История)
# Напиши функцию history_buffer(). Возвращаемая функция должна принимать строку (новое сообщение),
# добавлять его в список внутри замыкания и возвращать список,
# содержащий не более 3-х последних добавленных сообщений (более старые должны удаляться).

def history_buffer(total):
    messages = [None] * total
    index = 0
    def temp(message: str) -> list[str]:
        nonlocal index
        if index < total:
            messages[index] = message
            index += 1
            return messages
        else:
            index = 0
            messages[index] = message
            index += 1
            return messages
    return temp

func = history_buffer(3)
for _ in range(10):
    print(func(input('text: ')))