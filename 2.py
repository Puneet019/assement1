def conversion(paragraph):
    words = paragraph.split()
    filtered_words = [word for word in words if len(word) > 4]
    return filtered_words

def main():
    try:
        paragraph = input("Enter a paragraph: ")
        word_list = conversion(paragraph)
        
        if word_list:
            print("Words with more than 4 letters:", word_list)
        else:
            print("No words with more than 4 letters found.")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
