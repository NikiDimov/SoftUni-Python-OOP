class EncryptionGenerator:
    def __init__(self, text):
        self.text = text

    def __add__(self, other):
        if not isinstance(other, int):
            raise ValueError("You must add a number.")
        result = ''
        for el in self.text:
            checker = ord(el) + other
            while checker < 32:
                checker += 95
            while checker > 126:
                checker -= 95
            result += chr(checker)
        return result


some_text = EncryptionGenerator("I Love Python!")
print(some_text + 1)
print(some_text + (-1))

example = EncryptionGenerator("Super-Secret Message")
print(example + 20)
print(example + (-52))
