import unittest
import math
class TargetCalculator:
    def count(self, x):
        return x - math.floor(x/3) - math.floor(x/5) + 2*math.floor(x/15)
class TargetCalculatorTest(unittest.TestCase):
    
    def test_example_testcase(self):
        TC = TargetCalculator()
        self.assertEqual(TC.count(15), 9)
    def test_my_testcase0(self):
        TC = TargetCalculator()
        self.assertEqual(TC.count(0), 0)
    def test_my_testcase1(self):
        TC = TargetCalculator()
        self.assertEqual(TC.count(13), 7)
    def test_my_testcase2(self):
        TC = TargetCalculator()
        self.assertEqual(TC.count(199), 120)

if __name__ == '__main__':
	unittest.main()

