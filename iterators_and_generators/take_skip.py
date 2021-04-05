class take_skip:
    counter = 0
    count_num = 0

    def __init__(self, step, count):
        self.step = step
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.count:
            raise StopIteration
        c = self.count_num
        self.count_num += self.step
        self.counter += 1
        return c


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
