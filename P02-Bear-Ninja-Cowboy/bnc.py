from random import randrange

roles = {'bear':0, 'ninja':0, 'cowboy':0} #adds number of times picked to calculate weighted average
weights = {'bear':1/3, 'ninja':1/3, 'cowboy':1/3} #the weight for each pick
total = 0

#index value for role list
bear = 0
ninja = 1
cowboy = 2

roleList = list(roles.keys())

cpuChoice = ""
playerChoice = ""

#calculates weight/odds of being picked
def calcWeight():
    cpuChoice = ""
    playerChoice = ""
    for i in range(len(roleList)):
        weights[roleList[i]] = (1 + roles[roleList[i]]/total)/weights[roleList[i]]


def roundOver(playerWin, cpuChoice):
    if playerWin:
        print(cpuChoice)
        roles[cpuChoice] -= 1
        print(f"{playerChoice} beats {cpuChoice}")
    else:
        roles[cpuChoice] += 1
        print(f"{cpuChoice} beats {playerChoice}")

    calcWeight()

playing = True

while playing:
    print(f"weights: bear {weights['bear']}, ninja {weights['ninja']}, cowboy {weights['cowboy']}") 
    cpuNum = float(randrange(start=0, stop=100)/100)
    print(cpuNum)
    if cpuNum <= weights[roleList[bear]]:
        cpuChoice = roleList[bear]
    elif cpuNum > weights[roleList[bear]] and cpuNum <= weights[roleList[ninja]]+1/3:
        cpuChoice = roleList[ninja]
    elif cpuNum > weights[roleList[ninja]]+1/3 and cpuNum <= weights[roleList[cowboy]]+2/3:
        cpuChoice = roleList[cowboy]

    player = input('enter "b" for bear, "n" for ninja, and "c" for cowboy. type "done" to quit: ')

    if player.lower() == "b":
        playerChoice = roleList[bear]
        print(f"your choice is {playerChoice}")
    elif player.lower() == "n":
        playerChoice = roleList[ninja]
        print(f"your choice is {playerChoice}")
    elif player.lower() == "c":
        playerChoice = roleList[cowboy]
        print(f"your choice is {playerChoice}")
    elif player.lower() == "done":
        playing = False
    else:
        print("pleaes enter a valid input")
        continue
    
    total += 1

    if playerChoice == cpuChoice:
        print("Tie!")
    elif playerChoice == roleList[bear]:
        if cpuChoice == roleList[cowboy]:
            roundOver(False, cpuChoice)
        else:
            roundOver(True, cpuChoice)
    elif playerChoice == roleList[ninja]:
        if cpuChoice == roleList[bear]:
            roundOver(False, cpuChoice)
        else:
            roundOver(True, cpuChoice)
    elif playerChoice == roleList[cowboy]:
        if cpuChoice == roleList[ninja]:
            roundOver(False, cpuChoice)
        else:
            roundOver(True, cpuChoice)
            

