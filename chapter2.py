# f = open("more_file")
# lines1 = f.readlines()
# print(lines1, type(lines1))


# lines2 = f.readlines()
# print(lines2, type(lines2))

# lines3 = f.readlines()
# print(lines3, type(lines3))

# f.close()



import random

def game():
    print("you are playing the game")

    score =  random.randint(1,40)

    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0    
    print(f"Your score is: {score}")
    if(score > hiscore):

        with open("hiscore.txt","w") as f:
            f.write(str(score))

    return score
game()