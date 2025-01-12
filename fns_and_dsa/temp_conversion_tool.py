FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

while True:
    try:
        temperature = float(input("Enter the temperature to convert: "))
        break
    except:
        print("Invalid temperature. Please enter a numeric value.")

temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if temperature_type.lower() == "f":
    print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
elif temperature_type.lower() == "c":
    print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
    
else:
    print("Unknown temperature")
    
# if isinstance(temperature, int) == False:
#     print("Please enter the temperature")
# print( isinstance(temperature, int) )