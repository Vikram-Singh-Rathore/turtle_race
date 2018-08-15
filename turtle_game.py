#TURTLE GAME PROJECT

from tkinter import *
import random
import turtle as tr
root=Tk()
root.title('TURTLE RACE')
canvas=Canvas(root,width=500,height=500)
canvas.pack()
turtle=tr.RawTurtle(canvas)
turtle.speed(0)
turtle.penup()
turtle.goto(-140,140)


#making the race track
for path in range(15):
    turtle.write(path,align='center') #starting point
    turtle.right(90) #pointing the pointer at the right side
    for n in range(8):
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()
        turtle.forward(10)
    turtle.penup()   
    turtle.backward(160)
    turtle.left(90)
    turtle.forward(20)

#drwaing red turtle      
red=tr.RawTurtle(canvas)
red.color('red')
red.shape('turtle')

#point the turle at the starting point
red.penup()
red.goto(-160,100)
red.pendown()

for turn in range(10):
    red.right(36)
#making blue turtle
blue=tr.RawTurtle(canvas)
blue.color('blue')
blue.shape('turtle')

#point the turtle at the starting point
blue.penup()
blue.goto(-160,70)
blue.pendown()


for turn in range(72):
    blue.left(5)

 
    
    
#making green turtle
green=tr.RawTurtle(canvas)
green.color('green')
green.shape('turtle')

#point the turtle at the starting point
green.penup()
green.goto(-160,40)
green.pendown()


for turn in range(60):
    green.right(6)   
    
    
    
#making yellow turtle
yellow=tr.RawTurtle(canvas)
yellow.color('yellow')
yellow.shape('turtle')

#point the turtle at the starting point
yellow.penup()
yellow.goto(-160,10)
yellow.pendown()


for turn in range(30):
    yellow.left(12)

#function for the racing

def Start():
    r=red.goto(-160,100)
    b=blue.goto(-160,70)
    g=green.goto(-160,40)
    y=yellow.goto(-160,10)
    for move in range(100):
        red.forward(random.randint(1,5))
        blue.forward(random.randint(1,5))
        green.forward(random.randint(1,5))
        yellow.forward(random.randint(1,5))
    return

start_button=Button(root,text='START',fg='RED',command=Start).pack()
exit_button=Button(root,text="EXIT",fg='GREEN',command=root.destroy).pack()


mainloop()
