import random
n = random.randint(1,100)

guess = int(input("Enter any number between1 to 99: "))

while n != guess:
    if guess<n:
        print("Guess is low try longer")
        guess = int(input("Enter any number between1 to 99: "))
    elif guess>n:
        print("Guess is high")
        guess = int(input("Enter any number between1 to 99: "))
    else:
        print("Congrats you've got the number!")
        break
    print(" ")
