def count(text, word):
    return text.lower().count(word)

def check_cat_dog(text):
    cat_count = count(text, "cat")
    dog_count = count(text, "dog")
    return cat_count == dog_count

def main():
    try:
        user_input = input("Enter a string: ")
        if check_cat_dog(user_input):
            print("True")
        else:
            print("False")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
