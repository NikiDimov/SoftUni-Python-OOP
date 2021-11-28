from unittest import TestCase, main

from project.train.train import Train


class TestTrain(TestCase):
    def setUp(self):
        self.train = Train("A1", 20)

    def test_initialization(self):
        self.assertEqual("A1", self.train.name)
        self.assertEqual(20, self.train.capacity)
        self.assertEqual([], self.train.passengers)
        self.assertEqual(0, self.train.ZERO_CAPACITY)

    def test_add_passenger_when_the_train_is_full_raises(self):
        train = Train("A1", 1)
        train.add("Niki")
        self.assertEqual(["Niki"], train.passengers)
        with self.assertRaises(ValueError) as ex:
            train.add("Pesho")
        self.assertEqual("Train is full", str(ex.exception))

    def test_add_passenger_with_the_same_name_raises(self):
        train = Train("A1", 2)
        train.add("Niki")
        with self.assertRaises(ValueError) as ex:
            train.add("Niki")
        self.assertEqual("Passenger Niki Exists", str(ex.exception))

    def test_add_a_valid_passenger(self):
        actual = self.train.add("Niki")
        self.assertEqual("Added passenger Niki", actual)
        self.assertEqual(["Niki"], self.train.passengers)

    def test_remove_passenger_who_is_not_in_the_list_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.train.remove("Niki")
        self.assertEqual("Passenger Not Found", str(ex.exception))

    def test_remove_passenger_who_is_in_the_list(self):
        self.train.add("Niki")
        self.assertEqual(["Niki"], self.train.passengers)
        actual = self.train.remove("Niki")
        self.assertEqual("Removed Niki", actual)
        self.assertEqual([], self.train.passengers)


if __name__ == "__main__":
    main()
