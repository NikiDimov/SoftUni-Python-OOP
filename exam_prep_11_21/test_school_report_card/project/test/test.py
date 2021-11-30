from unittest import TestCase, main

from project.student_report_card import StudentReportCard


class TestStudentReportCard(TestCase):
    def setUp(self):
        self.card = StudentReportCard("Niki", 12)

    def test_initialization(self):
        self.assertEqual("Niki", self.card.student_name)
        self.assertEqual(12, self.card.school_year)
        self.assertEqual({}, self.card.grades_by_subject)

    def test_empty_string_for_student_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            StudentReportCard("", 12)
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_student_year_not_between_1_and_12_raises(self):
        with self.assertRaises(ValueError) as ex:
            StudentReportCard("Niki", 13)
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_student_year_is_exactly_1(self):
        self.card.school_year = 1
        self.assertTrue(self.card.school_year)

    def test_add_grade_in_grades_by_subject(self):
        self.card.add_grade("math", 6)
        self.assertEqual({"math": [6]}, self.card.grades_by_subject)

    def test_average_grade_by_subject_and_for_all_subjects_and_report(self):
        self.card.add_grade("math", 6)
        self.card.add_grade("math", 4)
        self.card.add_grade("physic", 5)
        self.card.add_grade("physic", 3)
        self.assertEqual({"math": [6, 4], "physic": [5, 3]}, self.card.grades_by_subject)
        actual = self.card.average_grade_by_subject()
        expected = "math: 5.00\nphysic: 4.00"
        self.assertEqual(expected, actual)
        actual = self.card.average_grade_for_all_subjects()
        expected = "Average Grade: 4.50"
        self.assertEqual(expected, actual)
        report = f"Name: Niki\n" \
                 f"Year: 12\n" \
                 f"----------\n" \
                 f"math: 5.00\nphysic: 4.00\n" \
                 f"----------\n" \
                 f"Average Grade: 4.50"
        self.assertEqual(report, str(self.card))


if __name__ == "__main__":
    main()
