guess = 50
high = 100
low = 0

print('Please think of a number between 0 and 100!')
print('Is your secret number ' + str(guess) + ' ?')
ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

while ans != 'c':
    if ans != 'h' and ans != 'l' and ans != 'c':
        print('Sorry, I did not understand your input.')
        print('Is your secret number ' + str(guess) + ' ?')
        ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    else:
        if ans == 'h':
            high = guess
            guess = int((high + low)/2)
        else:
            low = guess
            guess = int((high + low)/2)
        print('Is your secret number ' + str(guess) + ' ?')
        ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

print('Game over. Your secret number was: '+str(guess))
