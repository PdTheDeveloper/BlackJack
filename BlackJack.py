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
            print(f"{x}. {self.cards[x]}\n")

    def sum(self):
        return self.sum

    def showCard(self,position):
        self.cards[position-1].show()

    def hideCard(self,position):
        self.cards[position-1].hide()


playerMoney=0

def addMoney(amount):
    global playerMoney
    playerMoney+=amount

def busted(deck):
    if deck.sum()>21:
        return True
    else:
        return False


def drawCards():
    pass

#Globals
nums={"Ace":11,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,"Jack":10,"Queen":10,"King":10}
types=["Heart","Diamond","Club","Spade"]

fullDeck=None
fullCards=[]
for i in nums.items():
    for t in types:
        fullCards.append(Card(t, i))

dealerDeck=None
gamblerDeck=None


def setCards():
    global fullCards,fullDeck
    random.shuffle(fullCards)
    fullDeck=None
    fullDeck=Deck(fullCards)

def init():
    global dealerDeck,gamblerDeck,fullDeck
    print(35*"\n")
    setCards()
    dealerDeck = None
    gamblerDeck = None
    for x in range(2):
        fullDeck.draw(dealerDeck)
        fullDeck.draw(gamblerDeck)
    dealerDeck.hideCard(2)



def updateTable(dealerDeck,gamblerDeck):
    print(35*"\n")
