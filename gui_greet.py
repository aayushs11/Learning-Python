import tkinter as tk

def greet():
    label.config(text='Namaste! Welcome to Nepal🙏')

win= tk.Tk()
win.title('Nepal')
win.geometry('300x300')
label= tk.Label(win,text="Click the button for surprise")
button= tk.Button(win, text='Click Me!',command=greet)
button.pack(padx=10)
label.pack()
win.mainloop()