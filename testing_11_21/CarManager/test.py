from testing.CarManager.car_manager import Car
from unittest import TestCase, main


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("1997", "Jeep", 9, 50)

    def test_init(self):
        self.assertEqual("1997", self.car.make)
        self.assertEqual("Jeep", self.car.model)
        self.assertEqual(9, self.car.fuel_consumption)
        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_if_make_is_null(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_if_model_is_null(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_if_fuel_consumption_is_null(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_if_fuel_capacity_is_null(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_if_fuel_amount_is_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refueling_with_fuel_less_than_capacity(self):
        self.car.refuel(49)
        self.assertEqual(49, self.car.fuel_amount)

    def test_refueling_with_fuel_more_than_capacity(self):
        self.car.refuel(51)
        self.assertEqual(50, self.car.fuel_amount)

    def test_refueling_with_null_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_drive_distance_with_enough_fuel(self):
        self.car.refuel(40)
        self.car.drive(200)
        self.assertEqual(22, self.car.fuel_amount)

    def test_drive_distance_with_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(200)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()
