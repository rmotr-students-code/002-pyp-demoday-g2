from Glocal.API import google_maps
from Glocal.API import local_tweets
from Glocal.API import local_insta
import unittest


class TestGMapsAPI(unittest.TestCase):
    def setUp(self):
        self.st_num = "1500"
        self.st_name = "Massachusetts"
        self.st_type = "Avenue"
        self.city = "Washington"
        self.state = "DC"

    def test_get_coordinates(self):
        self.assertEqual((google_maps.get_coordinates(self.st_num, self.st_name,
                                                      self.st_type, self.city,
                                                      self.state)),
                         (38.9064936, -77.03541179999999))


class TestLocalTweetsAPI(unittest.TestCase):
    def setUp(self):
        self.st_num = "1500"
        self.st_name = "Massachusetts"
        self.st_type = "Avenue"
        self.city = "Washington"
        self.state = "DC"
        self.miles = "1"

    def test_local_tweets(self):
        self.assertIsNotNone(local_tweets.get_local_tweets(self.st_num,
                                                          self.st_name,
                                                          self.st_type,
                                                          self.city,
                                                          self.state))

    def test2_local_tweets(self):
        self.assertTrue(len(local_tweets.get_local_tweets(self.st_num,
                                                          self.st_name,
                                                          self.st_type,
                                                          self.city,
                                                          self.state,
                                                          self.miles)) > 1)

class TestLocalInstagramAPI(unittest.TestCase):

    def setUp(self):
        self.st_num = "1500"
        self.st_name = "Massachusetts"
        self.st_type = "Avenue"
        self.city = "Washington"
        self.state = "DC"
        self.miles = "1"

    def test_local_insta(self):
        self.assertIsNotNone(local_insta.get_local_instagram(self.st_num,
                                                             self.st_name,
                                                             self.st_type,
                                                             self.city,
                                                             self.state,
                                                             self.miles))

    def test2_local_insta(self):
        self.assertTrue(len(local_insta.get_local_instagram(self.st_num,
                                                            self.st_name,
                                                            self.st_type,
                                                            self.city,
                                                            self.state,
                                                            self.miles)) > 1)

if __name__ == '__main__':
    unittest.main()
