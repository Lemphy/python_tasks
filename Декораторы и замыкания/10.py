# Последние три сообщения (История)
# Напиши функцию history_buffer(). Возвращаемая функция должна принимать строку (новое сообщение),
# добавлять его в список внутри замыкания и возвращать список,
# содержащий не более 3-х последних добавленных сообщений (более старые должны удаляться).

def history_buffer(total: int):
    messages = []
    def temp(message: str) -> list[str]:
        if len(messages) >= total:
            del messages[0]
            messages.append(message)
            return messages
        else:
            messages.append(message)
            return messages
    return temp

func = history_buffer(3)
for _ in range(8):
    print(func(input('String: ')))
