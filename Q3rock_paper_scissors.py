from random import randint

def win():
    print('you win!')

def lose():
    print('you lose!')

i=True

while i:

    player_choice=input('What do you pick? (rock,paper,scissors):')

    random_move=randint(0,2)

    moves=['rock','paper','scissors']

    computer_choice= moves[random_move]

    if player_choice==computer_choice:
        print("Draw!")
        i=False
    elif player_choice=='rock' and computer_choice=='scissors':
        win()
        i=True
    elif player_choice=='paper' and computer_choice=='scissors':
        win()
        i=False
    elif player_choice == 'scissors' and computer_choice == 'paper':
        lose()
        i=True
    elif player_choice == 'scissors' and computer_choice == 'rock':
        lose()
        i=False
    elif player_choice == 'paper' and computer_choice == 'rock':
        win()
        i=True
    elif player_choice == 'rock' and computer_choice == 'paper':
        win()
        i=False
    aGain = input('Do you want to play again? (yes or no)').strip()
    if aGain == 'yes':
        print('continue your game')
        i=True
    else:
        print("game over")
        i=False
   


        
        
