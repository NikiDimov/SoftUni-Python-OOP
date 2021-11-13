def fibonacci():
    result = [0, 1]
    for el in result:
        yield el
        result.append(result[-1] + result[-2])


generator = fibonacci()
for i in range(5):
    print(next(generator))
