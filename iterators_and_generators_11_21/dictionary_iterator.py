from collections import deque


class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = deque(dictionary.items())

    def __iter__(self):
        return self

    def __next__(self):
        if self.dictionary:
            return self.dictionary.popleft()
        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
