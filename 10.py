
def prodDigits(number):
    product = 1
    while number > 0:
        digit = number % 10
        product *= digit
        number //= 10
    return product

def MDR(number):
    while number >= 10:
        number = prodDigits(number)
    return number

def MPersistence(number):
    persistence = 0
    while number >= 10:
        number = prodDigits(number)
        persistence += 1
    return persistence

def main():
    try:
        num = int(input("Enter a number: "))
        mdr_result = MDR(num)
        mpersistence_result = MPersistence(num)
        
        print(f"Multiplicative Digital Root (MDR) of {num}: {mdr_result}")
        print(f"Multiplicative Persistence of {num}: {mpersistence_result}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
