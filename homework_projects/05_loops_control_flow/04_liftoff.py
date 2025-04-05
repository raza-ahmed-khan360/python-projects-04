import time
def main():
    for i in range(10):
        print(str(10 - i) + "...")
        time.sleep(1)
    print("Liftoff!")

if __name__ == "__main__":
    main()