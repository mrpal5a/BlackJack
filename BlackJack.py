import random
from art import logo
print(logo)
card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_card = []
def get_card():
    random_card = random.choice(card_list)
    user_card.append(random_card)
get_card()
get_card()
user_sum = 0
def result():
    if user_sum > 21:
        print("Black Jack")
    elif user_sum > computer_sum:
        print("You won")
    elif user_sum == computer_sum:
        print("Game draw")
    else:
        print("You lose")
def sum():
    global user_sum
    user_sum = 0
    length = len(user_card)
    for i in range(length):
        first = user_card[i]
        user_sum += first
    print(f"user cards are {user_card}")
    print(f"The sum of user cards are {user_sum}")

length = len(user_card)
for i in range(length):
    first = user_card[i]
    user_sum += first
print(f"user cards are {user_card}")
print(f"The sum of user cards are {user_sum}")
computer_hand = []
def computer_card():
    rand_card = random.choice(card_list)
    computer_hand.append(rand_card)
computer_card()
computer_card()
lengths = len(computer_hand)
def computer_total():
    computer_sum = 0
    for i in range(lengths):
        card = computer_hand[i]
        computer_sum += card
    return computer_sum
computer_sum = computer_total()
# print(f"computer cards are {computer_hand}")
# print(f"The sum of computer cards are {computer_sum}") 
isgame = True
while isgame:
    insert = input("Type 'yes' for picking another card or type 'no' to stand ").lower()
    if insert == "yes":
        get_card()
        sum()
        if user_sum > 21:
            result()
            isgame = False
        else:
            isgame = True
    else:
        result()
        print(f"The sum of user cards are {user_sum}")
        print(f"The sum of computer cards are {computer_sum}") 
        isgame = False
