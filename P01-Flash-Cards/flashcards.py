import json

score = 0
numCorrect = 0

#open and load json file
with open("me-capitols.json", "r") as f:
    data = json.load(f)

cards = {}

#initializes the data structure for the flash cards
for i in data["cards"]:
    cards[i['q']] = i['a']

#makes a list of keys for flashcards
cardList = list(cards.keys())

print("Welcome to flash cards! \nfor every question you get right you get points equal to your streak. your streak decreases by 1 if you get a question wrong. \nIf your streak is below zero you lose!")

#play loop
play = True
while play:
    #prints the questions
    for i in range(len(cardList)):
        print(f"{i}. {cardList[i]}")
    qnum = input("Enter the question number you would like to answer: ")
    #checks for valid input
    if qnum.isnumeric():
        qnum = int(qnum)
        #game logic
        #TODO no longer accept answering the same question twice
        if input(f"{cardList[qnum]}: ").lower() == cards[cardList[qnum]].lower():
            numCorrect += 1
            score += numCorrect
            print(f"Correct! You earned {numCorrect}. your score is now {score}")
        else:
            numCorrect -=1
            print(numCorrect)
            print(f"Incorrect, you have {2+numCorrect} more chances")
            if numCorrect < -1:
                play = input("you lose! would you like to play again? y/n").lower()
                numCorrect = 0
                if play == "y":
                    play = True
                elif play == "n":
                    play = False
                else:
                    print('Error, invalid input: Please enter either "y" or "n"')

    else:
        print("Error, not a whole number: please enter a whole number")
