import random

# Set up                                      J   Q   K   A
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

#print(cards) # To see the list before being shuffled

random.shuffle(cards)

#print(cards) # To see the list after being shuffled

# Round 1
player_card1 = cards.pop()
computer_card1 = cards.pop()

print('Player Card: ' + str(player_card1))
print('Computer Cards: ' + str(computer_card1))

# Round 2
decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')

if decision == 'h':
    player_card2 = cards.pop()
    computer_card2 = cards.pop()
else:
    player_card2 = 0
    computer_card2 = cards.pop()

    print('Your Cards: ' + str(player_card1) + ', ' + str(player_card2))
    print('Computer Cards:  ' + str(computer_card1) + ', ' + str(computer_card2))

# Round 3
decision = raw_input('\nIf you want to stay type `s`, if you want to hit type `h`: ')

if decision == 'h':
    player_card3 = cards.pop()
else:
    player_card3 = 0

computer_total = computer_card1 + computer_card2
if computer_total <= 16:
    computer_card3 = cards.pop()
else:
    computer_card3 = 0

print('Your Cards: ' + str(player_card1) + ', ' + str(player_card2) + ', ' + str(player_card3))
print('Computer Cards:  ' + str(computer_card1) + ', ' + str(computer_card2) + ', ' + str(computer_card3))

#Results

print ('')

player_final = player_card1 + player_card2 + player_card3
computer_final = computer_card1 + computer_card2 + computer_card3

print('\nGame Over'+ '\nPlayer Total: ' + str(player_final) + '\nComputer total: ' + str(computer_final))

# Conclusion

if player_final > 21 and computer_final > 21:
    print('Tie! You both busted!')
elif player_final == computer_final and player_final <=21 and computer_final <=21:
    print ('Tie!!')
elif player_final <=21 and computer_final >21:
    print ('You Won!')
elif computer_final <= 21 and player_final <= 21 and player_final > computer_final:
    print('You Won!')
elif computer_final <= 21 and player_final <= 21 and computer_final > player_final:
    print('Computer Won!')
else:
    print('')
