def reverse_text(string):
    for char in string[::-1]:
        yield char


for char in reverse_text("step"):
    print(char, end='')
