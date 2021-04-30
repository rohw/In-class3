import unittest
import calculator_app


class testCaseAdd(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator_app.addition(5, 10), 15)

    def test_subtraction(self):
        self.assertEqual(calculator_app.subtraction(5, 10), -5)

    def test_multiplication(self):
        self.assertEqual(calculator_app.multiplication(5, 10), 50)

    def test_division(self):
        self.assertEqual(calculator_app.division(10, 5), 2)


if __name__ == "__main__":
    unittest.main()
