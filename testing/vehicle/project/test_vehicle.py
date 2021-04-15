from unittest import TestCase, main

from OOP.testing.vehicle.project.vehicle import Vehicle
# from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50, 200)

    def test_check_instance_attr_are_set(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_check_capacity_unchanged_if_fuel_changed(self):
        self.assertEqual(50, self.vehicle.capacity)
        self.vehicle.fuel = 20
        self.assertEqual(50, self.vehicle.capacity)

    def test_drive_car(self):
        self.vehicle.drive(5)
        self.assertEqual(43.75, self.vehicle.fuel)

    def test_drive_not_successful(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(49)
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_raises_when_more_than_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_success(self):
        self.vehicle.drive(5)
        self.assertEqual(43.75, self.vehicle.fuel)
        self.vehicle.refuel(1)
        self.assertEqual(44.75, self.vehicle.fuel)

    def test_str_representation_dunder(self):
        self.assertEqual(f"The vehicle has 200 horse power with 50 fuel left "
                         f"and 1.25 fuel consumption", str(self.vehicle))


if __name__ == '__main__':
    main()
