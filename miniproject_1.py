import random
def play_game():
    while True:
        number=random.randint(1,100)
        max_attempts=7
        attempts=0
        while attempts < max_attempts:
            try:
                guess=int(input("enter a number between 1 to 100"))
            except ValueError:
                print("please enter a valid number!!")
                continue
            if guess == number:
                print("you won the number is correct!")
                break
            elif guess < number:
                print("too low")
            else:
                print("too high")
            attempts +=1
            print(f"Attempts left: {max_attempts-attempts}")
        if attempts == max_attempts:
                print(f"game over! the number is {number}")
        play_again=input("do you want play again(yes/no)").lower()
        if play_again != "yes":
            print("thank you ! byee")
            break
play_game()
