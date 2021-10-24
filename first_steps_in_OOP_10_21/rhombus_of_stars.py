class Rhombus:
    def __init__(self, n):
        self.n = n

    def create_rhombus(self):
        for i in range(1, self.n + 1):
            print((self.n - i) * " " + "* " * i)
        for k in range(self.n - 1, 0, -1):
            print((self.n - k) * " " + "* " * k)


r = Rhombus(int(input()))
r.create_rhombus()
