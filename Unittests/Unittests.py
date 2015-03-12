from Glocal.API import GMaps
import unittest

class TestGMapsAPI(unittest.TestCase):

    def test_get_coordinates(self):
        self.assertEqual((GMaps.get_coordinates('1500','Massachusetts','Avenue','Washington','DC')), (38.9064936, -77.03541179999999))

if __name__ == '__main__':
    unittest.main()
