# http://www.codeskulptor.org/#user38_BLhraHQAHe_1.py
# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
#outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
    
    def draw_back(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0]+ CARD_BACK_SIZE[0]  , 
                    CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        
    
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.card = []

    def __str__(self):
        # return a string representation of a hand
        result = ""
        for card in self.card:
            result += card.get_suit()+card.get_rank()+" "
        return "Hand contains "+result

    def add_card(self, card):
        self.card.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        haveAces = False
        result = 0
        for card in self.card:
            result += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                haveAces = True
        if not haveAces:
            return result
        else:
            if result + 10 <= 21:
                return result + 10
            else:
                return result
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for i in range(len(self.card)):
            card = self.card[i]
            card.draw(canvas,[pos[0]+i*1.2*CARD_SIZE[0],pos[1]])
    def draw_back(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        card = self.card[0]
        card.draw_back(canvas,[pos[0],pos[1]])
         
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.cards = []
        for i in SUITS:
            for j in RANKS:
                newcard = Card(i,j)
                self.cards.append(newcard)
        #for i in range(len(SUITS)):
        #    for j in range(len(RANKS)):
        #        newcard = Card(SUITS[i],RANKS[j])
        #        self.cards.append(newcard)

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.cards)

    def deal_card(self):
        # deal a card object from the deck
        return self.cards.pop()
    
    def __str__(self):
        # return a string representing the deck
        result = ""
        for card in self.cards:
            result += card.get_suit()+card.get_rank()+" "
        return "Deck contains " + result



#define event handlers for buttons
def deal():
    global outcome, reminder, score, in_play, newDeck, playerHand, dealerHand
    
    if in_play:
        in_play = False
        outcome = "You clicked deal and lose."
        score -= 1
        reminder = "New deal?"
    else:
        outcome =""
        reminder = "Hit or stand?"    
        in_play = True
        # new deck
        newDeck = Deck()
        newDeck.shuffle()
        
        playerHand = Hand()
        dealerHand = Hand()
        
        cardp1 = newDeck.deal_card() # 1st card for player
        playerHand.add_card(cardp1)
        cardp2 = newDeck.deal_card() # 2nd card for player
        playerHand.add_card(cardp2)
        #print playerHand
        
        cardd1 = newDeck.deal_card() # 1st card for dealer
        dealerHand.add_card(cardd1)
        cardd2 = newDeck.deal_card() # 2nd card for dealer
        dealerHand.add_card(cardd2)
        #print dealerHand
    
    
    

def hit():
    global outcome, reminder, in_play, score, playerHand
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
    if in_play:
        newcard = newDeck.deal_card()
        playerHand.add_card(newcard)
        if playerHand.get_value() > 21:
            reminder = "New deal?"
            in_play = False
            outcome = "You went bust and lose."
            score -= 1
       
def stand():
    global outcome, reminder, in_play, score, dealerHand
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score
    if in_play:
        while dealerHand.get_value() < 17:
            newcard = newDeck.deal_card()
            dealerHand.add_card(newcard)
        if dealerHand.get_value() <= 21:
            if dealerHand.get_value() >= playerHand.get_value():
                outcome = "You lose."
                reminder = "New deal?"
                score -= 1
            else:
                outcome = "You win."
                reminder = "New deal?"
                score += 1
        else:
            outcome = "Dealer bust, you win!"
            reminder = "New deal?"
            score += 1
        
        in_play = False

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    #card = Card("S", "A")
    #card.draw_back(canvas, [300, 300])
    canvas.draw_text('Blackjack', (80, 100), 45, 'Cyan')
    canvas.draw_text('Score: '+str(score), (400, 100), 35, 'Black')
    canvas.draw_text('Dealer', (80, 160), 35, 'Black')
    canvas.draw_text(outcome, (220, 160), 35, 'Black')
    canvas.draw_text('Player', (80, 350), 35, 'Black')
    canvas.draw_text(reminder, (320, 350), 35, 'Black')
    
    if in_play:
        dealerHand.draw(canvas,[80,200])
        dealerHand.draw_back(canvas,[80,200])
    else:
        dealerHand.draw(canvas,[80,200])
    playerHand.draw(canvas,[80,400])
    
    
    


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric