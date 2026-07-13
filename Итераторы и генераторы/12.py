# «Словорубка»: Реализуйте класс SentenceSplitter, принимающий строку-предложение.
# Метод-генератор должен выдавать слова из этого предложения по одному.

class SentenceSplitter:
    def __init__(self, sentence):
        self.sentence = sentence

    def gen_word_from_sentence(self):
        for i in self.sentence.split():
            yield i.strip()

object1 = SentenceSplitter(' Как у тебя дела?\n')
for word in object1.gen_word_from_sentence():
    print(word)
