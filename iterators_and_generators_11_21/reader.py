def read_next(*args):
    for el in args:
        for e in el:
            yield e


for item in read_next("string", (2,), {"d": 1, "I": 2, "c": 3, "t": 4}):
    print(item, end='')
print()
for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
