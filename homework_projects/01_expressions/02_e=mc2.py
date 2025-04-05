C: int = 299792458 

def main():
    mass_in_kg: float = float(input("Enter mass in kg: "))
    energy_in_joules: float = mass_in_kg * (C ** 2)
    print("Solution:")
    print("m = "+ str(mass_in_kg)+ " kg") 
    print("C = "+ str(C)+ " m/s")

    print("By using Einstein's Mass energy equivalence formula:")
    print("e = mC^2...")
    print(str(energy_in_joules) + " joules of energy!")

if __name__ == "__main__":
    main()