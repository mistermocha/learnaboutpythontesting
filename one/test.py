import unittest
from classlib import SampleClass

class TestSampleClass(unittest.TestCase):
    def setUp(self):
        self.instance = SampleClass()

    def test_init(self):
        self.assertIsInstance(self.instance, SampleClass)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSampleClass)
    unittest.TextTestRunner().run(suite)
