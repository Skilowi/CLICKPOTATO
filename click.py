from tkinter import *

win = Tk()
win.title("CLICK POTATO!")
win.geometry("400x200")
win.configure(bg="black")

Punkty = 0

def CLICK():
	global Punkty
	global WYNIK
	global ZIEMNIORY
	global Sklepik
	WYNIK.destroy()
	ZIEMNIORY.destroy()
	Punkty += 1
	WYNIK = Label(text = Punkty, bg = "black", fg = "white" )
	WYNIK.pack(side = "bottom")
	ZIEMNIORY = Label(text = "CLICKED POTATOES:", bg = "black", fg = "white" )
	ZIEMNIORY.pack(side = "bottom")
	
def EXIT():
	win.destroy()

ZIEMNIOK = Button(win, text = "POTATO!", command = CLICK, height = 2, width = 7, bg = "black", fg = "white" )
ZIEMNIOK.pack(side = "top")

WYNIK = Label(text = Punkty , bg = "black", fg = "white" )
WYNIK.pack(side = "bottom")

ZIEMNIORY = Label(text = "CLICKED POTATOES:", bg = "black", fg = "white" )
ZIEMNIORY.pack(side = "bottom")

WYJSCIE = Button(win, text = "EXIT", command = EXIT, height = 2, width = 7, bg = "black", fg = "white" ).place(x=0, y=0)

mainloop()
