import unittest
import moar

class TestSomeFunctions(unittest.TestCase):
    def test_doubler(self):
        self.assertEqual(moar.doubler(3), 6)

    def test_text_formatter(self):
        self.assertEqual(moar.text_formatter("foo"), "i has a foo and i like it")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSomeFunctions)
    unittest.TextTestRunner().run(suite)
