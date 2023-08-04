def merge_lists_into_dict(keys, values):
    return dict(zip(keys, values))

def main():
    try:
        size = int(input("Enter the size of the lists: "))
        keys = []
        values = []

        print("Enter elements for the first list (unique elements):")
        keys = [input(f"Element {i+1}: ") for i in range(size)]

        print("Enter elements for the second list (same size as the first list):")
        values = [input(f"Element {i+1}: ") for i in range(size)]

        merged_dict = merge_lists_into_dict(keys, values)
        print("Merged Dictionary:", merged_dict)

    except ValueError:
        print("Invalid input. Please enter valid values.")

if __name__ == "__main__":
    main()
