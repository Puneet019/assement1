def Primecheck(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def twinPrime():
    twin_primes = []
    for num in range(3, 1000, 2):
        if Primecheck(num) and Primecheck(num + 2):
            twin_primes.append((num, num + 2))
    return twin_primes

def main():
    try:
        twin_prime_list = twinPrime()
        
        print("Twin Primes less than 1000:")
        for twin in twin_prime_list:
            print(twin[0], "and", twin[1])

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
