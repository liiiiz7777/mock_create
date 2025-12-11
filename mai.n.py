import random

while True:
    print('Welcome to this number guessing game!')
    n = int(input('Please enter an positive non-zero integer!'))
    print('You are going to guess a number between 0 and the number you just entered')

    answer= []
    def answer_generation(number):
        for i in range(0, number+1, 1):
            answer.append(i)
    answer_generation(n)

    a = random.choice(answer)

    guess= input('Take a guess:')
    if guess > a:
          print('The number is between 0 and', guess)
    elif guess < a:
          print(
    

    
    
    play_again = input('play again? (yes/no)')
    while play_again not in ('yes', 'no'):
            play_again = input('please type yes or no')
    if play_again == 'no':
            print('thanks for playing!')
            break