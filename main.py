import random
from time import sleep


def computer_guess(x):
    low = 1
    high = x
    user_guess = random.randint(low, high)
    guess = random.randint(low, high)
    while user_guess != guess:
        print(f'Seu número é {guess}')
        if guess >= high / 2 and guess <= high and user_guess <= high / 2 :
            print('Erooou, seu número ainda está muito alto\n')
            guess = random.randint(1, high / 2)
            sleep(1)
        elif guess >= high / 2 and guess <= high and user_guess >= high / 2 :
            print('Ta perto, continua que você chega lá pczin top\n')
            guess = random.randint(high / 2, high)
            sleep(1)
        elif guess <= high / 2 and guess >= low and user_guess >= high / 2:
            print('Erooou, seu número ainda está muito baixo\n')
            guess = random.randint(high / 2, high)
            sleep(1)
        elif guess <= high / 2 and guess >= low and user_guess <= high / 2:
            print('Ta perto, continua que você chega lá pczin top\n')
            guess = random.randint(1, high / 2)
            sleep(1)
    print(f'Aee Caraio, acertou!! \n \
            O numéro escolhido foi o {user_guess} ')

computer_guess(random.randint(10, 100))