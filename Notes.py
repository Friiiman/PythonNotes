from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import datetime
 
root = Tk()
root.title("Заметки")
root.geometry("400x400")
 
root.grid_rowconfigure(index = 0, weight = 1)
root.grid_columnconfigure(index = 0, weight = 1)
root.grid_columnconfigure(index =1, weight = 1)
 
text_editor = Text()
text_editor.grid(column = 0, columnspan = 2, row = 0)
 
def open_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r") as file:
            text = file.read()
            text_editor.delete("1.0", END)
            text_editor.insert("1.0", text)
 
def save_file():
    now = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    filepath = filedialog.asksaveasfilename(defaultextension = now + '.json')
    if filepath != "":
        text = text_editor.get("1.0", END)
        with open(filepath, "w") as file:
            file.write(text)
 
open_button = ttk.Button(text = "Открыть файл", command = open_file)
open_button.grid(column = 0, row = 1, sticky = NSEW, padx = 10)
 
save_button = ttk.Button(text = "Сохранить файл", command = save_file)
save_button.grid(column = 1, row = 1, sticky = NSEW, padx = 10)
 
root.mainloop()
