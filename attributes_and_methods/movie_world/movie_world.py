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
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        filtered_customer = [c for c in self.customers if c.id == customer_id][0]
        filtered_dvd = [d for d in self.dvds if d.id == dvd_id][0]
        if filtered_dvd in filtered_customer.rented_dvds:
            return f"{filtered_customer.name} has already rented {filtered_dvd.name}"
        elif filtered_dvd.is_rented:
            return "DVD is already rented"
        if filtered_customer.age < filtered_dvd.age_restriction:
            return f"{filtered_customer.name} should be at least {filtered_dvd.age_restriction} to rent this movie"
        else:
            filtered_dvd.is_rented = True
            filtered_customer.rented_dvds.append(filtered_dvd)
            return f"{filtered_customer.name} has successfully rented {filtered_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        filtered_customer = [c for c in self.customers if c.id == customer_id][0]
        filtered_dvd = [d for d in self.dvds if d.id == dvd_id][0]
        if filtered_dvd in filtered_customer.rented_dvds:
            filtered_customer.rented_dvds.remove(filtered_dvd)
            filtered_dvd.is_rented = False
            return f"{filtered_customer.name} has successfully returned {filtered_dvd.name}"
        return f"{filtered_customer.name} does not have that DVD"

    def __repr__(self):
        res = '\n'.join([c.__repr__()for c in self.customers])+'\n'
        res += '\n'.join([d.__repr__()for d in self.dvds])
        return res




