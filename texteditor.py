# imports
from io import open
from tkinter import *
from tkinter import filedialog as fd

# global variable
path = "" # save files path

#functions
def new():
    global path
    message.set("new file")
    path = ""
    text.delete(1.0, "end") # delete from char n1 to end
    root.title('Simple Text')


def open_file():
    global path
    message.set("open file")
    path = fd.askopenfilename(
        initialdir='.',
        filetypes=(("text files", "*.txt"),),
        title="Open a text file"
    )

    if path != "":
        file = open(path, 'r')
        content = file.read()
        text.delete(1.0, "end")
        text.insert('insert', content)
        file.close()
        root.title(path + ' - Simple Text') #show file path => C:/Users/Admin/Desktop/textfile.txt - Simple Text


def save():
    global path
    message.set("save file")
    if path != "":
        content = text.get(1.0, "end-1c") # last char is a new line, so we don't want it
        file = open(path, 'w+')
        file.write(content)
        file.close()
        message.set("File correctly saved")

    else:
        save_as()


def save_as():
    global path
    message.set("save file as")
    file = fd.asksaveasfile(title="Save File", mode="w", defaultextension=".txt")
    if file is not None:
        path = file.name
        content = text.get(1.0, "end-1c")  # last char is a new line, so we don't want it
        file = open(path, 'w+')
        file.write(content)
        file.close()
        message.set("File correctly saved")
    else:
        message.set("Save canceled")
        path = ""

#root
root = Tk()
root.title("Simple Text")
root.iconbitmap("text_editor_icon.ico")

# header menu
menubar = Menu(root)

# file menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New file", command=new)
filemenu.add_command(label="Open file", command=open_file)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save as", command=save_as)
filemenu.add_separator()
filemenu.add_command(label="exit", command=root.quit)
menubar.add_cascade(menu=filemenu, label="file")


# central text box
text = Text(root)
text.pack(fill="both", expand=1)
text.config(bd=0, padx=6, pady=4, font=("Helvetica", 12))


# Monitor
message = StringVar()
message.set("Welcome to Simple Text!")
monitor = Label(root, textvar=message, justify="left")
monitor.pack(side="left")

# add menu to the root
root.config(menu=menubar)

#mainloop
root.mainloop()
