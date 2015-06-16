##http://codeskulptor-user38.commondatastorage.googleapis.com/user38_zFyB8rRBe0_2.py
# template for "Stopwatch: The Game"

import simplegui

# define global variables
t = 0
stop_count = 0
success_count = 0
A = 0
B = 0
C = 0
D = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global A, B, C, D
    A = (t / 600) % 10
    tt = t - A * 600 # temp variable
    
    B = (tt / 100) % 10
    C = (tt / 10) % 10
    D = tt % 10
    return str(A)+":"+str(B)+str(C)+"."+str(D)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    timer.start()
    
def Stop():
    global stop_count, success_count
    timer.stop()
    stop_count += 1
    if D == 0:
        success_count += 1
    
def Reset():
    global t, stop_count, success_count
    timer.stop()
    t = 0
    stop_count =0
    success_count = 0
    

# define event handler for timer with 0.1 sec interval
def time_handler():
    global t
    t += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(t),[50,100],40,"White")
    canvas.draw_text(str(success_count)+"/"+str(stop_count),[150,20],30,"Green")
    
# create frame
frame = simplegui.create_frame("Stop Watch",200,150)
frame.add_button("Start",Start,50)
frame.add_button("Stop",Stop,50)
frame.add_button("Reset",Reset,50)


# register event handlers
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100,time_handler)


# start frame
frame.start()


# Please remember to review the grading rubric