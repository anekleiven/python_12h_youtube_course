# Weather API app based on the API from weatherapi.com 

# Create an account to get a API key. Sign up here: https://www.weatherapi.com/
# Input your own API key in the API key field before running the program. 

import sys 
import requests 
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                             QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt 

class WeatherApp(QWidget): 
    def __init__(self):
        super().__init__() 
        self.city_label = QLabel("Enter city name: ", self) 
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self) 
        self.temperature_label = QLabel(self) 
        self.emoji_label = QLabel(self)
        self.description = QLabel(self) 
        self.initUI() 
    
    def initUI(self): 
        self.setWindowTitle("Weather app") 

        vbox = QVBoxLayout() 

        # add widgets 
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button) 
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label) 
        vbox.addWidget(self.description) 

        self.setLayout(vbox) 

        # align objects in center
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description.setAlignment(Qt.AlignCenter)

        # set unique name to Qt objects 
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description.setObjectName("description")

        # set stylesheet 
        self.setStyleSheet("""
            QLabel{ 
                font-family: calibri;
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input{
                font-size: 40px;
            }
            QPushButton#get_weather_button{
                font-size: 30px; 
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 75px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description{
                font-size: 50px;
            }
                           """)
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self): 
        api_key = "9392ac8ad8494e1e841115756251610"
        city = self.city_input.text() 
        url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

        try:
            response = requests.get(url, timeout=5)
            data = response.json()

            # Check for WeatherAPI logical errors
            if "error" in data:
                code = data["error"].get("code")
                message = data["error"].get("message", "Unknown error")

                match code:
                    case 1002:
                        self.display_error("API key not provided.")
                    case 1003:
                        self.display_error("Missing 'q' parameter (city name).")
                    case 1005:
                        self.display_error("Invalid API request URL.")
                    case 1006:
                        self.display_error("No matching location found\nCheck the city name.")
                    case 2006:
                        self.display_error("Invalid API key.")
                    case 2007:
                        self.display_error("API key has exceeded monthly quota.")
                    case 2008:
                        self.display_error("API key has been disabled.")
                    case 2009:
                        self.display_error("API key does not have access to this resource.")
                    case 9000:
                        self.display_error("Invalid JSON body in request.")
                    case 9001:
                        self.display_error("Too many locations in bulk request (max 50).")
                    case 9999:
                        self.display_error("Internal application error.")
                    case _:
                        self.display_error(f"Error {code}: {message}")
                return  # Stop here

            # If no logical error, check for HTTP errors
            response.raise_for_status()

            # if no HTTP errors: 
            self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            code = response.status_code

            match code:
                case 400:
                    self.display_error("Bad request.\nPlease check your input.")
                case 401:
                    self.display_error("Unauthorized-\nInvalid API key.")
                case 403:
                    self.display_error("Forbidden.\nAccess denied.")
                case 404:
                    self.display_error("Not found.\nInvalid URL or endpoint.")
                case 500:
                    self.display_error("Internal server error.\nTry again later.")
                case 502:
                    self.display_error("Bad gateway\nInvalid response from server.")
                case 503:
                    self.display_error("Service unavailable\nServer is down.")
                case 504:
                    self.display_error("Gateway timeout\nServer didn’t respond.")
                case _:
                    self.display_error(f"HTTP error occurred ({code}): {http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection error.\nCheck your internet connection.")
        except requests.exceptions.Timeout:
            self.display_error("Timeout.\nThe request took too long.")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects.\nInvalid URL.")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error: {req_error}")
        

    def display_error(self, message): 
            self.temperature_label.setStyleSheet("font-size: 30px")
            self.temperature_label.setText(message) 
            self.emoji_label.clear() 
            self.description.clear()

    def display_weather(self, data): 
            self.temperature_label.setStyleSheet("font-size: 75px") 
            temperature_c = data['current']['temp_c']
            weather_description = data['current']['condition']['text'] 
            weather_id = data['current']['condition']['code']

            self.temperature_label.setText(f"{temperature_c:.0f}°C")
            self.emoji_label.setText(self.get_weather_emoji(weather_id))
            self.description.setText(f"{weather_description}")  
    
    # static methods belong to a class, but do not require any other instance of data 
    # or any other method
    @staticmethod
    def get_weather_emoji(weather_id):
        # ☀️ Clear / sunny
        if weather_id == 1000:
            return "☀️"

        # ⛅ Partly cloudy
        elif weather_id == 1003:
            return "⛅"

        # ☁️ Cloudy / Overcast
        elif weather_id in (1006, 1009):
            return "☁️"

        # 🌫️ Mist / Fog
        elif weather_id in (1030, 1135, 1147):
            return "🌫️"

        # 🌦️ Patchy rain
        elif weather_id == 1063:
            return "🌦️"

        # 🌨️ Patchy snow
        elif weather_id == 1066:
            return "🌨️"

        # 🌧️❄️ Patchy sleet
        elif weather_id == 1069:
            return "🌧️❄️"

        # 🌧️🧊 Patchy freezing drizzle
        elif weather_id == 1072:
            return "🌧️🧊"

        # ⛈️ Thunder
        elif weather_id == 1087:
            return "⛈️"

        # 🌨️💨 Blowing snow / Blizzard
        elif weather_id in (1114, 1117):
            return "🌨️💨"

        # 🌦️ Light drizzle
        elif weather_id in (1150, 1153):
            return "🌦️"

        # 🌧️🧊 Freezing drizzle
        elif weather_id in (1168, 1171):
            return "🌧️🧊"

        # 🌧️ Light to moderate rain
        elif weather_id in (1180, 1183, 1186, 1189):
            return "🌧️"

        # 🌧️💧 Heavy rain
        elif weather_id in (1192, 1195):
            return "🌧️💧"

        # 🌧️❄️ Freezing rain
        elif weather_id in (1198, 1201):
            return "🌧️❄️"

        # 🌨️ Light to heavy sleet
        elif weather_id in (1204, 1207):
            return "🌨️🌧️"

        # ❄️ Light to moderate snow
        elif weather_id in (1210, 1213, 1216, 1219):
            return "❄️"

        # ❄️☃️ Heavy snow
        elif weather_id in (1222, 1225, 1258):
            return "❄️☃️"

        # 🧊 Ice pellets / showers
        elif weather_id in (1237, 1261, 1264):
            return "🧊🌧️"

        # 🌦️ Rain showers (light to heavy)
        elif weather_id in (1240, 1243, 1246):
            return "🌦️"

        # 🌧️❄️ Sleet showers
        elif weather_id in (1249, 1252):
            return "🌧️❄️"

        # 🌨️❄️ Snow showers
        elif weather_id in (1255, 1258):
            return "🌨️❄️"

        # ⛈️🌧️ Thunder with rain
        elif weather_id in (1273, 1276):
            return "⛈️🌧️"

        # ⛈️❄️ Thunder with snow
        elif weather_id in (1279, 1282):
            return "⛈️❄️"

        # ❓ Default (unknown)
        else:
            return "🌈"


app = QApplication(sys.argv) 
weather_app = WeatherApp()
weather_app.show() 
sys.exit(app.exec_())