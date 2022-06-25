import turtle                                   #import for turtle
from Modules import main_menu                   #import from main menu

########################
###  WELCOME WINDOW  ###
########################

wn = turtle.Screen()                            #turtle drawing during the opening of the program
wn.bgcolor("light blue")                        #set the window background colour
wn.title("Food Ordering System - Welcome Page") #set the window title
tess = turtle.Turtle()                          #create tess and set some attributes
tess.hideturtle()
tess.penup()                                    #is used to pick up the pen and turtle stop drawing
tess.color('black')                             #is used to give black colour on the star
tess.goto(-75, 200)
tess.pendown()                                  #starts to draw star pattern
tess.speed(10)                                  #speed setting can be set between 1(slowest) to 10(fastest)
for i in [0, 1, 2, 3, 4]:                       #executing loop 5 times for a star
    tess.forward(100)                           #moving turtle 100 units forward
    tess.right(144)                             #rotating turtle 144 degree right

tess.penup()
tess.goto(-180, 90)
tess.pendown()
style1 = ('Courier', 30, 'bold')
tess.write('W E L C O M E', font=style1)

tess.penup()
tess.goto(-320, 10)
tess.pendown()

style2 = ('Courier', 20, 'italic')
tess.write("\nYou are using UTEM Food Ordering System", font=style2) # entering the welcome page of food ordering system

tess.penup()
tess.goto(100, -50)
tess.pendown()

tess.speed(7)

tess.color('brown')                               #is used to give brown colour on the word "Click to continue"
style3 = ('Courier', 10, 'italic')
tess.write("Click to continue...", font=style3)

tess.speed(10)
tess.penup()
tess.backward(20)
tess.pendown()
tess.forward(200)
tess.hideturtle()

wn.exitonclick()


#######################
###  MAIN FUNCTION  ###
#######################

main_menu()



