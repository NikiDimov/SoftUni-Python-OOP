class reverse_iter:
    def __init__(self, sequence: list):
        self.sequence = sequence

    def __iter__(self):
        return self

    def __next__(self):
        if self.sequence:
            return self.sequence.pop()
        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
