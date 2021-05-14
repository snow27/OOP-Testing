import unittest

from project.student import Student


class TestStudent(unittest.TestCase):

    def test_atr_in_class_if_courses_is_none(self):
        expected_name = "ivan"
        expected_courses = {}
        student = Student("ivan")
        self.assertEqual(expected_name, student.name)
        self.assertEqual(expected_courses, student.courses)

    def test_atr_in_class_if_courses(self):
        student = Student("ivan", {"softuni": ["first", "second"]})
        expected_name = "ivan"
        expected_courses = {"softuni": ["first", "second"]}
        self.assertEqual(expected_name, student.name)
        self.assertEqual(expected_courses, student.courses)

    def test_enroll_if_course_key_in_courses(self):
        student = Student("ivan", {"softuni": ["first", "second"]})
        result = student.enroll("softuni", "second", "nine")
        expected_return = "Course already added. Notes have been updated."
        self.assertEqual(expected_return, result)

    def test_enroll_if_add_notes_is_Y(self):
        student = Student("ivan", {"softuni": ["first", "second"]})
        result = student.enroll("elena", "tirth", "Y")
        expected_return = "Course and course notes have been added."
        self.assertEqual(expected_return, result)

    def test_enroll_if_add_notes_is_(self):
        student = Student("ivan", {"softuni": ["first", "second"]})
        result = student.enroll("elena", "tirth", "")
        expected_return = "Course and course notes have been added."
        self.assertEqual(expected_return, result)

    def test_enroll_if_add_notes_is_any(self):
        student = Student("ivan", {"softuni": ["first", "second"]})
        result = student.enroll("elena", "tirth", "No")
        expected_return = "Course has been added."
        self.assertEqual(expected_return, result)

    def test_add_notes_when_(self):
        student = Student("ivan", {"softuni": ["first", "second"]})
        result = student.add_notes("softuni", "zero",)
        expected_return = "Notes have been updated"
        self.assertEqual(expected_return, result)

    def test_add_notes_when_course_not_exist(self):
        student = Student("ivan", {"softuni": ["first", "second"]})
        with self.assertRaises(Exception) as ex:
            student.add_notes("not_exist_course", "zero")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_when_course_exist(self):
        student = Student("ivan", {"softuni": ["first", "second"]})
        result = student.leave_course("softuni")
        expected_return = "Course has been removed"
        self.assertEqual(expected_return, result)

    def test_leave_course_when_course_not_exist(self):
        student = Student("ivan", {"softuni": ["first", "second"]})
        with self.assertRaises(Exception) as ex:
            student.leave_course("not_exist_course")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
