def main():
    print("This program will convert Fahrenheit to Celsius.")
    fahrenheit = float(input("Enter the temprature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5.0/9.0
    print(f"The temperature in Celsius is: {celsius}")
if __name__ == '__main__':
    main()
