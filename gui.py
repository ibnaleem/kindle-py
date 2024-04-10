import tkinter as tk

class TkGUI(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Kindle.py - eBook Reader")
        self.geometry("1200x800")

app = TkGUI()
app.mainloop()
