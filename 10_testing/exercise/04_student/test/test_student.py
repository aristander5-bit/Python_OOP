from unittest import TestCase, main

from project.student import Student


class StudentTests(TestCase):

    def test_init_without_courses(self):
        student = Student("John")
        self.assertEqual(student.name, "John")
        self.assertEqual(student.courses, {})

    def test_init_with_courses(self):
        courses = {"Math": ["Algebra", "Geometry"]}
        student = Student("John", courses)
        self.assertEqual(student.name, "John")
        self.assertEqual(student.courses, courses)

    def test_enroll_existing_course_updates_notes(self):
        student = Student("John", {"Math": ["Algebra"]})
        result = student.enroll("Math", ["Calculus", "Statistics"])

        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertEqual(student.courses["Math"], ["Algebra", "Calculus", "Statistics"])

    def test_enroll_new_course_with_default_notes_flag_adds_course_and_notes(self):
        student = Student("John")
        result = student.enroll("Python", ["OOP", "Advanced"])

        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(student.courses["Python"], ["OOP", "Advanced"])

    def test_enroll_new_course_with_y_notes_flag_adds_course_and_notes(self):
        student = Student("John")
        result = student.enroll("Python", ["OOP"], add_course_notes="Y")

        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(student.courses["Python"], ["OOP"])

    def test_enroll_new_course_without_notes_flag_adds_empty_notes_list(self):
        student = Student("John")
        result = student.enroll("Python", ["OOP"], add_course_notes="N")

        self.assertEqual(result, "Course has been added.")
        self.assertEqual(student.courses["Python"], [])

    def test_add_notes_to_existing_course_updates_successfully(self):
        student = Student("John", {"Math": ["Algebra"]})
        result = student.add_notes("Math", "Calculus")

        self.assertEqual(result, "Notes have been updated")
        self.assertEqual(student.courses["Math"], ["Algebra", "Calculus"])

    def test_add_notes_to_non_existing_course_raises_exception(self):
        student = Student("John", {"Math": ["Algebra"]})
        with self.assertRaises(Exception) as ex:
            student.add_notes("Physics", "Mechanics")
        self.assertEqual(str(ex.exception), "Cannot add notes. Course not found.")

    def test_leave_existing_course_removes_it_successfully(self):
        student = Student("John", {"Math": ["Algebra"]})
        result = student.leave_course("Math")

        self.assertEqual(result, "Course has been removed")
        self.assertEqual(student.courses, {})

    def test_leave_non_existing_course_raises_exception(self):
        student = Student("John", {"Math": ["Algebra"]})
        with self.assertRaises(Exception) as ex:
            student.leave_course("Physics")
        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")


if __name__ == "__main__":
    main()