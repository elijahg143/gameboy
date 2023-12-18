#name of program: GameBoy Customizer
#author of program: Elijah Gonzalez
#version 2, worked on last 12/17/2023

#variable dictionary
#text1-text4:
#text that displays on the window giving instructions

#explanation: a function that goes with text1-4, displays text on the window to guide users

#writeReceipt: a function that allows all the data to be saved, gives who ordered what colors
#for what parts.

#gameBoyDraw: the last thing done. it grabs all the variables, then draws the gameboy

#getColors: gets the colors 


#frontData, backShell, dpadData, buttonData, startSelectData, volumeSliderData:
#variables that are assigned colors for their respective part of the Gameboy

#f: used to help open files, and write to the files as well. closes files too once called upon
#to do so.

#rNum: a random string of numbers so every file is unique and hosts different data.

#buttonAsk: a var to the button that allows the user to click it to see instructions
#buttonBegin: a var to the button that allows the user to begin entering colors
#buttonEnd: a var to the button that self destructs the windows and ends the program
#buttonStart: draws the GameBoy

#when text reappears under text1-7:
#text so that the user knows which part of the gameboy they are giving the color to, as well as their name so it remembers what colors they chose for each part
#textbox 1-7: textboxs that take the input and store the colors to the gameboy parts.

#import applications to allow things you cannot normally do in vanilla python
import turtle
import tkinter as tk
import random

#import everything
from tkinter import *

#helps give each files a unique var
rNum = str(random.randrange(1,1000000))


#this allows the user to see instructions on the process of the program if they need to.
def explanation():
        text1 = Label(window, text="Okay, to use the program, you have to input colors available with the Python")
        text1.place(x=70,y=90)
        text2 = Label(window, text="Turtle graphics. Here are a list of 15 example colors.: Black, Red, Green, Blue, Yellow, Aqua")
        text2.place(x=70,y=110)
        text3 = Label(window, text="Orange, Lime, Gold, Silver, Purple, Pink, Magenta, Violet, and White(not reccomended for shell of Gameboy.)")
        text3.place(x=70,y=130)
        text4 = Label(window, text="You can also do this through Hex Codes, entering it exactly as'#RRGGBB'")
        text4.place(x=70,y=150)

#writes the receipt with the unique var, and if it is the same, it just adds to it. if we dont, it always adds to the same file. if we open a file with w and it doesnt exist, it wont write.
#if we use x, it wont make a file cause it already exists the second time onwards.
def writeReciept():
        f = open( 'GBData'+rNum+'.txt', 'a' )
        f.write( userData + '\n' )
        f.write( "Front Shell:" + frontData + '\n' )
        f.write( "Back Shell: " + backShell + '\n' )
        f.write( "D-Pad Shell: " + dpadData + '\n' )
        f.write( "Start and Select: " + startSelectData + '\n' )
        f.write( "Buttons: " +buttonData + '\n' )
        f.close()

#define our variables, assign them to text boxes, end button is there if the user wants to end the program, buttonStart starts confirms the users entries. it is all then packed
#onto screen in the order for each button and text is lined up to the variables so the gameboy looks right.

def getColors():
        main=Toplevel(window)
        main.title("Window for Colors")

        def save_textbox_input():
            global frontData
            global backShell
            global dpadData
            global buttonData
            global startSelectData
            global volumeSliderData
            global userData
            frontData = textbox1.get("1.0", "end-1c")
            backShell = textbox2.get("1.0", "end-1c")          
            dpadData = textbox3.get("1.0", "end-1c")
            buttonData = textbox4.get("1.0", "end-1c")
            startSelectData = textbox5.get("1.0", "end-1c")
            volumeSliderData = textbox6.get("1.0", "end-1c")
            userData = textbox7.get("1.0", "end-1c")
            writeReciept()
            gameBoyDraw()
        buttonEnd = Button(main,
                text="Click to exit application.",
                command=exit)
        buttonStart = Button(main,text="Click to save the inputs and draw GameBoy", command=save_textbox_input)
        textbox1 = tk.Text(main, width="30", height="2")
        text1 = Label(main, text="Input front color:")
        textbox2 = tk.Text(main, width="30", height="2")
        text2 = Label(main,text="Input back color:")
        textbox3 = tk.Text(main, width="30", height="2")
        text3 = Label(main,text="Input D-Pad color")
        textbox4 = tk.Text(main, width="30", height="2")
        text4 = Label(main,text="Input A and B button Colors")
        textbox5 = tk.Text(main, width="30", height="2")
        text5 = Label(main,text="Input Start Select color")
        textbox6 = tk.Text(main, width="30", height="2")
        text6 = Label(main,text="Input volume slider color")
        textbox7 = tk.Text(main,width="30",height="2")
        text7 = Label(main,text="Input name")
        buttonEnd.pack()
        text1.pack()
        textbox1.pack()
        text2.pack()
        textbox2.pack()
        text3.pack()
        textbox3.pack()
        text4.pack()
        textbox4.pack()
        text5.pack()
        textbox5.pack()
        text6.pack()
        textbox6.pack()
        text7.pack()
        textbox7.pack()
        buttonStart.pack()
        tk.mainloop()

