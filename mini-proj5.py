#http://www.codeskulptor.org/#user38_1VcUllUVOb_3.py
# implementation of card game - Memory
# shut down previous 2 cards

import simplegui
import random

CARD_WIDTH = 50

decks = []
exposed = [False] * 16
state = 0

tmp_index = [] # used to record 1 step previous selection
tmp_index2 = [] # used to record 2 steps previous selection

counter = 0

# helper function to initialize globals
def new_game():
    global decks, counter, exposed
    exposed = [False] * 16
    decks = range(8)*2
    random.shuffle(decks) 
    counter = 0

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, state, tmp, tmp_index, tmp_index2, counter
    
    
    index = pos[0] // CARD_WIDTH
    if not exposed[index]:
        counter += 1
        print counter
        if state == 0:
            state = 1
            exposed[index] = True
            tmp_index2 = index
            
        elif state == 1:
            
            exposed[index] = True
            if decks[index] == decks[tmp_index2]:
                state = 0
            else:
                state = 2
                tmp_index = index
                
        else:
            
            exposed[index] = True
            exposed[tmp_index2] = False
            exposed[tmp_index] = False
            
            state = 1
            tmp_index2 = index
            
            
            #tmp_index2 = tmp_index
            #tmp_index = index
    
    
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    
    label.set_text("Turns = " + str(counter//2))
    for i in range(0,len(decks)):
        if (exposed[i]):
            canvas.draw_text(str(decks[i]),[15+50*i,65],40,"White")
        else:
            canvas.draw_polygon([[i*50, 0], [i*50+50, 0], [i*50+50, 100], [i*50, 100]], 1, 'Yellow', 'Green')
        
    


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()



# Always remember to review the grading rubric