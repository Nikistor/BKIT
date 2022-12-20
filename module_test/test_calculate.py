import unittest

from calculate.arithmetic_calculate import mathematical_calculator as smc

class test_calculate(unittest.TestCase):

    # Проверка на работу
    def test_1(self):
        self.assertEqual(smc('20.0').result, 20.0)
    def test_2(self):
        self.assertEqual(smc('12 + 12').result, 24.0)
    def test_3(self):
        self.assertEqual(smc('3 + 5 * 2').result, 13.0)
    def test_4(self):
        self.assertEqual(smc('5 + 2 + 9').result, 16.0)
    def test_5(self):
        self.assertEqual(smc('130 + 15 - 39').result, 106.0)
    def test_6(self):
        self.assertEqual(smc('5 * 2 / 5').result, 2.0)
    def test_7(self):
        self.assertEqual(smc('5 - 3 / 3').result, 4.0)
    def test_8(self):
        self.assertEqual(smc('5 * 0').result, 0.0)
    def test_9(self):
        self.assertEqual(smc('3 / 0').result, 'infinity')

if __name__ == '__main__':
    unittest.main()
