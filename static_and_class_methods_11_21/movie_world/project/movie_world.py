class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        return f"{customer.name} has already rented {dvd.name}"
                for dvd in self.dvds:
                    if dvd.id == dvd_id:
                        if dvd.is_rented:
                            return "DVD is already rented"
                        if customer.age < dvd.age_restriction:
                            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
                        customer.rented_dvds.append(dvd)
                        dvd.is_rented = True
                        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        customer.rented_dvds.remove(dvd)
                        dvd.is_rented = False
                        return f"{customer.name} has successfully returned {dvd.name}"
                return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ''
        for customer in self.customers:
            result += f"{customer}\n"
        for dvd in self.dvds:
            result += f"{dvd}\n"
        return result.strip()

