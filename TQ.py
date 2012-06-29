import turtle

turtle.setup(1000,1000)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Turtle Quest")     # Change the window title
wn.bgcolor("DeepPink") 
malacai= turtle.Turtle()
malacai.color("DarkOrchid", "DeepSkyBlue")
malacai.pensize(6)
malacai.up()
malacai.ht()

#Make the T
malacai.setpos(-450, 450)
malacai.down()
#top
malacai.forward(200)
malacai.right(90)
malacai.forward(50)
malacai.right(90)
malacai.forward(75)
malacai.left(90)
malacai.forward(200)
malacai.right(90)
malacai.up()
malacai.forward(50)
malacai.right(90)
malacai.down()
malacai.forward(200)
malacai.left(90)
malacai.forward(75)
malacai.right(90)
malacai.forward(50)
malacai.up()

#Make the U

malacai.setpos(-375,200)
malacai.down()
malacai.left(180)
malacai.forward(250)
malacai.left(90)
malacai.forward(200)
malacai.left(90)
malacai.forward(250)
malacai.left(90)
malacai.forward(50)
malacai.left(90)
malacai.forward(200)
malacai.right(90)
malacai.forward(100)
malacai.right(90)
malacai.forward(200)


#Make R
malacai.up()
malacai.right(90)
malacai.forward(150)
malacai.stamp()
turtle.done()
