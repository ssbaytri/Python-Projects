import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_name = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_btn = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.descr_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_name)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_btn)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.descr_label)

        self.setLayout(vbox)

        self.city_name.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.descr_label.setAlignment(Qt.AlignCenter)

        self.city_name.setObjectName("city_name")
        self.city_input.setObjectName("city_input")
        self.get_weather_btn.setObjectName("weather_btn")
        self.temperature_label.setObjectName("temp_label")
        self.emoji_label.setObjectName("emoji_label")
        self.descr_label.setObjectName("desc_label")

        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: calibri;
            }
            #city_name {
                font-size: 40px;
            }
            #city_input {
                font-size: 40px;
            }
            #weather_btn {
                font-size: 30px;
                font-weight: bold;
            }
            #temp_label {
                font-size: 70px;
            }
            #emoji_label {
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            #desc_label {
                font-size: 50px;
            }
        """)

        self.get_weather_btn.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "API_KEY"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request:\nPlease check your input!")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API Key!")
                case 403:
                    self.display_error("Forbidden:\nAccess is denied!")
                case 404:
                    self.display_error("Not Found:\nCity not found!")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later!")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the server!")
                case 503:
                    self.display_error("Service Unavailable:\nServer is donw!")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from the server!")
                case _:
                    self.display_error(f"HTTP error occurred:\n{http_error}")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too Many Redirects:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")

    def display_error(self, msg):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(msg)
        self.emoji_label.clear()
        self.descr_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 70px;")
        temp_k = data["main"]["temp"]
        temp_c = temp_k - 273.15
        weather_desc = data["weather"][0]["description"]
        weather_id = data["weather"][0]["id"]

        self.temperature_label.setText(f"{temp_c:.2f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.descr_label.setText(weather_desc)

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
