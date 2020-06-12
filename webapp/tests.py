from app import app, add
import os
import unittest


class AppTestCase(unittest.TestCase):
    def test_add(self):
        answer = add(1,3)
        assert answer == 4
    
if __name__ == '__main__':
    unittest.main()
