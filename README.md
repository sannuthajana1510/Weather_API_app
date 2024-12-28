Weather Application

This project implements a simple weather application using Python and PyQt5.  It fetches weather data from the OpenWeatherMap API and displays it in a user-friendly graphical interface.

Characteristics

* City Input: Allows users to enter a city name to get weather information.
* API Integration: Uses the OpenWeatherMap API ([https://openweathermap.org/](https://openweathermap.org/)) to retrieve real-time weather data.
* Error Handling: Robustly handles various error conditions, such as invalid city names, network issues, and API errors, providing informative error messages to the user.
* Clear Display: Presents weather information clearly with temperature (Celsius), a relevant emoji, and a descriptive text.
* Customizable Styling:  The appearance is customizable through embedded CSS for fonts, sizes, and layout.

Prerequisites

* Python 3.x
* PyQt5:  `pip install PyQt5`
* requests: `pip install requests`

Utilization

1. Clone the repository: `git clone <repository_url>`
2. Navigate to the project directory: `cd Weather-App`
3. Run the application: `python Weather_API_app.py`

API Key

The application uses an API key for the OpenWeatherMap API.  The key is currently hardcoded within the source code.  For security best practices, consider storing the API key in a more secure manner (e.g., environment variables) before deploying to a production environment.

Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

 
