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
            print(f"{x+1}. {self.cards[x]}\n")

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


    def sum(self):
        return self.sum

    def showCard(self,position):
        self.cards[position-1].show()

    def hideCard(self,position):
        self.cards[position-1].hide()



def addMoney(amount):
    global playerMoney
    playerMoney+=amount

def bust(deck):
    global gamblerIsDone
    if gamblerIsDone:
        print("Dealer Busted!")
        win()
    else:
        print("Gambler Busted!")
        lose()


#Globals
playerMoney=0
bet=0

nums={"Ace":11,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,"Jack":10,"Queen":10,"King":10}
types=["Heart","Diamond","Club","Spade"]

fullDeck=None
fullCards=[]
for i in nums.items():
    for t in types:
        fullCards.append(Card(t, i))

dealerDeck=None
gamblerDeck=None
gamblerIsDone=False

def stay():
    global gamblerIsDone
    gamblerIsDone=True

def hit():
    global gamblerDeck,dealerDeck,gamblerIsDone
    if not gamblerIsDone:
        fullDeck.draw(gamblerDeck)
        if gamblerDeck.sum()>21:
            gamblerDeck.aceMove()
        if gamblerDeck.sum()>21:
            bust(gamblerDeck)
        else:
            updateTable(dealerDeck,gamblerDeck)
    else:
        fullDeck.draw(dealerDeck)
        if dealerDeck.sum() > 21:
            dealerDeck.aceMove()
        if dealerDeck.sum() > 21:
            bust(dealerDeck)
        else:
            updateTable(dealerDeck, gamblerDeck)




def resetCards():
    global fullCards,fullDeck
    random.shuffle(fullCards)
    fullDeck=None
    fullDeck=Deck(fullCards)

def init():
    global dealerDeck,gamblerDeck,fullDeck,playerMoney,bet
    print(35*"\n")
    while True:
        try:
            bet=int(input("How much do you wanna gamble?\n"))
        except:
            print("\nInvalid bet! Try again :\n")
            continue
        if bet>playerMoney:
            playerMoney-=bet
            break
        else:
            print("\nNot enough money! Try again :\n")
    resetCards()
    dealerDeck = None
    gamblerDeck = None
    for x in range(2):
        fullDeck.draw(dealerDeck)
        fullDeck.draw(gamblerDeck)
    dealerDeck.hideCard(2)



def updateTable(dealerDeckP,gamblerDeckP):
    global gamblerDeck,dealerDeck,gamblerIsDone
    print(35*"\n")
    print("You :\n\n")
    gamblerDeck.show()
    print("\n-----------------------------------------------------\n\nDealer:\n\n")
    dealerDeck.show()
    if not gamblerIsDone:
        while True:
            try:
                choice=int(input("\nDo you wanna hit or stay? 1 for hit and 2 for stay"))
            except:
                print("\nInvalid choice! Try again:")
                continue
            if choice==1 or choice==2:
                if choice==1:
                    hit()
                else:
                    stay()
                break
            else:
                print("\nInvalid choice! Try again:")
                continue

