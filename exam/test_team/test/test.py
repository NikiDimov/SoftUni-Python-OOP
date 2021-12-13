from unittest import TestCase, main

from project.team import Team


class TestTeam(TestCase):
    def setUp(self):
        self.team = Team("Niki")

    def test_initialization(self):
        self.assertEqual("Niki", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_invalid_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.team.name = "1Niki"
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_adding_members(self):
        actual = self.team.add_member(pesho=18, toshko=20)
        self.assertEqual({"pesho": 18, "toshko": 20}, self.team.members)
        self.assertEqual(f"Successfully added: pesho, toshko", actual)

    def test_remove_member_if_he_doesnt_exist(self):
        self.assertEqual("Member with name pesho does not exist", self.team.remove_member("pesho"))
        self.assertEqual({}, self.team.members)

    def test_remove_member_if_he_exists(self):
        self.team.add_member(pesho=18, toshko=20)
        actual = self.team.remove_member("pesho")
        self.assertEqual("Member pesho removed", actual)
        self.assertEqual({"toshko": 20}, self.team.members)

    def test_greater_than_method_true(self):
        self.team.add_member(pesho=18, toshko=20)
        new_team = Team("Stars")
        actual = self.team > new_team
        self.assertEqual(True, actual)

    def test_greater_than_method_false(self):
        new_team = Team("Stars")
        new_team.add_member(pesho=18, toshko=20)
        actual = self.team > new_team
        self.assertEqual(False, actual)


    def test_len_method(self):
        self.team.add_member(pesho=18, toshko=20)
        self.assertEqual(2, len(self.team))

    def test_add_method(self):
        other_team = Team("Stars")
        other_team.add_member(toshko=20)
        self.team.add_member(pesho=18)
        new_team = self.team + other_team
        self.assertTrue(new_team)
        self.assertEqual("NikiStars", new_team.name)
        self.assertEqual({"pesho": 18, "toshko": 20}, new_team.members)

    def test_output(self):
        self.team.add_member(pesho=18, toshko=20, ani=20)
        expected = f"Team name: Niki\nMember: ani - 20-years old\nMember: toshko - 20-years old\nMember: pesho - 18-years old"
        self.assertEqual(expected, str(self.team))


if __name__ == '__main__':
    main()
