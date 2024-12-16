import tkinter as tk
from calculator import Calculator

def main():
    root = tk.Tk()

    label = tk.Label(root, text="Hello Bueno")
    label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()