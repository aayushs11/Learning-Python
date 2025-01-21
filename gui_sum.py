import tkinter as tk
from tkinter import messagebox

#Function to calculate sum and display result
def find_sum():
    num1= entry1.get()
    num2= entry2.get()

    if num1.isdigit() and num2.isdigit():
        result= int(num1) + int(num2)
        messagebox.showinfo('Result',f'The Sum of two numbers is {result}')
    else:
        messagebox.showerror('Error','Enter valid numbers')

#Create Window
window= tk.Tk()
window.title('Simple Addition APP')
window.geometry('300x300')

#Label
label= tk.Label(window,text='SUM')
label.pack()

#Input fields
entry1= tk.Entry(window)
entry1.pack(pady=7)

entry2= tk.Entry(window)
entry2.pack(pady=7)

#Create button
buttom=tk.Button(window,text='ADD', command=find_sum)
buttom.pack()
#OR, buttom=tk.Button(window,text='ADD', command=find_sum).pack(pady=7)

footer= tk.Label(window,text='Developed by AJ Aayush').pack(pady=80)
window.mainloop()