#the long if statement is for detecting a blank var, it tells the user one is blank and to reinput the data. the program will still run, but wont cause any issues if one piece of data is missing.
#this also begins to draw the gameboy. each part is labeled for what does what.
def gameBoyDraw():

    if frontData and backShell and dpadData and buttonData and startSelectData and volumeSliderData and userData:
            print()
    else:
            print("Data missed. The missing data will not be drawn, or inputted as blank. Reinput data, be careful next time.")

    t = turtle.Turtle()
    
    #position for body
    t.pencolor("White")
    t.setpos(-150,-150)

    #draw beginning line
    t.color(frontData)
    t.forward(290)

    #break away for side view
    t.color("White")
    t.forward(30)

    #draw front of side view
    t.color("Black")
    t.color(backShell)
    t.begin_fill()
    t.left(90)
    t.forward(390)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(390)
    t.right(90)
    t.forward(25)
    t.end_fill()

    #position for back view
    t.color(backShell)
    t.right(90)
    t.forward(390)
    t.right(90)
    t.forward(26)
    t.color(frontData)
    t.begin_fill()
    t.forward(24)
    t.right(90)
    t.forward(390)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(390)
    t.end_fill()

    #position for volume slider
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(140)
    t.right(90)
    t.forward(25)

    #draw volume
    t.color(volumeSliderData)
    t.begin_fill()
    t.forward(20)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(60)
    t.end_fill()

    #position for rest of body
    t.color(backShell)
    t.forward(250)
    t.right(90)
    t.forward(26)
    t.color("White")
    t.forward(30)

    #draw body
    t.color(frontData)
    t.begin_fill()
    t.right(90)
    t.forward(390)
    t.left(90)
    t.forward(290)
    t.left(90)
    t.forward(390)
    t.left(90)
    t.end_fill()

    #position for dpad
    t.forward(1)
    t.forward(80)
    t.left(90)
    t.forward(80)

    #draw dpad
    t.color(dpadData)
    t.begin_fill()
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.end_fill()
    t.forward(21)

    #position for button 1
    t.color(frontData)
    t.forward(150)

    #button 1
    t.color(buttonData)
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.right(90)

    #position for button 2
    t.forward(1)
    t.color(frontData)
    t.forward(1)
    t.right(90)
    t.forward(20)

    #button 2
    t.color(buttonData)
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.forward(5)

    #position for start and select
    t.color(frontData)
    t.forward(75)
    t.left(90)
    t.forward(75)
    t.right(90)
    t.left(20)

    #draw select
    t.color(startSelectData)
    t.begin_fill()
    t.circle(2,180)
    t.forward(20)
    t.circle(2,180)
    t.forward(20)
    t.right(2)
    t.forward(1)
    t.end_fill()

    #position for start
    t.color(frontData)
    t.forward(30)

    #draw start
    t.color(startSelectData)
    t.begin_fill()
    t.circle(2,180)
    t.forward(20)
    t.circle(2,180)
    t.forward(20)
    t.right(108)
    t.forward(1)
    t.end_fill()

    #position for outer screen
    t.color(frontData)
    t.forward(150)

    #draw outer screen
    t.color("Gray")
    t.begin_fill()
    t.left(90)
    t.forward(80)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(230)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(180)
    t.right(90)
    t.forward(1)
    t.end_fill()

    #position for inner screen
    t.forward(40)

    #draw inner screen, at the end it turns -45 to hide the arrow.
    t.color("Black")
    t.begin_fill()
    t.forward(120)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(120)
    t.right(90)
    t.forward(120)
    t.right(-45)
    t.end_fill()

#create window, define is size by window.geometry
#name it "window for main" as it is the main page.
#buttons for wanting an explanation by the user,
#wanting to start the app, or end it.
#it is unpacked so it displays on the screen, then mainloop to actually run this process.
window = Tk()
window.geometry("700x300")
window.title("Window for Main")

buttonAsk = Button(window,
                text="Click for an explanation.",
                command=explanation)
buttonBegin = Button(window,
                text="Click to start the application",
                command=getColors)
buttonEnd = Button(window,
                text="Click to end application.",
                command=exit)

buttonAsk.pack()
buttonBegin.pack()
buttonEnd.pack()

window.mainloop()
        






