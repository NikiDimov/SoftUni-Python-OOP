from unittest import TestCase, main

from project.library import Library


class TestLibrary(TestCase):
    def setUp(self):
        self.library = Library("Botev")

    def test_initialization(self):
        self.assertEqual("Botev", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_set_an_empty_name(self):
        with self.assertRaises(ValueError) as ex:
            self.library.name = ''
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_add_book_but_no_author_in_books_by_author(self):
        self.library.add_book("Vazov", "Pod igoto")
        self.assertEqual({"Vazov": ["Pod igoto"]}, self.library.books_by_authors)

    def test_add_book_author_in_books_by_author(self):
        self.library.add_book("Vazov", "Pod igoto")
        self.library.add_book("Vazov", "Nemili, nedragi")
        self.assertEqual({"Vazov": ["Pod igoto", "Nemili, nedragi"]}, self.library.books_by_authors)

    def test_add_reader(self):
        self.library.add_reader("Niki")
        self.assertEqual({"Niki": []}, self.library.readers)
        self.assertEqual("Niki is already registered in the Botev library.", self.library.add_reader("Niki"))

    def test_rent_book_by_a_reader_not_in_the_list(self):
        actual = self.library.rent_book("Misho", "Vazov", "Pod igoto")
        expected = "Misho is not registered in the Botev Library."
        self.assertEqual(expected, actual)

    def test_rent_book_with_invalid_author_name(self):
        self.library.add_reader("Niki")
        actual = self.library.rent_book("Niki", "Elin Pelin", "Po jicata")
        expected = "Botev Library does not have any Elin Pelin's books."
        self.assertEqual(expected, actual)

    def test_rent_book_with_invalid_authors_book(self):
        self.library.add_book("Vazov", "Pod igoto")
        self.library.add_reader("Niki")
        actual = self.library.rent_book("Niki", "Vazov", "Nemili, nedragi")
        expected = """Botev Library does not have Vazov's "Nemili, nedragi"."""
        self.assertEqual(expected, actual)

    def test_rent_book_correct_way(self):
        self.library.add_book("Vazov", "Pod igoto")
        self.library.add_reader("Niki")
        self.library.rent_book("Niki", "Vazov", "Pod igoto")
        self.assertEqual({"Niki": [{"Vazov": "Pod igoto"}]}, self.library.readers)
        self.assertEqual({"Vazov": []}, self.library.books_by_authors)


if __name__ == '__main__':
    main()
