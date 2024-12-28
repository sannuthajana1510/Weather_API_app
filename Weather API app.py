import sys
from re import match
from urllib.error import HTTPError

import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
       self.setWindowTitle("Weather App")

       vbox = QVBoxLayout()

       vbox.addWidget(self.city_label)
       vbox.addWidget(self.city_input)
       vbox.addWidget(self.get_weather_button)
       vbox.addWidget(self.temperature_label)
       vbox.addWidget(self.emoji_label)
       vbox.addWidget(self.description_label)

       self.setLayout(vbox)

       self.city_label.setAlignment(Qt.AlignCenter)
       self.city_input.setAlignment(Qt.AlignCenter)
       self.temperature_label.setAlignment(Qt.AlignCenter)
       self.emoji_label.setAlignment(Qt.AlignCenter)
       self.description_label.setAlignment(Qt.AlignCenter)

       self.city_label.setObjectName("city_label")
       self.city_input.setObjectName("city_input")
       self.get_weather_button.setObjectName("get_weather_button")
       self.temperature_label.setObjectName("temperature_label")
       self.emoji_label.setObjectName("emoji_label")
       self.description_label.setObjectName("description_label")

       self.setStyleSheet("""
           QLabel, QPushButton{
               font-family: calibre;
           }
           QLabel#city_label{
               font-size: 40px;
               font-style: catholic;
           }
           QLineEdit#city_input{
               font-size: 40px;
           }
           QPushButton#get_weather_button{
               font-size: 25px;
               font-weight: bold;
           }
           QLabel#temperature_label{
               font-size: 75px;
           }
           QLabel#emoji_label{
               font-size: 100px;
               font-family: segeo UI emoji;
           }
           QLabel#description_label{
               font-size: 50px;
           }
        """)

       self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):

        api_key = "42d8e62e3e410b55aee3b2e042452ec9"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                 self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            status_code = response.status_code
            if status_code == 400:
                self.display_error("Bad request:\nPlease check your input")
            elif status_code == 401:
                self.display_error("Unauthorized:\nInvalid API key")
            elif status_code == 403:
                self.display_error("Forbidden:\nAccess is denied")
            elif status_code == 404:
                self.display_error("Not found:\ncity not found")
            elif status_code == 500:
                self.display_error("Internal Server Error:\nPlease try again later")
            elif status_code == 502:
                self.display_error("Bad Gateway:\nInvalid response from the server")
            elif status_code == 503:
                self.display_error("Service unavailable:\nService is doom")
            elif status_code == 504:
                self.display_error("Gateway timeout:\nNo response from the server")
            else:
                self.display_error(f"HTTP error occurred:\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nthe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 50px;")
        self.description_label.setStyleSheet("font-size: 25px;")
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]
        print(data)

        self.temperature_label.setText(f"{round(temperature_c)}℃")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):

        if 232 >= weather_id >= 200:
            return"⛈️"
        elif 321 >= weather_id >= 300:
            return"🌧️"
        elif 531 >= weather_id >= 500:
            return"⛅"
        elif 622 >= weather_id >= 600:
            return"❄️"
        elif 741 >= weather_id >= 700:
            return"🌁"
        elif weather_id == 762:
            return"🌋"
        elif weather_id == 771:
            return "🌪️"
        elif weather_id == 781:
            return"💨"
        elif weather_id == 800:
            return"☀️"
        elif 801>= weather_id >=804:
            return"☁️"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())





















