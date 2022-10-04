import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do List App")
root.geometry("600x400")

f_done = ('Times', 10, 'overstrike', 'italic')

def my_upd(k):
    if(my_ref[k][1].get()==True):
         my_ref[k][0].config(font=f_done, fg= 'blue')
    else:
         my_ref[k][0].config(font='arial 8', fg='black')

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")


def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")


def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")


def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))


frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)
scrollbar_tasks.config(command=listbox_tasks.yview)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Delete task", width=48, command=delete_task)
button_delete_task.pack()

button_load_tasks = tkinter.Button(root, text="List of tasks", width=48, command=load_tasks)
button_load_tasks.pack()

button_save_tasks = tkinter.Button(root, text="Save tasks", width=48, command=save_tasks)
button_save_tasks.pack()


my_dict = {'a': 'Task 1', 'b': 'Task 2', 'c': 'Task 3'}
my_ref = {}
i = 1
for k in my_dict.keys():
     var = tkinter.BooleanVar()
     ck = tkinter.Checkbutton(root, text=my_dict[k], variable = var, onvalue=True, offvalue=False, command = lambda k = k: my_upd(k))
     ck.pack(side=tkinter.LEFT)

     my_ref[k] = [ck, var]
     i = i + 1

root.mainloop()
