import unittest
from app.auth import Auth


class TddPythonLab(unittest.TestCase):
    def setUp(self):
        self.calc = Auth()


if __name__ == '__main__':
    unittest.main()
