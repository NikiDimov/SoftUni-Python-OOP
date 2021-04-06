class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.counter = 0
        self.char_counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.char_counter == self.number:
            raise StopIteration
        char = self.sequence[self.counter]
        self.counter += 1
        self.char_counter += 1
        if self.counter == len(self.sequence):
            self.counter = 0
        return char


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
