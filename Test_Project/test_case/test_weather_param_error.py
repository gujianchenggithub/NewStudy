import unittest
import requests

from time import  sleep

class WeatherTest(unittest.TestCase):
    def setUp(self):
        self.url='https://www.sojson.com/open/api/weather/json.shtml'


    def test_weather_param_error(self):
        data={'city':'999'}
        r=requests.get(self.url,params=data)
        result=r.json()

        self.assertEqual(result['message'],'Check the parameters.')
        sleep(3)



if __name__ == '__main__':
    unittest.main()
