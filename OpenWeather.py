# openweather.py

# Starter code for assignment 4 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# James Homer
# jphomer@uci.edu
# 14782048

import urllib, json
from urllib import request,error


#API Key: 63b3bf0aeb696dbac81b065b1f495d0f
#TODO: error handling
#TODO: commenting
#TODO: customize info?

class OpenWeather:

    key:str = ''
    zip:str = ''
    ccode:str = ''
    weather_obj:str = ''
    temperature:float = 0
    high_temperature:float = 0
    low_temperature:float = 0
    longitude:float = 0
    latitude:float = 0
    description:str = ''
    humidity:int = 0
    sunset:int = 0
    city:str = ''

    def __init__(self, zipcode, ctrycode):
        self.zip = zipcode
        self.ccode = ctrycode

    
    def set_apikey(self, apikey:str) -> None:
        '''
        Sets the apikey required to make requests to a web API.
        :param apikey: The apikey supplied by the API service
        '''
        self.key = apikey


    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.
        '''
        response = None
        r_obj = None
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={self.zip},{self.ccode}&appid={self.key}"

        try:
            response = urllib.request.urlopen(url)
            json_results = response.read()
            r_obj = json.loads(json_results)
        except urllib.error.HTTPError as e:
            print('Failed to download contents of URL')
            print('Status code: {}'.format(e.code))
        except urllib.error.URLError as e:
            print('Loss of local connection to the Internet')
            print('Status code: {}'.format(e.code))
        finally:
            if response != None:
                response.close()
        
        self.weather_obj = r_obj
        self.temperature = self.weather_obj["main"]["temp"]
        self.high_temperature = self.weather_obj["main"]["temp_max"]
        self.low_temperature = self.weather_obj["main"]["temp_min"]
        self.longitude = self.weather_obj["coord"]["lon"]
        self.latitude = self.weather_obj["coord"]["lat"]
        self.description = self.weather_obj["weather"][0]["description"]
        self.humidity = self.weather_obj["main"]["humidity"]
        self.city = self.weather_obj["name"]
        self.sunset = self.weather_obj["sys"]["sunset"]
    

    def transclude(self, message:str) -> str:
        '''
        Replaces keywords in a message with associated API data.
        :param message: The message to transclude
            
        :returns: The transcluded message
        '''
        #TODO: write code necessary to transclude keywords in the message parameter with appropriate data from API
        message = message.replace("@weather", self.description)
        return message











""" def _download_url(url_to_download: str) -> dict:
    response = None
    r_obj = None

    try:
        response = urllib.request.urlopen(url_to_download)
        json_results = response.read()
        r_obj = json.loads(json_results)

    except urllib.error.HTTPError as e:
        print('Failed to download contents of URL')
        print('Status code: {}'.format(e.code))

    finally:
        if response != None:
            response.close()
        
    return r_obj

def main() -> None:
    zip = "92697"
    ccode = "US"
    apikey = "63b3bf0aeb696dbac81b065b1f495d0f"
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip},{ccode}&appid={apikey}"

    weather_obj = _download_url(url)
    if weather_obj is not None:
        print(weather_obj['weather'][0]['description'])


if __name__ == '__main__':
    main() """