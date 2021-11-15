import time


def exec_time(func):
    def wrapper(*args):
        start_point = time.time()
        func(*args)
        end_time = time.time()
        return end_time - start_point

    return wrapper


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


print(concatenate(["a" for i in range(1000000)]))
