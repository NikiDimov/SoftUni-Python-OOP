from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.car = Vehicle(50, 200)

    def test_initialization(self):
        self.assertEqual(50, self.car.fuel)
        self.assertEqual(50, self.car.capacity)
        self.assertEqual(200, self.car.horse_power)
        self.assertEqual(1.25, self.car.fuel_consumption)

    def test_drive_distance_with_enough_fuel(self):
        self.car.drive(2)
        self.assertEqual(47.5, self.car.fuel)

    def test_drive_distance_with_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_with_normal_amount_of_fuel(self):
        self.car.drive(20)
        self.assertEqual(25, self.car.fuel)
        self.car.refuel(5)
        self.assertEqual(30, self.car.fuel)

    def test_refuel_with_extra_amount_of_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(2)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_output_result(self):
        expected = "The vehicle has 200 horse power with 50 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected, str(self.car))


if __name__ == "__main__":
    main()
