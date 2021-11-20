from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Niki")

    def test_student_initialization(self):
        self.assertEqual("Niki", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_enroll_in_course_which_is_already_added(self):
        student = Student("Niki", {"English": ["grammar"]})
        actual = student.enroll("English", ["listening", "reading"])
        self.assertEqual("Course already added. Notes have been updated.", actual)
        self.assertEqual({"English": ["grammar", "listening", "reading"]}, student.courses)

    def test_enroll_in_course_with_adding_course_and_notes_I(self):
        actual = self.student.enroll("English", ["listening", "reading"])
        self.assertEqual("Course and course notes have been added.", actual)
        self.assertEqual({"English": ["listening", "reading"]}, self.student.courses)

    def test_enroll_in_course_with_adding_course_and_notes_II(self):
        actual = self.student.enroll("English", ["listening", "reading"], "Y")
        self.assertEqual("Course and course notes have been added.", actual)
        self.assertEqual({"English": ["listening", "reading"]}, self.student.courses)

    def test_enroll_in_course_with_adding_only_course(self):
        actual = self.student.enroll("English", ["listening", "reading"], "No")
        self.assertEqual("Course has been added.", actual)
        self.assertEqual({"English": []}, self.student.courses)

    def test_adding_notes_in_valid_course(self):
        student = Student("Niki", {"English": ["grammar"]})
        actual = student.add_notes("English", "listening")
        self.assertEqual("Notes have been updated", actual)
        self.assertEqual({"English": ["grammar", "listening"]}, student.courses)

    def test_adding_notes_in_invalid_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("English", "listening")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_a_course(self):
        student = Student("Niki", {"English": ["grammar"]})
        self.assertEqual("Course has been removed", student.leave_course("English"))
        self.assertEqual({}, student.courses)

    def test_leave_invalid_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("English")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
