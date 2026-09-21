import unittest
from src.validator import is_valid_student_id, is_valid_email

class TestValidator(unittest.TestCase):
    """
    Test suite cho module validator.
    Các test case mở rộng sẽ được bổ sung trong Issue #4 (Add unit tests for validator).
    """
    def test_student_id_valid(self):
        self.assertTrue(is_valid_student_id("12345678"))

    def test_email_valid(self):
        self.assertTrue(is_valid_email("student@example.com"))

if __name__ == "__main__":
    unittest.main()
