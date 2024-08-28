import random

print("Winning Rules for the Game:- \n \n 1. ROCK vs PAPER --> PAPER \n 2. PAPER vs SCISSOR --> SCISSOR \n 3. PAPER vs ROCK --> ROCK")
print(' ')

while True:
    print('------------------------------------------------------------------------')
    print('Enter the choice:- \n 1 - ROCK \n 2 - PAPER \n 3 - SCISSOR')

    choice = int(input('Enter your choice: '))
    print(' ')

    while choice >3 or choice <1:
        choice = int(input('Invalid Choice :( \n Please Enter valid choice: '))
        print(" ")

    if choice == 1:
        choicename = 'ROCK'
    elif choice == 2:
        choicename = 'PAPER'
    else:
        choicename = 'SCISSOR'

    print('You Choose', choicename)
    print(" ")
    print('Now its Computer Turn...')
    print(' ')
    
    comp_choice = random.randint(1,3)

    if comp_choice == 1:
        comp_choicename = 'rock'
    elif comp_choice == 2:
        comp_choicename = 'paper'
    else:
        comp_choicename = 'scissor'
        
    print('Computer Choose:',comp_choicename)
    print(" ")

    if choice == comp_choice:
        result = 'DRAW'  
    if choice == 1 and comp_choice == 2:
        result = 'Computer Win'
    elif choice == 2 and comp_choice == 1:
        result = 'You Win'
    elif choice == 2 and comp_choice == 3:
        result = 'Computer Win'
    elif choice == 3 and comp_choice == 2:
        result = 'You Win'
    elif choice == 1 and comp_choice == 3:
        result = 'You Win'
    elif choice == 3 and comp_choice == 1:
        result = 'Computer Win' 
        
    print(choicename ,"V/S", comp_choicename )
    print('Winner of the game is:',result)
    print(" ")
    
    ans = input("Do you want to play again!(y/n): ")
    if ans == 'n':
        break
        
print('------------------------------------------------------------------------')
print("Thanks for Playing :) GG ")
