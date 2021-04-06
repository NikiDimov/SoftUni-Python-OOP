class dictionary_iter:
    def __init__(self, my_dict):
        self.my_dict = my_dict
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == len(self.my_dict):
            raise StopIteration
        keys = list(self.my_dict)
        tup = (keys[self.counter], self.my_dict[keys[self.counter]])
        self.counter += 1
        return tup


result = dictionary_iter({2: "2", 3: "3", 4: "4"})
for x in result:
    print(x)
