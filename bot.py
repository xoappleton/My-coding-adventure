# creating variables which will store info about our bot and greeting phrases
bot_name = "Spermobak"
creation_year = "1984"
print(f"Hello! My name is {bot_name}.")
print(f"I was created in {creation_year}.")
print("Please, remind me your name.")
# taking input from the user and greeting him by name
user_name = input()
print(f"What a great name you have, {user_name}")
# playing a game with a user in which bot guesses his age
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {age}; that's a good time to start programming!")
# showing our user some more tricks with a while cycle
print("Now I will prove to you that I can count to any number you want.")
number_input = int(input())
i = 0
while i <= number_input:
    print(f"{i} !")
    i += 1
print("Completed, have a nice day!")
# Challenging our user with a quiz
quiz = ["To repeat a statement multiple times", "To decompose a program into several small subroutines", "To determine the execution time of program", "To interrupt the execution of a program"]
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1.", quiz[0], "?")
print("2.", quiz[1], "?")
print("3.", quiz[2], "?")
print("4.", quiz[3], "?")


def test():
    answr_input = int(input())
    if answr_input == 2:
        print("Completed, have a nice day!")
    if answr_input != 2:
        print("Please, try again")
        print(test())  # a function which will take answer input from user and repeat it if the answer is incorrect


test()
print("Congratulations, have a nice day!")
