🌦️ Voice-Enabled Weather Assistant

A lightweight, interactive Python command-line application that fetches real-time weather and geographical data for any city worldwide using the WeatherAPI. It combines terminal output with text-to-speech (TTS) technology to read your requested weather metrics aloud.

✨ Features

Real-Time Weather Data: Retrieve live temperature, coordinates (latitude and longitude), wind speed (kph), and wind direction (degrees).

Audio Feedback: Automatically speaks the fetched information out loud using pyttsx3.

Clean Dictionary Mapping: Uses Python dictionaries instead of lengthy conditional blocks for efficient and clean query handling.

Continuous Interactive Loop: Run multiple queries seamlessly in a single session without restarting the script.

Error Handling: Gracefully handles invalid inputs and API lookup failures.

🛠️ Prerequisites & Dependencies

Make sure you have Python installed on your system. You will need the following third-party libraries:

requests: For making HTTP requests to the WeatherAPI.

pyttsx3: For offline text-to-speech conversion.

Installation

Install the required packages via pip:

pip install requests pyttsx3


Platform Note for pyttsx3:

Windows: Works out of the box using SAPI5.

Linux: May require espeak and libespeak1 installed (sudo apt-get install espeak).

macOS: Uses NSSpeechSynthesizer natively.

🚀 How to Run

Clone this repository or copy the Python script into your local machine.

Open your terminal or command prompt in the project directory.

Run the script:

python weather_assistant.py


Follow the interactive prompts in the terminal:

Enter the name of the city.

Select the data metric you want to check (Temperature, Latitude, Longitude, Wind speed, or Wind degree).

Listen to the voice assistant read out the results and view them on your screen!

📂 Code Structure

import requests
import pyttsx3

# Main infinite loop for continuous querying
while True:
    engine = pyttsx3.init()
    city = input("Enter the city whose weather data you want to know: ")
    
    # API Request configuration...
    # Dictionary query mapping for clean data selection...


🔌 API Reference

This project utilizes the WeatherAPI Current Weather Endpoint. A default development key is included in the script, but you can swap it out for your own free API key if needed.

📜 License

This project is open-source and available under the MIT License.
