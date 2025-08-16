# Temperature Converter Program with File Output
def temperature_converter():
    print("Welcome to the Temperature Converter Program!")
    print("This tool converts temperature values between Celsius, Fahrenheit, and Kelvin.\n")

    try:
        temp = float(input("Enter the temperature value: "))
        unit = input("Enter the unit (C, F, K): ").upper()

        # Convert to all formats
        if unit == "C":
            c = temp
            f = (c * 9/5) + 32
            k = c + 273.15
        elif unit == "F":
            f = temp
            c = (f - 32) * 5/9
            k = (f - 32) * 5/9 + 273.15
        elif unit == "K":
            k = temp
            c = k - 273.15
            f = (k - 273.15) * 9/5 + 32
        else:
            print("Invalid unit. Please enter C, F, or K.")
            return

    except ValueError:
        print("Invalid input. Please enter a numeric value for temperature.")
        return

    # Prepare result string
    result = (
        "\nConverted Temperatures:\n"
        f"Celsius     : {c}\n"
        f"Fahrenheit  : {f}\n"
        f"Kelvin      : {k}\n"
        + "=" * 30 + "\n"
    )

    # Print to screen
    print(result)

    # Save to file
    with open("temperature_results.txt", "a") as file:
        file.write(f"Original Input: {temp} {unit}\n")
        file.write(result)

    print("Conversion saved to 'temperature_results.txt' successfully.")

# Run the converter
temperature_converter()
