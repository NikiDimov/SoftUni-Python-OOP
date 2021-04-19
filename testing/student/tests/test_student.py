from unittest import TestCase, main

# from OOP.testing.student.project.student import Student
from project.student import Student

class TestStudent(TestCase):
    def setUp(self):
        self.student_1 = Student("Test1")

    def test_attr_are_set(self):
        self.assertEqual("Test1", self.student_1.name)
        self.assertEqual({}, self.student_1.courses)

    def test_enroll_course_with_notes_1(self):
        result = self.student_1.enroll("Python OOP", ["Inheritance", "SOLID"])
        self.assertEqual(1, len(self.student_1.courses))
        self.assertEqual(2, len(self.student_1.courses["Python OOP"]))
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_course_with_notes_2(self):
        result = self.student_1.enroll("Python OOP", ["Inheritance", "SOLID"], "Y")
        self.assertEqual(1, len(self.student_1.courses))
        self.assertEqual(2, len(self.student_1.courses["Python OOP"]))
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_course_with_notes_without_saving_them(self):
        result = self.student_1.enroll("Python OOP", ["Inheritance", "SOLID"], "N")
        self.assertEqual(1, len(self.student_1.courses))
        self.assertEqual(0, len(self.student_1.courses["Python OOP"]))
        self.assertEqual("Course has been added.", result)

    def test_enroll_add_notes_to_existing_course(self):
        result = self.student_1.enroll("Python OOP", ["Inheritance", "SOLID"])
        self.assertEqual(1, len(self.student_1.courses))
        self.assertEqual(2, len(self.student_1.courses["Python OOP"]))
        self.assertEqual("Course and course notes have been added.", result)

        result = self.student_1.enroll("Python OOP", ["Abstraction", "Testing"])
        self.assertEqual(1, len(self.student_1.courses))
        self.assertEqual(4, len(self.student_1.courses["Python OOP"]))
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_add_notes_not_existing_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student_1.add_notes("Python OOP", ["1", 2])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_to_existing_course(self):
        result = self.student_1.enroll("Python OOP", ["Inheritance", "SOLID"])
        self.assertEqual(1, len(self.student_1.courses))
        self.assertEqual(2, len(self.student_1.courses["Python OOP"]))
        self.assertEqual("Course and course notes have been added.", result)

        result = self.student_1.add_notes("Python OOP", "Testing")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(3, len(self.student_1.courses["Python OOP"]))
        self.assertIn("Testing", self.student_1.courses["Python OOP"])

    def test_unexisting_course_removal_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student_1.leave_course("Python OOP")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_existing_course(self):
        result = self.student_1.enroll("Python OOP", ["Inheritance", "SOLID"])
        self.assertEqual(1, len(self.student_1.courses))

        result = self.student_1.leave_course("Python OOP")
        self.assertEqual("Course has been removed", result)
        self.assertEqual(0, len(self.student_1.courses))


if __name__ == '__main__':
    main()
