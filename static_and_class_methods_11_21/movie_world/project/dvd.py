class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @staticmethod
    def get_month(month):
        if month == "1" or month == "01":
            return "January"
        elif month == "2" or month == "02":
            return "February"
        elif month == "3" or month == "03":
            return "March"
        elif month == "4" or month == "04":
            return "April"
        elif month == "5" or month == "05":
            return "May"
        elif month == "6" or month == "06":
            return "June"
        elif month == "7" or month == "07":
            return "July"
        elif month == "8" or month == "08":
            return "August"
        elif month == "9" or month == "09":
            return "September"
        elif month == "10":
            return "October"
        elif month == "11":
            return "November"
        elif month == "12":
            return "December"

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        day, month, year = date.split(".")
        year = int(year)
        month = DVD.get_month(month)
        return cls(name, id, year, month, age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has" \
               f" age restriction {self.age_restriction}. " \
               f"Status: {'rented' if self.is_rented else 'not rented'}"


