def avg(a:float, b:float):
    sum = a + b
    return sum / 2

def main():
    avg1 = avg(1.0, 2.0)
    avg2 = avg(3.0, 4.0)
    final = avg(avg1, avg2)
    print(f"Final average: {final}")
    print(f"Average of 1.0 and 2.0: {avg1}")
    print(f"Average of 3.0 and 4.0: {avg2}")
    print(f"Final Average of {avg1} and {avg2}: {final}")

if __name__ == "__main__":
    main()