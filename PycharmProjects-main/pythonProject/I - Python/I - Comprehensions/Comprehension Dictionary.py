# DICTIONARY COMPREHENSION = create dictionaries using an expression; can replace for loops and certain lambda functions
# dictionary = {key: expression for (key, value) in iterable}

cities_in_Fahrenheit = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 69}

cities_in_Celcius = {key: round((value-32)*(5/9)) for (key, value) in cities_in_Fahrenheit.items()}
print(cities_in_Celcius)

print("------------------------------------------------------------------------------------")
# dictionary = {key: expression for (key, value) in iterable if conditional}

weather = {"New York": "snowing", "Boston": "sunny", "Los Angeles": "sunny", "Chicago": "bipolar"}
sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
print(sunny_weather)

print("------------------------------------------------------------------------------------")
# dictionary = {key: if/else for (key, value) in iterable}

cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 69}
does_cities = {key: ("Warm" if value >= 40 else "Cold") for (key, value) in cities.items()}
print(does_cities)

print("------------------------------------------------------------------------------------")
# dictionary = {key: function(value) for (key, value) in iterable}

def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"

cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 69}
does_cities = {key: check_temp(value) for (key, value) in cities.items()}
print(does_cities)
