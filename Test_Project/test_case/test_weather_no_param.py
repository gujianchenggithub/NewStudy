import unittest
import requests

from time import  sleep

class WeatherTest(unittest.TestCase):
    def setUp(self):
        self.url='https://www.sojson.com/open/api/weather/json.shtml'



    def test_weather_no_param(self):

        r=requests.get(self.url)
        result=r.json()

        self.assertEqual(result['message'],'Check the parameters.')
        self.assertEqual(result['status'],400)
        sleep(3)

if __name__ == '__main__':
    unittest.main()
