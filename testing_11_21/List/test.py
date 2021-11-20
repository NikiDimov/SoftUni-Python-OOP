from testing.List.extended_list import IntegerList
from unittest import TestCase, main


class TestExtendedList(TestCase):
    def setUp(self):
        self.new_list = IntegerList(1, 2, 3)

    def test_the_constructor(self):
        self.assertEqual([1, 2, 3], self.new_list.get_data())

    def test_the_constructor_II(self):
        new_list = IntegerList(1, 2.3, 'one')
        self.assertEqual([1], new_list.get_data())

    def test_add_integer(self):
        self.new_list.add(4)
        self.assertEqual([1, 2, 3, 4], self.new_list.get_data())

    def test_add_not_integer(self):
        with self.assertRaises(ValueError) as ex:
            self.new_list.add(2.3)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index(self):
        self.new_list.remove_index(1)
        self.assertEqual([1, 3], self.new_list.get_data())

    def test_remove_index_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.new_list.remove_index(4)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_function(self):
        result = self.new_list.get(2)
        self.assertEqual(3, result)

    def test_get_functionality_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.new_list.get(5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_with_valid_index_and_value(self):
        self.new_list.insert(2, 10)
        self.assertEqual([1, 2, 10, 3], self.new_list.get_data())

    def test_insert_with_invalid_index(self):
        with self.assertRaises(IndexError) as ex:
            self.new_list.insert(5, 2)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_with_invalid_element(self):
        with self.assertRaises(ValueError) as ex:
            self.new_list.insert(0, 'a')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_get_biggest(self):
        self.assertEqual(3, self.new_list.get_biggest())

    def test_get_index(self):
        result = self.new_list.get_index(2)
        self.assertEqual(1, result)


if __name__ == "__main__":
    main()
