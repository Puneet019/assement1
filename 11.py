def two_sum(nums, target):
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index

    return []

def main():
    try:
        nums = [int(x) for x in input("Enter a list of integer numbers separated by spaces: ").split()]
        target = int(input("Enter the target sum: "))
        
        result = two_sum(nums, target)
        
        if result:
            print("Indices of the two numbers:", result)
        else:
            print("No solution found.")

    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()
