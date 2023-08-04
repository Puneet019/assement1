def calculate_trek_length(a, b, c):
    # Total length traveled by Amit, Suman, and Ravi
    total_length = (a + b) + (b + c) + (a + c)
    return total_length

def main():
    try:
        a = float(input("Enter the distance A "))
        b = float(input("Enter the distance B"))
        c = float(input("Enter the distance C "))
        
        total_trek_length = calculate_trek_length(a, b, c)
        print("Total length of trek traveled by all three:", total_trek_length, "meters")

    except ValueError:
        print("Invalid input. Please enter valid distances.")

if __name__ == "__main__":
    main()
