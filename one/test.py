import unittest
from classlib import SampleClass

class TestSampleClass(unittest.TestCase):
    def setUp(self):
        self.instance = SampleClass()

    def test_init(self):
        self.assertIsInstance(self.instance, SampleClass)

    def test_default_value(self):
        self.assertEqual(self.instance.get_value(), 'value at init')

    def test_set_value(self):
        self.instance.set_value('testing this value')
        self.assertEqual(self.instance.get_value(), 'testing this value')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSampleClass)
    unittest.TextTestRunner().run(suite)
