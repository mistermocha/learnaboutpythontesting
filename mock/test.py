import unittest
import mock
import getter

class TestSomeFunctions(unittest.TestCase):
    @mock.patch('urllib2.urlopen')
    def test_getter(self, mocked_urllib2):
        mocked_urllib2.return_value = open('mock.txt', 'r')
        self.assertEqual(getter.disallowed(), ['/thiswillfail/'])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSomeFunctions)
    unittest.TextTestRunner().run(suite)
