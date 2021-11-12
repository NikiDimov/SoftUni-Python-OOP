def solution():
    def integers():
        a = 1
        while True:
            yield a
            a += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        for i in seq:
            if len(result) == n:
                return result
            result.append(i)

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
integers = solution()[2]
print(take(5, halves()))
