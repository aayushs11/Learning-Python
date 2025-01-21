import tkinter as tk

def add_task():
    task= input.get()
    if task!='':
        listbox.insert(tk.END,task)
        input.delete(0,tk.END)

def delete_task():
    listbox.delete(tk.ANCHOR)

frame= tk.Tk()
frame.geometry('400x400')
frame.title('To Do List')

banner= tk.Label(frame,text="Simple To Do List").pack()

input= tk.Entry(frame,width=50)
input.pack()

add_button= tk.Button(frame,text='Add Task',command=add_task)
add_button.pack(pady=7)

listbox= tk.Listbox(frame,width=50, height=15)
listbox.pack()

del_button= tk.Button(frame,text='Delete Task',command=delete_task)
del_button.pack(pady=7)

footer=tk.Label(frame,text='Developed by AJ Aayush').pack(pady=10)
frame.mainloop()