import pygame, sys, time
from pygame.locals import *

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

#windowSurface = pygame.display.set_mode((800, 600), 0, 32)

### Tells the number of joysticks/error detection
joystick_count = pygame.joystick.get_count()
print ("There is ", joystick_count, "joystick/s")
if joystick_count == 0:
    print ("Error, I did not find any joysticks")
else:
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()

#crosshairs = pygame.image.load("crosshairs.png")
#background = pygame.image.load("shooter/image_library/background.jpg")

x = 300
y = 300
### Creates rectangle
#Rectangle = pygame.Rect( x, y, 100, 100)
#Back = pygame.Rect(0, 0, 800, 600)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    button1=my_joystick.get_button(0)
    button2=my_joystick.get_button(1)
    button3=my_joystick.get_button(2)
    button4=my_joystick.get_button(3)
    button5=my_joystick.get_button(4)
    button6=my_joystick.get_button(5)
    button7=my_joystick.get_button(6)
    button8=my_joystick.get_button(7)
    button9=my_joystick.get_button(8)
    button10=my_joystick.get_button(9)


    left_zy_axis_pos = my_joystick.get_axis(0)
    left_sx_axis_pos = my_joystick.get_axis(1)
    right_zy_axis_pos = my_joystick.get_axis(2)
    right_sx_axis_pos = my_joystick.get_axis(3)


    if left_sx_axis_pos!=0 and button5==1:
        front=-left_sx_axis_pos
        l_speed=r_speed=front*wanted_speed
        print (l_speed,r_speed)
    elif left_zy_axis_pos!=0 and button7==1:
        right=left_zy_axis_pos*maxturn
        front=-left_sx_axis_pos
        l_speed=(front+right)*stable_speed
        r_speed=(front-right)*stable_speed
        if l_speed>100:
            l_speed=100
        if r_speed>100:
            r_speed=100
        print (l_speed,r_speed)
            
    print (left_zy_axis_pos, left_sx_axis_pos, right_zy_axis_pos, right_sx_axis_pos)
 
    print (button1,button2,button3,button4,button5,button6,button7,button8,button9,button10)    


    time.sleep(1)
	
