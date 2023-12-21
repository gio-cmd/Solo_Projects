percenatge = 0
score = 0

print("Welcome! This is words best quiz game")
 
game = input ("Do you want to play?: ")
if game.lower() != "yes":
    quit()
print("Good Choice")

anwer = input("what year is this: ")
if anwer == 2023:
    print("Correct")
    score += 1
    percenatge += 25
else:
    print("Wrong")
    score -= 1

anwer = input("What is the capital of France?: ")
if anwer.lower() == "paris":
    print("Correct")
    score += 1
    percenatge += 25
else:
    print("Wrong")
    score -= 1

anwer = input("What is the output of 'print("Hello" + "World")': ")
if anwer.lower() == "hello world":
    print("Correct")
    score += 1
    percenatge += 25
else:
    print("Wrong")
    score -= 1



anwer = input("Which programming language is known for its readability and simplicity?: ")
if anwer.lower() == "python":
    print("Correct")
    score += 1
    percenatge += 25
else:
    print("Wrong")
    score -= 1

print("your total score is ", score, "points")
print("Out of this questions you got",percenatge,"procent correct")
