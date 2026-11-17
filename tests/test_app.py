import runpy
import unittest
from contextlib import redirect_stdout
from io import StringIO

from app import greet


class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World from Reem Saab!")

    def test_greet_another_name(self):
        self.assertEqual(greet("Jenkins"), "Hello, Jenkins from Reem Saab!")

    def test_command_line_greeting(self):
        output = StringIO()
        with redirect_stdout(output):
            runpy.run_module("app", run_name="__main__")
        self.assertEqual(output.getvalue(), "Hello, World from Reem Saab!\n")


if __name__ == "__main__":
    unittest.main()
