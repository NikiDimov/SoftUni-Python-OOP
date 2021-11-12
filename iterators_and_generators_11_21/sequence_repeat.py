from collections import deque
from math import ceil


class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence_repeat.validate_sequence(sequence, number)
        self.number = number
        self.counter = 0

    @staticmethod
    def validate_sequence(seq, num):
        return deque(seq * (ceil(num / len(seq))))

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.number:
            self.counter += 1
            return self.sequence.popleft()
        raise StopIteration


result = sequence_repeat("abc", 5)
for item in result:
    print(item, end='')

# result = sequence_repeat("I Love Python", 3)
# for item in result:
#     print(item, end='')
