__author__ = 'Nick'

import tkinter
import random
import os

def buttonPressed( event ):
   f = random.randrange(8)
   os.system("afplay ./"+str(f)+".wav")

root= tkinter.Tk()
root.title("canvas example")
root.geometry("800x600")
canvas = tkinter.Canvas(root, bg="#666666", 
	height=root.winfo_screenheight(), width=root.winfo_screenwidth())
canvas.pack()

points = [100, 140, 110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]
canvas.create_polygon(points, outline="black",fill='yellow', width=3)

canvas.bind( "<Button-1>", buttonPressed )

root.mainloop()