def squares(num):
    for i in range(1, num + 1):
        result = i ** 2
        yield result


print(list(squares(5)))
