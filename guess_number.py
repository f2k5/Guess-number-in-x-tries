import random 

while True:
    c = random.randint(1,100)

    #c     -> the numner the computer is thinking 
    #(x-y) -> number of guesses remaining
    #u     -> user's guesses
    #y     -> lives remaining
    #x     -> number of tries you want to bet on

    print()
    print('''The computer is thinking of a number
    between 1 and 100.''')
    print()

    print('''You have to challenge the computer that you 
    can guess the number in say x number of tries. ''')
    print()

    x = int(input("How many tries do you want to bet on? "))
    y = 1
    i = 0
    print_win_once_only = 0
    print()

    u = int(input("What number is the computer thinking? "))

    while x != y:

        if c != u and c > u:
            print()
            print(" ==================================== ")
            print("WRONG!")
            print("Hint: The number is higher!")
            print("Guess attempts remaining %d." %(x-y))
            print(" ==================================== ")
            print()
            u = int(input("Try again: "))
            

        elif c != u and c < u:
            print()
            print(" =================================== ")
            print("WRONG!")
            print("Hint: The number is lower!")
            print("Guess attempts remaining %d." %(x-y))
            print(" =================================== ")
            print()
            u = int(input("Try again: "))

        elif c == u:
            print()
            print("CORRECT!")
            print("The computer guessed %d." %c)
            print("You won with %d guesses to spare!" %(x-y))
            print()
            i += 1
            print_win_once_only += 1
            break  

        y += 1

    if c == u and (x-y)==1 and print_win_once_only == 0:
            print()
            print("CORRECT!")
            print("The computer guessed %d." %c)
            print("You won with only ONE guess to spare!")
            print()
            print("DAMN that was a close one!")
            print()
            i += 1
            break

    elif c != u and i:
        print()
        print("=========")
        print("GAME OVER.")
        print("=========")
        print("The computer guessed: %d" %c)
        print("You have run out of guesses.")
        print()
        print("The computer defeated you.")
        print()

    user_response = input("""Do you want to play again?
Press "y" for YES or "n" for NO: """)

    if user_response == "y" or "Y":
        continue
    elif user_response == "n" or "N":
        break

