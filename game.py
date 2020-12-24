from art import logo
from random import randint as r
from replit import clear
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def game():
    first = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if first == "y":
        clear()
        print(logo)
    else:
        print("*****Thank You for play with Us. GoodBye!*****")
        return "END"
    player = []
    comp = []
    comp.append(cards[r(0,12)])
    player.append(cards[r(0,12)])
    player.append(cards[r(0,12)])
    print(f"    Your cards: {player}, current score: {sum(player)}")
    print(f"    Computer's first card: {comp[0]}")
    #Player game
    if sum(player) != 21:
        x = input("Type 'y' to get another card, type 'n' to pass: ")
    else:
        x = "n"
    while x == "y" and sum(player) < 21:
        player.append(cards[r(0,12)])
        if (11 in player) and sum(player) > 21:
            i = player.index(11)
            player.remove(11)
            player.insert(i, 1)
        print(f"    Your cards: {player}, current score: {sum(player)}")
        print(f"    Computer's first card: {comp[0]}")
        if sum(player) < 21:
            x = input("Type 'y' to get another card, type 'n' to pass: ")


    print(f"    Your final hand: {player}, final score: {sum(player)}")
    #Computer game
    while (sum(comp) < 21) and (sum(comp) < sum(player)):
        comp.append(cards[r(0,12)])
        if (11 in comp) and sum(comp) > 21:
            j = comp.index(11)
            comp.remove(11)
            comp.insert(j, 1)

    print(f"    Computer's final hand: {comp}, final score: {sum(comp)}")
    #Who is the Winner?
    if sum(player) == 21:
        print("Win with a Blackjack 😎")
    elif (sum(player) > sum(comp)) and (sum(player) < 22):
        print("You win 😃")
    elif (sum(player) < 22) and (sum(comp) > 21):
        print("You win 😃")
    elif sum(player) == sum(comp) and (sum(player) < 22):
        print("Draw 🙃")
    elif sum(player) < sum(comp) and sum(comp) < 22:
        print("You lose 😤")
    else:
        print("You went over. You lose 😭")
    game()

game()
