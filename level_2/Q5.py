"""
5. You are developing a program that analyzes weather data. Write
a Python function that takes a list of temperature readings for a
specific location and determines the average temperature, highest
temperature, and lowest temperature.
    Input: temperature_readings = [25, 28, 21, 24, 27]
    Output:
        Average Temperature: 25.0
        Highest Temperature: 28
        Lowest Temperature: 21
"""
import json

def unique_elements_in_list(weather_data_lst):

    min_temp = lst[0]
    max_temp = lst[0]

    sum_of_temp = sum(weather_data_lst)
    avg_temp = sum_of_temp / len(weather_data_lst)

    for temperature in weather_data_lst:
        if temperature > max_temp:
            max_temp = temperature
        
        if temperature < min_temp:
            min_temp = temperature

    result = f"""
    Average Temperature: {avg_temp}
    Highest Temperature: {max_temp}
    Lowest Temperature: {min_temp}
            """

    return result

if __name__ == "__main__":
    try:
        weather_data = input()
        lst = json.loads(weather_data)

        print(unique_elements_in_list(lst))
    
    except json.JSONDecodeError:
        print("Invalid input. Please enter a valid JSON list.")
    except Exception as e:
        print("An error occured: {e}")
