#Importing tkinter for GUI
import tkinter as tk

#Create window
root= tk.Tk()

#Set window title
root.title("MyApplication")

#Set window size
root.geometry('300x300')

#Create label with text
label= tk.Label(root, text="Welcome to my World!")

#Add label to window
label.pack()

#Start the GUI Loop
root.mainloop()