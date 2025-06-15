
from martypy import Marty

my_marty=Marty ("wifi","192.168.0.111")



def move_on():
    my_marty.walk(num_steps=7,start_foot='auto',turn=0,step_length=25,move_time=1000)
    my_marty.stand_straight()




def move_back():
    my_marty.walk(num_steps=7,start_foot='auto',turn=0,step_length=-25,move_time=1000)
    my_marty.stand_straight()
    


def step_right():
    my_marty.sidestep("right",7)
    my_marty.stand_straight()
    
def step_left():
    my_marty.sidestep("left",7)
    my_marty.stand_straight()
    
    


def turn_left():
    
    my_marty.walk(turn=15,move_time=1000)
    

def turn_right():
    
    my_marty.walk(turn=-15,move_time=1000)
    
    




    
       