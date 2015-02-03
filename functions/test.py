import unittest
import somefunctions as sf

class TestSomeFunctions(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(sf.fib(8), 21)

    def test_fiblist(self):
        self.assertEqual(sf.fiblist(5), [0, 1, 1, 2, 3])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSomeFunctions)
    unittest.TextTestRunner().run(suite)
