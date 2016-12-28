import random

# Parameters: a String `move`
# Returns: Boolean for whether move is valid
#
# Valid moves include 'rock', 'paper', or 'scissors'`
#
def check_move(move):

    # YOUR CODE GOES HERE
    if move == 'rock':
        return True
    if move == 'paper':
        return True
    if move == 'scissors':
        return True
    else:
        return False

# Test the check_move function
#print check_move('rock') # Expects: True
#print check_move('paper') # Expects: True
#print check_move('scissors') # Expects: True
#print check_move('roc') # Expects: False
#print check_move(1) # Expects: False

# This function is provided; no edits are needed.
# Parameters: None
# Returns: String of 'rock', 'paper', or scissors'
# Prompts the user for a move
# Makes sure that move is valid; if it's not, continues to ask user for a move
def get_player_move():

    # Prompt the user to enter their move
    move = raw_input('Pick your move: rock, paper, or scissors? ')

    # This will happen on a loop until the user enters a valid move
    while check_move(move) == False:
        print('Invalid move; pick again.')
        # Run this function again, so they're asked to enter a new move
        move = get_player_move()

    # If they get out of the while loop, it means they
    # entered a valid move, so return it
    return move

# Test this function
#print 'You picked: ' + get_player_move()

# This function is provided; no edits are needed
# Parameters: None
# Returns: String of 'rock', 'paper', or 'scissors'
def get_computer_move():
    moves = ['rock', 'paper', 'scissors'];
    return random.choice(moves)

#print get_computer_move() # Expected: 'rock', 'paper', or 'scissors'
#print get_computer_move() # Expected: 'rock', 'paper', or 'scissors'
#print get_computer_move() # Expected: 'rock', 'paper', or 'scissors'

# Parameters: String moveA, String moveB
# Returns: Boolean if moveA beats moveB according to the rules of RPS
#
# Examples:
# If moveA is 'rock' and moveB is 'paper', it should return False
# If moveA is 'paper' and moveB is 'rock', it should return True
#
# Should work for 6 different possible combinations of moveA and moveB
# Will not be concerned with ties; i.e, moveA will never be the same as moveB
def judge(moveA, moveB):

    # YOUR CODE HERE
    if moveA == 'rock' and moveB == 'paper':
        return False
    if moveA == 'paper' and moveB == 'scissors':
        return False
    if moveA == 'scissors' and moveB == 'rock':
        return False
    else:
        return True

#print judge('rock','paper') # Expected: False
#print judge('rock','scissors') # Expected: True
#print judge('paper','rock') # Expected: True
#print judge('paper','scissors') # Expected: False
#print judge('scissors','rock') # Expected: False
#print judge('scissors','paper') # Expected: True

def play():

    print('Welcome to Welcome to Rock, Paper, Scissors!')

    # Player goes
    # ???
    player = get_player_move()
    check_move(get_player_move)

    # Computer goes
    # ???
    computer = get_computer_move()

    print('The computer picked: ' + computer)

    # Figure out who won
    # Print results; either: `Tie`, `You Won!`, or `The computer won.`
    # ???

# Stolen from WCC
    if player == computer:
        print('Tie!')
    elif(judge(player, computer) == True):
        print('You won!')
    else:
        print('The computer won!')

    # Prompt to play again
    play_again = raw_input('Play again? Type `y` or `n`: ')

    if(play_again == 'y'):
        play()
    else:
        print('Thanks for playing!')

# Run the game
play()
