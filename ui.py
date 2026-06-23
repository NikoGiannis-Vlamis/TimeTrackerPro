import tkinter as tk

class App:
    def __init__(self, root):
        root.title("Time Tracker Pro")
        root.geometry("400x300")

def run():
    root=tk.Tk()
    App(root)
    root.mainloop()