http://codeskulptor-user38.commondatastorage.googleapis.com/user38_raZmI7MPCF_5.py

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    if direction:
        ball_vel = [random.randrange(1,5), -random.randrange(1,5)]
    else:
        ball_vel = [-random.randrange(1,5),-random.randrange(1,5)]
    
  


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos = HEIGHT /2 
    paddle2_pos = HEIGHT /2 
    paddle1_vel = 0
    paddle2_vel = 0
    
    score1 = 0
    score2 = 0
    
    
    spawn_ball(LEFT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White") # mid line
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White") # left gutter
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White") # right gutter
        
    # update ball
    if (ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS): # touch right edge
        if (ball_pos[1] <= paddle2_pos+HALF_PAD_HEIGHT) and (ball_pos[1] >= paddle2_pos-HALF_PAD_HEIGHT):
            ball_vel[0] = -1.1*ball_vel[0]
            ball_pos[0] = ball_pos[0] + ball_vel[0]
            ball_pos[1] = ball_pos[1] + ball_vel[1]
        else:
            score1 += 1
            spawn_ball(LEFT)
    elif ball_pos[0] <= PAD_WIDTH + BALL_RADIUS: # touch left edge
        if (ball_pos[1] <= paddle1_pos+HALF_PAD_HEIGHT) and (ball_pos[1] >= paddle1_pos-HALF_PAD_HEIGHT):
            ball_vel[0] = -1.1*ball_vel[0]
            ball_pos[0] = ball_pos[0] + ball_vel[0]
            ball_pos[1] = ball_pos[1] + ball_vel[1]
        else:
            score2 += 1
            spawn_ball(RIGHT)        
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS: # touch bottom
        ball_vel[1] = -ball_vel[1]
        ball_pos[0] = ball_pos[0] + ball_vel[0]
        ball_pos[1] = ball_pos[1] + ball_vel[1]
    elif ball_pos[1] <= BALL_RADIUS: # touch top
        ball_vel[1] = -ball_vel[1]
        ball_pos[0] = ball_pos[0] + ball_vel[0]
        ball_pos[1] = ball_pos[1] + ball_vel[1]
    else:
        ball_pos[0] = ball_pos[0] + ball_vel[0]
        ball_pos[1] = ball_pos[1] + ball_vel[1]
    
    
    
            
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,5,"White","White")
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos+paddle1_vel >= HALF_PAD_HEIGHT and paddle1_pos+paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos = paddle1_pos + paddle1_vel
    if paddle2_pos+paddle2_vel >= HALF_PAD_HEIGHT and paddle2_pos+paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos = paddle2_pos + paddle2_vel
    
    # draw paddles
    canvas.draw_line([PAD_WIDTH/2,paddle1_pos-HALF_PAD_HEIGHT],[PAD_WIDTH/2,paddle1_pos+HALF_PAD_HEIGHT],PAD_WIDTH,"White")
    canvas.draw_line([(WIDTH-PAD_WIDTH/2),paddle2_pos-HALF_PAD_HEIGHT],[(WIDTH-PAD_WIDTH/2),paddle2_pos+HALF_PAD_HEIGHT],PAD_WIDTH,"White")


    # draw scores
    canvas.draw_text(str(score1),[WIDTH/4,HEIGHT/6],25,"White")
    canvas.draw_text(str(score2),[WIDTH*3/4,HEIGHT/6],25,"White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -5
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 5
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -5
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 5

   
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset",new_game,50)


# start frame
new_game()
frame.start()