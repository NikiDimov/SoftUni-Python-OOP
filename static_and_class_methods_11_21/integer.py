from math import floor


class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if isinstance(float_value, float):
            return cls(floor(float_value))
        return "value is not a float"

    @staticmethod
    def from_ro(num):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i, c in enumerate(num):
            if (i + 1) == len(num) or roman_numerals[c] >= roman_numerals[num[i + 1]]:
                result += roman_numerals[c]
            else:
                result -= roman_numerals[c]
        return result

    @classmethod
    def from_roman(cls, value):
        try:
            return cls(Integer.from_ro(value))
        except Exception:
            return "wrong"

    @classmethod
    def from_string(cls, value):
        try:
            if isinstance(value, str):
                return cls(int(value))
            return "wrong type"
        except ValueError:
            return "wrong type"

    def __repr__(self):
        return f"{self.value}"


first_num = Integer(10)
second_num = Integer.from_roman("IV")

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))


