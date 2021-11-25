from unittest import TestCase, main

from project.pet_shop import PetShop


class TestPetShop(TestCase):
    def setUp(self):
        self.shop = PetShop("Tommy")

    def test_initialization(self):
        self.assertEqual("Tommy", self.shop.name)
        self.assertEqual([], self.shop.pets)
        self.assertEqual({}, self.shop.food)

    def test_add_food_with_null_quantity(self):
        with self.assertRaises(ValueError) as ex:
            self.shop.add_food("biscuits", 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_in_foods(self):
        actual = self.shop.add_food("biscuits", 20)
        expected = f"Successfully added 20.00 grams of biscuits."
        self.assertEqual(expected, actual)
        self.assertEqual({"biscuits": 20}, self.shop.food)

    def test_add_pet_raises(self):
        self.shop.pets.append("Niki")
        with self.assertRaises(Exception) as ex:
            self.shop.add_pet("Niki")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet(self):
        actual = self.shop.add_pet("Niki")
        self.assertEqual("Successfully added Niki.", actual)
        self.assertEqual(["Niki"], self.shop.pets)

    def test_feed_pet_raises(self):
        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet("biscuits", "Niki")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_if_food_not_in_the_dict(self):
        self.shop.pets.append("Niki")
        actual = self.shop.feed_pet("biscuits", "Niki")
        self.assertEqual('You do not have biscuits', actual)

    def test_feed_pet_if_there_is_no_enough_amount_of_food(self):
        self.shop.pets.append("Niki")
        self.shop.food["biscuits"] = 50
        actual = self.shop.feed_pet("biscuits", "Niki")
        self.assertEqual("Adding food...", actual)
        self.assertEqual({"biscuits": 1050}, self.shop.food)

    def test_feed_pet_if_there_is_enough_amount_of_food(self):
        self.shop.pets.append("Niki")
        self.shop.food["biscuits"] = 200
        actual = self.shop.feed_pet("biscuits", "Niki")
        self.assertEqual("Niki was successfully fed", actual)
        self.assertEqual({"biscuits": 100}, self.shop.food)

    def test_shop_repr(self):
        self.shop.pets.append("Niki")
        self.assertEqual(f'Shop Tommy:\nPets: Niki', str(self.shop))


if __name__ == "__main__":
    main()
