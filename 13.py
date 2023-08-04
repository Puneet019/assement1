#1.The type of values returned by the nextCard function is a tuple containing two elements: the next card (integer) and the new hand (list of integers).
#2. The nextCard function takes a list of cards as input. It returns a tuple containing the first card from the input list as the "next" card, and a new hand formed by moving the first card to the end of the list.
#3 a loop that calls the nextCard function repeatedly and prints out the card from the top of the deck each time

cards = [1, 5, 3, 4, 2, 3, 2]

for _ in range(len(cards)):
    next_card, cards = nextCard(cards)
    print("Next card:", next_card)
#program that uses the nextCard function to check a deck of cards
    def check_for_pairs(cards):
    for i in range(len(cards) - 1):
        if cards[i] == cards[i + 1]:
            return True
    return False

cards = [1, 5, 3, 4, 2, 2, 3]

if check_for_pairs(cards):
    print("Consecutive identical pair found.")
else:
    print("No consecutive identical pairs found.")
