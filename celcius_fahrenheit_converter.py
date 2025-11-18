def celsius_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit
    return (celsius * 9/5) + 32


def main():
    # Ask for temperature in Celsius
    temp_c = float(input("Enter temperature in Celsius: "))
    
    # Convert and display
    temp_f = celsius_to_fahrenheit(temp_c)
    print(f"{temp_c}°C is equal to {temp_f}°F")


# Run the program
if __name__ == "__main__":
    main()

