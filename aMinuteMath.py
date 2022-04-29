"""
This program challenges the user to a minute of math problems. The math problems consists of basic operations (+ - * /) wherein the 2 numbers will be randomly generated. If the user gets the answer correctly, they get a point. After one minute, the program will display how many correct answers the user got in terms of percentage

This program will be run on the terminal. Uses format print, while loop, if conditions, lists, exception handle, functions, time module, random module
"""

import random, time

# Randomly chooses a posible divisor for a given number to eliminate the chance of a ZeroDivision Error
def get_divisor(n):
    l = []
    for i in range(1, n+1):
        if n % i == 0:
            l.append(i)

    return random.choice(l)


# Chooses a random operator for the program
def operation():
    operators = ["+", "-", "*", "/"]
    randomOp = random.randint(0, 3)
    return operators[randomOp]

totalPoints = 0
userPoints = 0

timeStart = time.time()

# While the seconds is less than 60

while (time.time() - timeStart) <= 60:
    firstNumber = random.randint(1, 20)
    operator = operation()

    if operator == "/":
        secondNumber = get_divisor(firstNumber)
    else:
        secondNumber = random.randint(1, 20)

    correctAns = eval("{}{}{}".format(firstNumber, operator, secondNumber)) # Evaluates the correct answer

    # Getting User Input
    print(f"{firstNumber} {operator} {secondNumber} = ", end="")

    try:
        userInput = int(input())
    except:
        userInput = ""

    # Adds the total points/total number of questions
    totalPoints += 1

    # Check if the answer is correct
    if userInput == correctAns:
        userPoints += 1
        print("Correct! ", end="")
    else:
        print("Wrong answer! ", end="")
    
    print(f"Time remain: {(60 - (time.time() - timeStart)):.2f}s")

# Gets the correct rate of the user
correctRate = userPoints / totalPoints * 100

# Prints the final score
print(f"{totalPoints} questions. You got {correctRate:.2f}% correct.")

