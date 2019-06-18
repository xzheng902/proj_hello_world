from proj_hello_world import hello_world
import unittest
from io import StringIO
import sys

class MyTest(unittest.TestCase):
    def test_print_hello_world(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        hello_world.print_hello_world()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "Hello world\n")

    def test_print_greetings(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        hello_world.print_greetings("Mike")
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "Hello, Mike\n")

if __name__ == '__main__':
    unittest.main()
