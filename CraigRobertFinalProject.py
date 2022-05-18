import tkinter as tk #Imports the module tkinter, using 'tk' for ease of use later

#Defines the main window, as well as its buttons that links to other windows, functions, and labels. 
class mainWindow:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x400")
        self.frame = tk.Frame(self.master)
        self.label = tk.Label(master, text=f"Select a pizza")
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.butnew("Pepperoni", "pepperoni", window1)
        self.butnew("Cheese", "cheese", window2)
        self.quitButton.pack()
        self.label.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy() #Used in each window to 'close' or delete the windows once the user is finished.

    def butnew(self, text, type, _class):
        tk.Button(self.frame, text = text, width = 25, command = lambda: self.new_window(type, _class)).pack() #What the buttons will show and variables to be used in other windows

    def new_window(self, type, _class):
        self.newWindow = tk.Toplevel(self.master)
        _class(self.newWindow, type)

#Defines the first window, which shows when the user selects pepperoni on the main window.
class window1:
    def __init__(self, master, type):
        self.master = master
        self.master.geometry("400x400+400+400")
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Order and exit', width = 25, command = self.close_windows)
        self.label = tk.Label(master, text=f"You have selected {type}")
        self.label.pack()
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

#Defines the second window, which shows when the user selects cheese on the main window.
class window2:
    def __init__(self, master, type):
        self.master = master
        self.master.geometry("400x400+400+400")
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Order and exit', width = 25, command = self.close_windows)
        self.label = tk.Label(master, text=f"You have selected {type}")
        self.label.pack()
        self.label2 = tk.Label(master, text="Cheese pizzas are currently half off!")
        self.label2.pack()
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


def main(): 
    root = tk.Tk()
    app = mainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()