import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!"
    elif user_score == 0:
        return "You got a blackjack, You Win!"
    elif computer_score == 0:
        return "Computer got a blackjack, You Lose!"
    elif user_score > 21:
        return "You went over, You Lose!"
    elif computer_score > 21:
        return "Computer went over, You Win!"
    elif user_score > computer_score:
        return "You Win!"
    elif computer_score > user_score:
        return "You Lose!"


def game_play():
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    game_over = False
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"User Cards: {user_cards} User Score: {user_score}")
        print(f"Computer Card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            go_again = input("Do you want another cards Type 'y' or 'n'? ")
            if go_again == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
        print(f"Computers final card: {computer_cards} Sum: {computer_score}")
        print(compare(user_score, computer_score))


while input("Do you want to play a game of blackjack? Type 'y' or 'n' ") == 'y':
    game_play()





















