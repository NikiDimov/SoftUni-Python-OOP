class vowels:
    V = ["A", "E", "I", "O", "U", "Y"]

    def __init__(self, string):
        self.string = list(string)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.string):
            raise StopIteration
        char = self.string[self.index]
        self.index += 1
        if char.upper() in vowels.V:
            return char
        return self.__next__()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
