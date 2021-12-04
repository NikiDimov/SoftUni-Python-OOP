from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self):
        self.factory = PaintFactory("Niki", 100)

    def test_initialization(self):
        self.assertEqual("Niki", self.factory.name)
        self.assertEqual(100, self.factory.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.factory.valid_ingredients)
        self.assertEqual({}, self.factory.ingredients)

    def test_can_add_method(self):
        self.assertTrue(self.factory.can_add(100))

    def test_add_ingredient(self):
        self.factory.add_ingredient("white", 50)
        self.assertEqual({"white": 50}, self.factory.ingredients)

    def test_add_ingredient_if_full_capacity_raises(self):
        self.factory.add_ingredient("white", 50)
        with self.assertRaises(ValueError) as ex:
            self.factory.add_ingredient("white", 60)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_an_invalid_ingredient_raises(self):
        with self.assertRaises(TypeError) as ex:
            self.factory.add_ingredient("purple", 50)
        self.assertEqual(f"Ingredient of type purple not allowed in PaintFactory", str(ex.exception))

    def test_remove_ingredient(self):
        self.factory.add_ingredient("white", 50)
        self.factory.remove_ingredient("white", 30)
        self.assertEqual({"white": 20}, self.factory.ingredients)

    def test_remove_ingredient_leaving_negative_quantity_raises(self):
        self.factory.add_ingredient("white", 50)
        with self.assertRaises(ValueError) as ex:
            self.factory.remove_ingredient("white", 60)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_try_to_remove_invalid_ingredient_raises(self):
        with self.assertRaises(KeyError) as ex:
            self.factory.remove_ingredient("purple", 60)
        self.assertIn("No such ingredient in the factory", str(ex.exception))

    def test_property_products(self):
        self.factory.add_ingredient("white", 50)
        self.assertEqual({"white": 50}, self.factory.products)

    def test_output(self):
        self.factory.add_ingredient("white", 50)
        expected = f"Factory name: Niki with capacity 100.\nwhite: 50\n"
        self.assertEqual(expected, str(self.factory))


if __name__ == '__main__':
    main()
