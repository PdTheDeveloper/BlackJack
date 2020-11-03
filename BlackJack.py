import random

class Card:
    def __init__(self,shape,num,visiblity=True):
        self.shape=shape
        self.num=num
        self.visiblity=visiblity


    def __str__(self):
        if self.visiblity:
            return f"{str(self.num)} of {self.shape}s"
        else:
            return "????"

    def show(self):
        self.visiblity=True

    def hide(self):
        self.visiblity =False

    def value(self):
        global nums
        return nums[self.num]


class Deck:
    def __init__(self,cards):
        self.count=len(cards)
        self.cards=cards
        self.sum=0
        self.acesDone=0
        for card in self.cards:
            self.sum+=card.value()

    def __str__(self):
        return f"A deck with {self.count} cards"

    def add(self,card):
        self.cards.append(card)
        self.sum+=card.value()

    def draw(self,deck):
        randomCard=random.choice(self.cards)
        self.cards.remove(randomCard)
        deck.add(randomCard)

    def show(self):
        for x in range(len(self.cards)):
            print(f"{x+1}. {self.cards[x]}")

    def aceMove(self):
        while self.aces()>self.acesDone and self.sum>21:
            self.sum-=10
            self.acesDone+=1

    def aces(self):
        a=0
        for card in self.cards:
            if card.value()==11:
                a+=1
        return a

    def showCard(self,position):
        self.cards[position-1].show()

    def hideCard(self,position):
        self.cards[position-1].hide()


#Globals
playerMoney=500
bet=0
dealerIsBusted=False
gamblerIsBusted=False

nums={"Ace":11,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,"Jack":10,"Queen":10,"King":10}
types=["Heart","Diamond","Club","Spade"]

fullDeck=None
fullCards=[]
for i in nums:
    for t in types:
        fullCards.append(Card(t, i))

dealerDeck=None
gamblerDeck=None
gamblerIsDone=False



def addMoney(amount):
    global playerMoney
    playerMoney+=amount

def bust(deck):
    global gamblerIsDone,gamblerIsBusted,dealerIsBusted
    if gamblerIsDone:
        dealerIsBusted=True
        win()
    else:
        gamblerIsBusted=True
        lose()

def playOrNot():
    while True:
        try:
            choice = input("Do you wanna play again? Y for yes and N for no :")
        except:
            print("\nInvalid choice! Try again :\n")
            continue
        if choice=="Y" or choice=="N":
            return choice
            break
        else:
            print("\nInvalid choice! Try again :\n")


def win():
    global bet,playerMoney
    playerMoney+=bet
    updateTable()
    if dealerIsBusted:
        print("\nDealer is Busted!")
    print(f"\nYou won {bet}$ and now you have {playerMoney}$\n")
    choice=playOrNot()
    if choice=="Y":
        init()
    else:
        exit()

def lose():
    global bet,playerMoney,gamblerIsDone
    playerMoney-=bet
    gamblerIsDone=True
    updateTable()
    if gamblerIsBusted:
        print("\nGambler is Busted!")
    print(f"\nYou lost {bet}$ and now you have {playerMoney}$\n")
    choice=playOrNot()
    if choice=="Y":
        init()
    else:
        exit()


def stay():
    global gamblerIsDone,gamblerDeck,dealerDeck
    gamblerIsDone=True
    dealerDeck.showCard(2)
    if dealerDeck.sum>gamblerDeck.sum:
        updateTable()
        win()
    else:
        hit()


def hit():
    global gamblerDeck,dealerDeck,gamblerIsDone
    if not gamblerIsDone:
        fullDeck.draw(gamblerDeck)
        if gamblerDeck.sum>21:
            gamblerDeck.aceMove()
        if gamblerDeck.sum>21:
            bust(gamblerDeck)
            gamblerIsDone=True
        else:
            updateTable()
    else:
        if dealerDeck.sum>gamblerDeck.sum:
            lose()
        else:
            fullDeck.draw(dealerDeck)
            if dealerDeck.sum > 21:
                dealerDeck.aceMove()
            if dealerDeck.sum > 21:
                bust(dealerDeck)
            else:
                updateTable()
            if dealerDeck.sum>gamblerDeck.sum:
                lose()
            else:
                hit()




def resetCards():
    global fullCards,fullDeck
    random.shuffle(fullCards)
    fullDeck=None
    fullDeck=Deck(fullCards)

def init():
    global dealerDeck,gamblerDeck,fullDeck,playerMoney,bet,gamblerIsDone,gamblerIsBusted,dealerIsBusted
    gamblerIsBusted=False
    dealerIsBusted=False
    gamblerIsDone = False
    print(35*"\n")
    while True:
        try:
            bet=int(input(f"How much do you wanna gamble? (You have {playerMoney}$)\n"))
        except:
            print("\nInvalid bet! Try again :\n")
            continue
        if bet<=playerMoney:
            break
        else:
            print("\nNot enough money! Try again :\n")
            continue
    resetCards()
    dealerDeck = None
    gamblerDeck = None
    dealerDeck=Deck([])
    gamblerDeck = Deck([])
    for x in range(2):
        fullDeck.draw(dealerDeck)
        fullDeck.draw(gamblerDeck)
    dealerDeck.hideCard(2)
    updateTable()



def updateTable():
    global gamblerDeck,dealerDeck,gamblerIsDone
    print(35*"\n")
    print("You :\n\n")
    gamblerDeck.show()
    print("\n-----------------------------------------------------\n\nDealer:\n")
    dealerDeck.show()
    if not gamblerIsDone:
        while True:
            try:
                choice=int(input("\nDo you wanna hit or stay? 1 for hit and 2 for stay\n"))
            except:
                print("\nInvalid choice! Try again:")
                continue
            if choice==1 or choice==2:
                if choice==1:
                    hit()
                    break
                else:
                    stay()
                    break
            else:
                print("\nInvalid choice! Try again:")
                continue


init()
