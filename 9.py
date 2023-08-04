def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def permutations(n, r):
    return factorial(n) // factorial(n - r)

def combinations(n, r):
    return permutations(n, r) // factorial(r)

def main():
    try:
        n = int(input("Enter the value of n: "))
        r = int(input("Enter the value of r: "))
        
        if n < 0 or r < 0:
            print("n and r must be non-negative numbers.")
        elif n < r:
            print("n must be greater than or equal to r.")
        else:
            p = permutations(n, r)
            c = combinations(n, r)
            
            print(f"Number of permutations of {n} objects taken {r} at a time (p({n}, {r})): {p}")
            print(f"Number of combinations of {n} objects taken {r} at a time (c({n}, {r})): {c}")

    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()
