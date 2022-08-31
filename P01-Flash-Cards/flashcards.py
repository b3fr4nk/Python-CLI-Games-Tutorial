import json

score = 0
numCorrect = 0

with open("me-capitols.json", "r") as f:
    data = json.load(f)
    print(data)

cards = {}

for i in data["cards"]:
    cards[i['q']] = i['a']
print(cards.keys())

cardList = list(cards.keys())

play = True
while play:
    for i in range(len(cardList)):
        print(f"{i}. {cardList[i]}")
    qnum = input("Enter the question number you would like to answer: ")
    if qnum.isnumeric():
        qnum = int(qnum)
        if input(f"{cardList[qnum]}: ").lower() == cards[cardList[qnum]].lower():
            numCorrect += 1
            score += numCorrect
            print(f"Correct! You earned {numCorrect}. your score is now {score}")
        else:
            numCorrect -=1
            print(f"Incorrect, you have {2+numCorrect} more chances")
            if numCorrect < -1:
                play = input("you lose! would you like to play again? y/n").lower()
                if play == "y":
                    play = True
                elif play == "n":
                    play = False
                else:
                    print('Error, invalid input: Please enter either "y" or "n"')

    else:
        print("Error, not a whole number: please enter a whole number")
