import unittest
import calculator_app


class testCaseAdd(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator_app.addition(5, 10), 14)


if __name__ == "__main__":
    unittest.main()
