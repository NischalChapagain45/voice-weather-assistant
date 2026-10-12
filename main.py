import requests
import pyttsx3

while True:
    engine = pyttsx3.init()

    city = input("Enter the city whose weather data you want to know: ")
    print("Please wait a second...\n")

    url = f"https://api.weatherapi.com/v1/current.json?key=5dab2445b6734da69c474904261210&q={city}"

    try:
        r = requests.get(url)
        rjson = r.json()

        # Check if the API returned an error (e.g., city not found)
        if "error" in rjson:
            data = f"Sorry, I couldn't find the city '{city}'. Please try again."
        else:
            # Extract weather data
            temp = rjson["current"]["temp_c"]
            lat = rjson["location"]["lat"]
            lon = rjson["location"]["lon"]
            wind_kph = rjson["current"]["wind_kph"]
            wind_deg = rjson["current"]["wind_degree"]

            # Dictionary mapping user queries to corresponding messages
            query_dict = {
                1: f"The temperature of {city} is {temp} degrees Celsius.",
                2: f"The latitude of {city} is {lat}.",
                3: f"The longitude of {city} is {lon}.",
                4: f"The wind speed in {city} is {wind_kph} kilometers per hour.",
                5: f"The wind degree in {city} is {wind_deg} degrees."
            }

            userquery = int(input("Enter the data you want:\n1. Temperature\n2. Latitude\n3. Longitude\n4. Wind kph\n5. Wind degree\nEnter choice (1-5): "))
            
            # Fetch response from dictionary, default to error message if invalid
            data = query_dict.get(userquery, "Please enter a valid number between 1 and 5.")

    except Exception as e:
        data = "An error occurred. Please check your internet connection and try again."

    print(data)
    engine.say(data)
    engine.runAndWait()