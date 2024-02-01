playing = input("Do you want to play? ")
if playing != "yes":
    quit()
    print("Okay, let's play!")
score = 0
answer = input("What is the full form of CPU? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Thats incorrect!")
answer = input("What is the full form of GPU? ")
if answer.lower() == "graphics processing unit":
    print("thats right!")
    score += 1
else:
    print("thats incorrect")
answer = input("What is the full form of ROM? ")
if answer == "read only memory":
    print("you got it right")
    score += 1
else:
    print("thats wrong")
print("you got " + str(score) + " questions right")
print("you've scored a percentile of " + str((score/3) * 100) + "%.")





