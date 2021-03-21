import tkinter as tk
import random

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.winfo_toplevel().geometry('300x400+300+100')
        self.createWidgets()

    def createWidgets(self):
        BOARD_SIZE = 4
        TOP_WIDTH, TOP_HEIGHT = 10, 4

        top=self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        for i in range(BOARD_SIZE):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)
        self.rowconfigure(BOARD_SIZE, weight=1)
        # menu
        self.NewButton = tk.Button(self, text='New', command = self.restart, width = TOP_WIDTH, height = TOP_HEIGHT)
        self.ExitButton = tk.Button(self, text='Exit', command = self.quit, width = TOP_WIDTH, height = TOP_HEIGHT)

        self.ExitButton.grid(row = 0, column = 2, columnspan = 2)
        self.NewButton.grid(row = 0, column = 0, columnspan = 2)
        # buttons
        self.buttons, self.numbers = list(), list(range(15))
        random.shuffle(self.numbers)

        for i in range(len(self.numbers)):
            number = self.numbers[i]
            self.buttons.append(tk.Button(self, text=str(number+1)))
            self.buttons[-1].grid(row=i//4+1, column=i%4, sticky="SEWN")

    def restart(self):
        self.destroy()
        self.__init__()


app = Application()
app.master.title('GAME 15')
app.mainloop()