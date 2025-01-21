import tkinter as tk

def welcome():
    txt.config(text='Experience the deep darkness of Scorpio♏')

app= tk.Tk()
app.title('Scorpio')
app.geometry('250x250')

txt= tk.Label(app,text='The secret is hidden here!')
txt.pack(pady=7)

button= tk.Button(app,text='Tap to Reveal',command=welcome)
button.pack()

app.mainloop()