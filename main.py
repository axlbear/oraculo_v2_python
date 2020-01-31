# IMPORTS
import tkinter as tk
import tkinter.filedialog as fd
import tkinter.ttk as ttk
import tkinter.messagebox as ms
import os
import random
import openpyxl

# FUNCTIONS

# INIT
os.system('cls')
root = tk.Tk()

# GUI

# MENU
menuBar = tk.Menu(root)
firstMenu = tk.Menu(menuBar, tearoff=0)
secondMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Primeiro Menu", menu=firstMenu)
menuBar.add_cascade(label="Segundo Menu", menu=secondMenu)

firstMenu.add_command(label="Opção #1")
firstMenu.add_command(label="Opção #2")
firstMenu.add_command(label="Opção #3")
firstMenu.add_command(label="Opção #4")
firstMenu.add_command(label="Opção #5")

secondMenu.add_command(label='Opção #1')
secondMenu.add_command(label='Opção #2')
secondMenu.add_command(label='Opção #3')
secondMenu.add_command(label='Opção #4')
secondMenu.add_command(label='Opção #5')

# CONFIG
if __name__ == "__main__":
    root.title('Oráculo II - RPG Solo - Criado de Campanhas')
    root.state('zoomed')
    root.config(menu=menuBar)
    root.mainloop()