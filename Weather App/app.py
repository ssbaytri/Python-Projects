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
        api_key = "Your_api_key"
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
                    print("Bad Request\nPlease check your input!")
                case 401:
                    print("Unauthorized\nInvalid API Key!")
                case 403:
                    print("Forbidden\nAccess is denied!")
                case 404:
                    print("Not Found\nCity not found!")
                case 500:
                    print("Internal Server Error\nPlease try again later!")
                case 502:
                    print("Bad Gateway\nInvalid response from the server!")
                case 503:
                    print("Service Unavailable\nServer is donw!")
                case 504:
                    print("Gateway Timeout\nNo response from the server!")
                case _:
                    print(f"HTTP error occurred\n{http_error}")

    def display_error(self, msg):
        pass

    def display_weather(self, data):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
