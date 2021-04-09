def make_underline(function):
    def wrapper(*args):
        return "<u>" + function(*args) + "</u>"

    return wrapper


def make_italic(function):
    def wrapper(*args):
        return "<i>" + function(*args) + "</i>"

    return wrapper


def make_bold(function):
    def wrapper(*args):
        return "<b>" + function(*args) + "</b>"

    return wrapper


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))
