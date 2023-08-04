def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_of_list(numbers):
    if len(numbers) < 2:
        raise ValueError("The list must contain at least 2 numeric values.")

    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
    
    return result

def main():
    try:
        input_list = [int(x) for x in input("Enter a list of numeric values separated by spaces: ").split()]

        result = gcd_of_list(input_list)
        print("Greatest Common Divisor (GCD):", result)

    except ValueError as ve:
        print(ve)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
