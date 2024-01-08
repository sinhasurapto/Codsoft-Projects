from tkinter import *
import tkinter.messagebox


# Enter a task
def entertask():
    input_text = ""
    def add():
        input_text = entry_task.get(1.0, "end-1c")
        if input_text == "":
            tkinter.messagebox.showwarning(title="Warning", message="Please enter some text!")
        else:
            listbox_task.insert(END, input_text)
            root1.destroy()
    root1 = Tk()
    root1.title("Add task")
    entry_task = Text(root1, width=40, height=4)
    entry_task.pack()
    button_temp = Button(root1, text="Add task", command=add)
    button_temp.pack()
    root1.mainloop()


# Delete a task
def deletetask():
    selection = listbox_task.curselection()
    listbox_task.delete(selection[0])


# To mark as completed
def markcompleted():
    marked = listbox_task.curselection()
    temp = marked[0]
    # store the text of selected item in a string
    temp_marked = listbox_task.get(marked)
    # update it
    temp_marked = temp_marked + " ✔"
    # delete it then insert it
    listbox_task.delete(temp)
    listbox_task.insert(temp, temp_marked)


# Window and window title
window = Tk()
window.title("My To-do List")

# Frame widget
frame_task = Frame(window)
frame_task.pack()

# Listbox widget
listbox_task = Listbox(frame_task, bg="red", fg="yellow", height=15, width=40, font="Helvetica")
listbox_task.pack(side=tkinter.LEFT)

# Scroll
scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

# Button widget
entry_button = Button(window, text="Add task", width=50, command=entertask)
entry_button.pack(pady=3)
delete_button = Button(window, text="Delete selected task", width=50, command=deletetask)
delete_button.pack(pady=3)
mark_button = Button(window, text="Mark as completed ", width=50, command=markcompleted)
mark_button.pack(pady=3)

window.mainloop()
