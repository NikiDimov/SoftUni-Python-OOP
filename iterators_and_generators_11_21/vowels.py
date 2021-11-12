from collections import deque


class vowels:
    def __init__(self, text: str):
        self.text = vowels.checker(text)

    @staticmethod
    def checker(text):
        return deque(el for el in list(text) if el.lower() in "aeiouy")

    def __iter__(self):
        return self

    def __next__(self):
        if self.text:
            return self.text.popleft()
        raise StopIteration


my_string = vowels("Abcedifuty0o")
for char in my_string:
    print(char)
