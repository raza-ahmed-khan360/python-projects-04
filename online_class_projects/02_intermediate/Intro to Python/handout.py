def main():
    gravity = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    try:
        earth_weight = float(input("Enter a weight on Earth: "))
    except ValueError:
        print("Invalid weight. Please enter a number.")
        return

    planet = input("Enter a planet: ")

    multiplier = gravity.get(planet)
    if multiplier is None:
        print("Planet not recognized.")
        return

    planetary_weight = round(earth_weight * multiplier, 2)
    print(f"The equivalent weight on {planet}: {planetary_weight}")

if __name__ == "__main__":
    main()