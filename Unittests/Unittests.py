from Glocal.API import API
import unittest

class TestGetCoordinates(unittest.TestCase):
    def setUp(self):
        self.st_num = "1500"
        self.st_name = "Massachusetts"
        self.st_type = "Avenue"
        self.city = "Washington"
        self.state = "DC"
        user_query = API.GlocalAPI(self.st_num, self.st_name, self.st_type,
                                   self.city, self.state)
        self.latitude, self.longitude = user_query.get_coordinates()

    def test_get_coordinates(self):
        self.assertEqual((self.latitude,self.longitude),
                         (38.9064936, -77.03541179999999))

class TestGetTweets(unittest.TestCase):
    def setUp(self):
        self.st_num = "1500"
        self.st_name = "Massachusetts"
        self.st_type = "Avenue"
        self.city = "Washington"
        self.state = "DC"
        self.user_query = API.GlocalAPI(self.st_num, self.st_name, self.st_type,
                                        self.city, self.state)
    def test_get_tweets(self):
        self.assertIsNotNone(self.user_query.get_tweets())

    def test2_local_tweets(self):
        self.assertTrue(len(self.user_query.get_tweets()) > 1)

class TestGetInstagram(unittest.TestCase):
    def setUp(self):
        self.st_num = "1500"
        self.st_name = "Massachusetts"
        self.st_type = "Avenue"
        self.city = "Washington"
        self.state = "DC"
        self.user_query = API.GlocalAPI(self.st_num, self.st_name, self.st_type,
                                        self.city, self.state)

    def test_get_instagram(self):
        self.assertIsNotNone(self.user_query.get_instagram())

    def test2_get_instagram(self):
        self.assertTrue(len(self.user_query.get_instagram()) > 1)


if __name__ == '__main__':
    unittest.main()
