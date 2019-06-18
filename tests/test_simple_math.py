from proj_hello_world import simple_math
import unittest

class MyTest(unittest.TestCase):
    def test_mean_0(self):
        list = [1,3,5]
        mean = simple_math.mean(list)
        self.assertEqual(mean, 3)

    def test_mean_1(self):
        list = [1,4,5]
        mean = simple_math.mean(list)
        self.assertAlmostEqual(mean, 3.3333333)

    def test_mean_2(self):
        self.assertRaises(ZeroDivisionError, simple_math.mean, [])

if __name__ == '__main__':
    unittest.main()
