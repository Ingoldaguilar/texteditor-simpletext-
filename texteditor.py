# imports
from io import open
from tkinter import *
#from tkinter import messagebox as mb
from tkinter import filedialog as fd

# global variable
path = ""  # save files path
# value = ""  # value of btns

#functions
def new():
    global path
    message.set("new file")
    path = ""
    text.delete(1.0, "end")  # delete from char n1 to end
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
        root.title(path + ' - Simple Text')  #show file path => C:/Users/Admin/Desktop/textfile.txt - Simple Text


def save():
    global path
    message.set("save file")
    if path != "":
        content = text.get(1.0, "end-1c")  # last char is a new line, so we don't want it
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


# def search():
    # global value
    # message.set("Search")

    # Crear un widget Entry()
    # entry = Entry(root)
    # entry.pack()

    #  getVal
    # def getVal():
        # global value
        # value = entry.get()
        # message.set(f"Searching - {value}")

    # Crear un botón para obtener el valor de la entrada
    # btn = Button(root, text="Search word", command=getVal)
    # btn.pack()

    # Search word
    # position = text.search(value, "1.0", stopindex="end")
    # print(position)
    # highlight word
    # if position:
    #     text.tag_add("resaltado", position, f"{position}+{len(value)}c")
    #     text.tag_config("resaltado", background="yellow")

    # root.title('Simple Text')


def cleartext():
    message.set("Clear Text")
    text.delete(1.0, "end") # delete from char n1 to end
    root.title('Simple Text')


def getHelp():
    global path
    message.set("Help")
    path = ""
    text.delete(1.0, "end")  # delete from char n1 to end
    text.insert(1.0, "Welcome to Simple Text, a user-friendly text editor that makes it easy to create and edit documents.\n\nTo get started, you can use the options in the top menu to create a new document, open an existing one, or save changes to a document.\n\nYou can also use keyboard shortcuts to speed up your text editing tasks, such as copying and pasting text, undoing changes, and more. In the workspace, you can write and edit your text documents. You will see that there are various tools available to assist you in this task, such as the spell checker, search and replace text, and line numbering.\n\nIn addition, you can customize the appearance of the Simple Text editor, such as the font type, size, and color, to adapt it to your preferences. \n\nRemember that you can always find help and support in the Help section of Simple Text, where you can find detailed information about the functions and features of the editor, as well as tips and suggestions to optimize your workflow. Enjoy your experience in Simple Text and do not hesitate to contact us if you need additional help!")
    root.title('Simple Text')


def getInfo():
    global path
    message.set("Info")
    path = ""
    text.delete(1.0, "end")  # delete from char n1 to end
    text.insert(1.0, "Welcome to Simple Text, the user-friendly text editor designed to make your writing and editing tasks as easy and efficient as possible. With Simple Text, you can create and edit documents with ease and take advantage of helpful features such as spell checking and line numbering. We hope you enjoy using Simple Text and that it helps you to be more productive and efficient in your work!")
    root.title('Simple Text')


# root
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
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(menu=filemenu, label="File")


# editmenu
editmenu = Menu(menubar, tearoff=0)
# editmenu.add_command(label="Search", command=search)  # fix position search first
editmenu.add_command(label="Clear text", command=cleartext)
menubar.add_cascade(menu=editmenu, label="Edit")


# infomenu
infomenu = Menu(menubar, tearoff=0)
infomenu.add_command(label="Help", command=getHelp)
infomenu.add_command(label="Info", command=getInfo)
menubar.add_cascade(menu=infomenu, label="Info")


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

# mainloop
root.mainloop()
