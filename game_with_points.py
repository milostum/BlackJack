############### Blackjack Project #####################

from art import logo
from random import randint as r
from replit import clear
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_name = input("What's is your name? ")
player_points = 0
comp_points = 0

def game(player_points, comp_points):

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
        player_points += 1
    elif (sum(player) > sum(comp)) and (sum(player) < 22):
        print("You win 😃")
        player_points += 1
    elif (sum(player) < 22) and (sum(comp) > 21):
        print("You win 😃")
        player_points += 1
    elif sum(player) == sum(comp) and (sum(player) < 22):
        print("Draw 🙃")
    elif sum(player) < sum(comp) and sum(comp) < 22:
        print("You lose 😤")
        comp_points += 1
    else:
        print("You went over. You lose 😭")
        comp_points += 1
    return player_points, comp_points

new_game = True
while new_game:
    first = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if first == "y":
        clear()
        print(logo)
        player_points, comp_points = game(player_points, comp_points)
        print(f"You have {player_points} points and Computer has {comp_points} points.")
        if player_points == 10:
            print(f"*****Winner is {player_name}. Good Luck!*****")
            break
        elif comp_points == 10:
            print(f"*****Winner is Computer. Good Luck!*****")
            break
    else:
        print("*****Thank You for play with Us. GoodBye!*****")
        new_game = False
