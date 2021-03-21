import tkinter as tk
import random
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.winfo_toplevel().geometry('300x400+300+100')
        self.createWidgets()

    def createWidgets(self):
        self.BOARD_SIZE = 4
        TOP_WIDTH, TOP_HEIGHT = 10, 4

        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        for i in range(self.BOARD_SIZE):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)
        self.rowconfigure(self.BOARD_SIZE, weight=1)
        # menu
        self.NewButton = tk.Button(self, text='New', command = self.restart, width = TOP_WIDTH, height = TOP_HEIGHT)
        self.ExitButton = tk.Button(self, text='Exit', command = self.quit, width = TOP_WIDTH, height = TOP_HEIGHT)

        self.ExitButton.grid(row = 0, column = 2, columnspan = 2)
        self.NewButton.grid(row = 0, column = 0, columnspan = 2)
        # buttons
        self.buttons, self.numbers = list(), list(range(15))
        self.empty_location = (4, 3)
        random.shuffle(self.numbers)
        while not self.solvable_combination(self.numbers):
            random.shuffle(self.numbers)

        for i in range(len(self.numbers)):
            number = self.numbers[i]
            row, column = i//self.BOARD_SIZE+1, i%self.BOARD_SIZE
            self.buttons.append(tk.Button(self, text = str(number+1), command = lambda x = i: self.click(x)))
            self.buttons[-1].grid(row = row, column = column, sticky = "SEWN")


    def restart(self):
        self.destroy()
        self.__init__()

    def click(self, index):
        current_location = (self.buttons[index].grid_info()['row'], self.buttons[index].grid_info()['column'])
        new_location = self.empty_location
        row_diff = abs(new_location[0] - current_location[0])
        column_diff = abs(new_location[1] - current_location[1])
        if (row_diff == 1 and column_diff == 0) or (row_diff == 0 and column_diff == 1):
            self.buttons[index].grid(row = new_location[0], column = new_location[1], sticky="SEWN")
            self.empty_location = current_location
        if self.correct_board():
            messagebox.showinfo('', 'YOU ARE A WINNER!')
            self.restart()
    
    def correct_board(self):
        for i in range(len(self.numbers)):
            current_location = (self.buttons[i].grid_info()['row'], self.buttons[i].grid_info()['column'])
            text = int(self.buttons[i].cget('text')) - 1
            index = (current_location[0] - 1) * self.BOARD_SIZE + current_location[1]
            print(text, index)
            if text != index:
                return False
        return True

    def solvable_combination(self, numbers_list):
        inv = 0
        for i in range(14):
            for j in range(i+1, 15):
                if numbers_list[i] > numbers_list[j]: 
                    inv+=1
        return True if inv%2==0 else False
    

app = Application()
app.master.title('GAME 15')
app.mainloop()