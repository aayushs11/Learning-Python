import tkinter as tk
from tkinter import messagebox

def simple_interest():
    p= principle.get()
    t= time.get()
    r= rate.get()
    
    if p.isdigit() and t.isdigit() and r.isdigit():
        result= float(p) * float(t) * float(r) / 100
        messagebox.showinfo('Simple Intrest', f'The Simple Interest is Rs {result}')
    else:
        messagebox.showerror('Invalid','Enter Valid Data')

frame=tk.Tk()
frame.geometry('310x300')
frame.title('Simple Interest Calculator')

#Label
tk.Label(frame,text='Principle').pack()
principle= tk.Entry(frame)
principle.pack()

tk.Label(frame,text='Time').pack()
time= tk.Entry(frame)
time.pack()

tk.Label(frame,text='Rate').pack()
rate= tk.Entry(frame)
rate.pack()

button= tk.Button(frame,text='Calculate SI',command=simple_interest).pack(pady=10)

tk.Label(frame,text='Developed by AJ Aayush').pack(pady=30)
frame.mainloop()