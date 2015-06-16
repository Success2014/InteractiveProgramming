# http://codeskulptor-user38.commondatastorage.googleapis.com/user38_Rig1EAjvhQ_0.py

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


import simplegui
import random
import math


range = 100


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    
    global secret_number, remain_guess
    # secret_number = random.randrange(0, range)
    secret_number = random.randrange(0, range)
    print "*--------------*"
    print "New Game Starts"
    print "*--------------*"
    
    if range == 100:
        remain_guess = 7       
    elif range == 1000:
        remain_guess = 10
    else:
        print "Wrong Range"
    
    print "Number of remaining guesses is", remain_guess
   
    
   
    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range
    range = 100
    new_game()
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range
    range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global remain_guess
    player_guess = int(guess)
    print "Guess was", player_guess
    
    remain_guess = remain_guess - 1
    
    
    print "Number of remaining guesses is", remain_guess
    if remain_guess ==0:
        print "You have run out of chances!"
        print "The secrect number is: ", secret_number
        new_game()
    if player_guess > secret_number:
        print "Lower"
        print ""
    elif player_guess < secret_number:
        print "Higher"
        print ""
    else:
        print "Correct!"
        print ""
        new_game()
    
    
    

    
# create frame
frame = simplegui.create_frame("Guess the number",300,300)
frame.add_button("Range is [0,100)", range100,200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 100)

frame.start


# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric