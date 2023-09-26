import tkinter as tk

def run_gui():
    window = tk.Tk()
    window.title("Tkinter GUI")
    label = tk.Label(window, text="Hello, Tkinter!")
    label.pack()
    window.mainloop()

if __name__ == "__main__":
    run_gui()
