import random 

c = random.randint(1,100)
print()
print('''The computer is thinking of a number
between 1 and 100.''')
print()

print('''You have to challenge the computer that you 
can guess the number in say x number of tries. ''')
print()

x = int(input("How many tries do you want to bet on? "))
y = 1
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
        print("Run script to play again.")
        print()
        break  

    y += 1

else:
    print()
    print("GAME OVER.")
    print("The computer guessed: %d" %c)
    print("The computer defeated you.")
    print("Run script to play again.")
    print()
