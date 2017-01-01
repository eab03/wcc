import random

# Get the user's guess
# Params: None
# Returns: Integer
#
def get_guess():

    # Get initial guess
    guess = raw_input('Enter your guess: ')

    # Assume it's not valid, until it's proven otherwise
    valid = False

    while valid != True:

        try:
            # Try and convert this number to an integer
            # If it fails, the exception will occur
            guess = int(guess)
        except Exception:
            # Exception was thrown when trying to convert to number,
            # Report the issue and ask again
            print('Invalid input; please enter a whole number.')
            valid = False
            guess = get_guess()

        # If they get here, it means the number must have been valid
        # Set valid to be true to break out of the while loop
        valid = True

    return guess

    # Test get_guess
#print get_guess() # Expected: Keeps prompting until user enters a valid number

#______________

def compare(numA, numB):
    if numA > numB:
        return 'high';
    else:
        return 'low'

# Test compare
#print compare(100,1)  # Expected: 'high'
#print compare(1,100)  # Expected: 'low'
#print compare(99,100) # Expected: 'low'

#______________

#
#
#
def play():

    # Pick a secret number
    secret_number = random.randint(1, 100)

    # When building your program, the following line will tell you what
    # the secret_number is; this will make it easier to test the game.
    # When done, remove or comment-out this line.
    print('TEMPORARY DEBUGGING HELPER -> The secret number is: ' + str(secret_number))

    # Print message at the start the game
    print("\nI'm thinking of a number between 1 and 100; what do you think it is?")

    guess = get_guess()

    # Keep prompting until they get it correct
    # For every failed attempt, print 'Too x. Guess again.' where x is either 'high' or 'low'

    #for count in range(4, 0, -1):
    #http://stackoverflow.com/questions/4767401/decrementing-for-loops

    for guess_count in range(0, 4):

        if guess == secret_number:
            break

        results = compare(guess, secret_number);

        guesses_left = 4 - guess_count;

        print('Too ' + results + ' you have ' + str(guesses_left) + ' guesses left')
        guess = get_guess()

# conclusion
    if guess == secret_number:
        print('You got it! The number was ' + str(secret_number))
    else:
        print('Sorry, you ran out of turns! The correct number was ' + str(secret_number))


# Run the game
play()
