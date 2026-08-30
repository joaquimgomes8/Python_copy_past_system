import tkinter as tk
root = tk.Tk()
root.title("AZShip System")
root.geometry("400x300")
root.attributes('-topmost',True)
#===============================
def bom_dia():
    return print("Bom dia")
#===============================

button = tk.Button(root, text="Bom diaa")
button.pack(pady=20)

#===============================
root.mainloop()