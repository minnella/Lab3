import turtle # allows us to use the turtles library

wn = turtle.Screen() #creates a graphics window

#set the turtle background color
wn.bgcolor("lightblue")

#creates a turtle named Murtle
Murtle = turtle.Turtle() 

#Murtle's attributes
Murtle.color("darkgreen")
Murtle.pensize(5)

#move Murtle with user input
sides = input("Number of sides: " )
for i in range(sides):
	Murtle.forward(75)
	Murtle.right(360/sides)



