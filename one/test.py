import unittest
from classlib import SampleClass

class TestSampleClass(unittest.TestCase):
    pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSampleClass)
    unittest.TextTestRunner().run(suite)
