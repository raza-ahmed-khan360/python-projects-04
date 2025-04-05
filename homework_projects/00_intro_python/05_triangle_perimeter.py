def main():
    print("This program will calculate the perimeter of a triangle.")
    one_side = float(input("Enter the length of the first side:"))
    second_side = float(input("Enter the length of the second side:"))
    third_side = float(input("Enter the length of the third side:"))
    perimeter = one_side + second_side + third_side
    print(f"The perimeter of the triangle is: {perimeter}")

if __name__ == '__main__':
    main()     