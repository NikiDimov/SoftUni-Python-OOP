def cache(func):
    def wrapper(n):
        result = func(n)
        wrapper.log[n] = result
        return result
    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(10)
print(fibonacci.log)



