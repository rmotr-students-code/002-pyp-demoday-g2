from Glocal.API import GMaps
from Glocal.API import LocalTweets
import unittest


class TestGMapsAPI(unittest.TestCase):

    def setUp(self):
        self.st_num = "1500"
        self.st_name = "Massachusetts"
        self.st_type = "Avenue"
        self.city = "Washington"
        self.state = "DC"

    def test_get_coordinates(self):
        self.assertEqual(
            (GMaps.get_coordinates(self.st_num, self.st_name,self.st_type,
                                   self.city,self.state)),
            (38.9064936, -77.03541179999999))


class TestLocalTweetsAPI(unittest.TestCase):

    def setUp(self):
        self.st_num = "1500"
        self.st_name = "Massachusetts"
        self.st_type = "Avenue"
        self.city = "Washington"
        self.state = "DC"

    def test_local_tweets(self):
        latitude, longitude = GMaps.get_coordinates(self.st_num, self.st_name,
                                                    self.st_type, self.city,
                                                    self.state)
        self.assertIsNotNone(LocalTweets.get_local_tweets(latitude,longitude))

    def test2_local_tweets(self):
        latitude, longitude = GMaps.get_coordinates(self.st_num, self.st_name,
                                                    self.st_type, self.city,
                                                    self.state)
        self.assertTrue(len(LocalTweets.get_local_tweets(latitude,longitude)) > 1)

if __name__ == '__main__':
    unittest.main()
