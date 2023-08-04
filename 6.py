def even(input_list):
    return [x for x in input_list if x % 2 == 0]

def odd(input_dict):
    return {key: value for key, value in input_dict.items() if value % 2 != 0}

def main():
    try:
        # Example 
        numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # Example 
        numbers_dict = {
            'a': 11,
            'b': 12,
            'c': 13,
            'd': 14,
            'e': 15
        }

        even_filtered_list = even(numbers_list)
        odd_filtered_dict = odd(numbers_dict)

        print("Even filtered list:", even_filtered_list)
        print("Odd filtered dictionary:", odd_filtered_dict)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
