#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: sarasamy
"""

MARGIN = 10  # Pixels around the board


########### ------IMPORTS-------########### 

import tkinter as tk 
from math import floor
from copy import deepcopy

########### ------HELPER FUNCTIONS-------########### 

def apply_rule(field, original, i, j, neighbours, rule):
    if original[i][j] == 1 and str(neighbours.count(1)) not in rule[0]:
        field[i][j] = 0
    if original[i][j] == 0 and str(neighbours.count(1)) in rule[1]:
        field[i][j] = 1

########### ------LIFE LOGIC CLASS-------###########                        
                    
class Life:
    def __init__(self, seed, rule, edge):
        self.S = seed
        self.rule = rule
        self.b = edge
        
    def __str__(self):
        result = ''.join(str(row) for row in self.S).replace('[', '').replace(']', ' \n').replace(',', '').replace(' ', '')
        return result[:-1]
            
    def tick(self):
        rows = len(self.S)
        cols = len(self.S[0])
        
        SB_form = self.rule.split("/")
        
        field = deepcopy(self.S)
                
        for i in range(rows):
            for j in range(cols):
                if i == 0:
                    
                    if j == 0:
                        #Case: Top left Cell
                        neighbours = [self.S[i][j+1],self.S[i+1][j],self.S[i+1][j+1]]
                        if self.b == 1:
                            neighbours +=  [0 for val in range(5)]
                        elif self.b == 2:
                            neighbours +=  [1 for val in range(5)]
                        else:
                            neighbours += [self.S[i][cols-1],self.S[i+1][cols-1],self.S[rows-1][cols-1],self.S[rows-1][0],self.S[rows-1][1]]
                        apply_rule(field, self.S, i, j, neighbours, SB_form)
                    elif j == cols-1:
                        #Case: Top right Cell
                        neighbours = [self.S[i+1][j],self.S[i+1][j-1],self.S[i][j-1]]
                        if self.b == 1:
                            neighbours +=  [0 for val in range(5)]
                        elif self.b == 2:
                            neighbours +=  [1 for val in range(5)]
                        else:
                            neighbours += [self.S[0][0],self.S[1][0],self.S[rows-1][cols-1],self.S[rows-1][cols-2],self.S[rows-1][0]]
                        apply_rule(field, self.S, i, j, neighbours, SB_form)
                    else:
                        #Top Rows cells
                        neighbours = [self.S[i][j-1],self.S[i+1][j-1],self.S[i+1][j],self.S[i+1][j+1],self.S[i][j+1]]
                        if self.b == 1:
                            neighbours +=  [0 for val in range(3)]
                        elif self.b == 2:
                            neighbours +=  [1 for val in range(3)]
                        else:
                            neighbours += [self.S[rows-1][j-1],self.S[rows-1][j],self.S[rows-1][j+1]]
                        apply_rule(field, self.S, i, j, neighbours, SB_form)
                        
                elif i == rows-1:
                    if j == 0:
                        #Case: bottom left cell
                        neighbours = [self.S[i-1][j],self.S[i-1][j+1],self.S[i][j+1]]
                        if self.b == 1:
                            neighbours +=  [0 for val in range(5)]
                        elif self.b == 2:
                            neighbours +=  [1 for val in range(5)]
                        else:
                            neighbours += [self.S[0][0],self.S[0][1],self.S[i][cols-1],self.S[i-1][cols-1],self.S[0][cols-1]]
                        apply_rule(field, self.S, i, j, neighbours, SB_form)
                    elif j == cols-1:
                        #Case: Bottom right cell
                        neighbours = [self.S[i-1][j],self.S[i-1][j-1],self.S[i][j-1]]
                        if self.b == 1:
                            neighbours +=  [0 for val in range(5)]
                        elif self.b == 2:
                            neighbours +=  [1 for val in range(5)]
                        else:
                            neighbours += [self.S[0][0],self.S[0][j],self.S[0][j-1],self.S[i][0],self.S[i-1][0]]
                        apply_rule(field, self.S, i, j, neighbours, SB_form)
                    else:
                        #Last row cells
                        neighbours = [self.S[i][j-1],self.S[i-1][j-1],self.S[i-1][j],self.S[i-1][j+1],self.S[i][j+1]]
                        if self.b == 1:
                            neighbours +=  [0 for val in range(3)]
                        elif self.b == 2:
                            neighbours +=  [1 for val in range(3)]
                        else:
                            neighbours += [self.S[0][j-1],self.S[0][j],self.S[0][j+1]]
                        apply_rule(field, self.S, i, j, neighbours, SB_form)
                    
                else:
                    if j == 0:
                        #First col cells
                        neighbours = [self.S[i-1][j],self.S[i-1][j+1],self.S[i][j+1],self.S[i+1][j+1],self.S[i+1][j]]
                        if self.b == 1:
                            neighbours +=  [0 for val in range(3)]
                        elif self.b == 2:
                            neighbours +=  [1 for val in range(3)]
                        else:
                            neighbours += [self.S[i-1][cols-1],self.S[i][cols-1],self.S[i+1][cols-1]]
                        apply_rule(field, self.S, i, j, neighbours, SB_form)
                    elif j == cols-1:
                        #Last col cells
                        neighbours = [self.S[i-1][j],self.S[i-1][j-1],self.S[i][j-1],self.S[i+1][j-1],self.S[i+1][j]]
                        if self.b == 1:
                            neighbours +=  [0 for val in range(3)]
                        elif self.b == 2:
                            neighbours +=  [1 for val in range(3)]
                        else:
                            neighbours += [self.S[i-1][0],self.S[i][0],self.S[i+1][0]]
                        apply_rule(field, self.S, i, j, neighbours, SB_form)
                    else:
                        #Normal cells
                        neighbours = [self.S[i][j-1],self.S[i-1][j-1],self.S[i-1][j],self.S[i-1][j+1],self.S[i][j+1],self.S[i+1][j+1],self.S[i+1][j],self.S[i+1][j-1]]
                        apply_rule(field, self.S, i, j, neighbours, SB_form)
        self.S = field
        
        
########### ------LIFE GUI CLASS-------###########       

class LifeUI(tk.Tk):
    def __init__(self, game, SIDE):
        super().__init__()
        
        self.game = game
        self.running = True
        
        self.grid_rows = len(game.S)
        self.grid_cols = len(game.S[0])
        self.side = SIDE
        
        self.width = self.grid_cols*self.side + 2*MARGIN
        self.height = self.grid_rows*self.side + 2*MARGIN
        
        self.frame = tk.Frame(self)
        self.frame.grid(padx=20, pady=20)
        
        self.resizable(False, False)
        self.configure(background="white")
        self.title("Game of Life")
        
        tk.Label(self.frame, text="Regel", bg="white").grid(row=0,column=50)
        self.regel = tk.Entry(self.frame)
        self.regel.bind('<Return>', self.get_rule)
        self.regel.grid(row=1,column=50)
        self.regel.insert(tk.END,"%s" %(game.rule))
        
        self.canvas = tk.Canvas(self.frame,width=self.width,height=self.height,bg="white")
        self.canvas.grid(columnspan=self.width, rowspan=self.height, column = floor(self.grid_cols*self.side/2), row = 5)
        self.canvas.bind("<Button-1>", self.cell_clicked)
        
        tk.Button(self.frame,text="Start Game",command=self.start_game, bg="white").grid(row=1, column=self.grid_cols*self.side+10, pady=4)
        tk.Button(self.frame,text="Stop Game",command=self.stop_game, bg="white").grid(row=1, column=self.grid_cols*self.side+20, pady=4)
        tk.Button(self.frame,text="Clear",command=self.clear_game, bg="white").grid(row=1, column=self.grid_cols*self.side+30, pady=4)
        
        self.var = tk.IntVar()
        
        tk.Radiobutton(self.frame,text="Dead",command=self.sel_edge, bg="white", value=1, variable=self.var).grid(row = 0, column =(2*self.grid_cols*self.side))
        tk.Radiobutton(self.frame,text="Alive",command=self.sel_edge, bg="white",value=2, variable=self.var).grid(row = 1, column =(2*self.grid_cols*self.side))
        tk.Radiobutton(self.frame,text="Donut",command=self.sel_edge, bg="white", value=3, variable=self.var).grid(row = 2, column =(2*self.grid_cols*self.side))

        self.draw_grid(self.grid_rows, self.grid_cols)

        
    def color_rectangle(self, row, col):
        if row >= 0 and col >= 0:
            x0 = MARGIN + col * self.side + 1
            y0 = MARGIN + row * self.side + 1
            x1 = MARGIN + (col + 1) * self.side - 1
            y1 = MARGIN + (row + 1) * self.side - 1
            if self.game.S[row][col] == 0:
                color = "white"
                self.canvas.create_rectangle(x0-1, y0-1, x1+1, y1+1, fill=color)
            elif self.game.S[row][col] == 1:
                color = "black"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
                
    def loop_step(self):
        self.game.tick()
        for row in range(self.grid_rows):
            for col in range(self.grid_cols):
                self.color_rectangle(row,col)
                
    def start_loop(self):
        if self.running:
            self.loop_step()
            
        self.after(1000,self.start_loop)
        
    def start_game(self):
        self.running = True
        self.canvas.unbind("<Button-1>")
        self.start_loop()
    
    def stop_game(self):
        self.running = False
        self.canvas.bind("<Button-1>", self.cell_clicked)
            
    def get_rule(self, event):
        if self.running == True:
            self.stop_game()           
        rule = self.regel.get()
        self.game.rule = rule
                 
    
    def clear_game(self):
        for i in range(self.grid_rows):
            for j in range(self.grid_cols):
                if  self.game.S[i][j] == 1:
                    self.game.S[i][j] = 0
                    self.color_rectangle(i,j)       
        self.stop_game()        
        
    def sel_edge(self):
        if self.running == True:
            self.stop_game()
            
        if self.var.get() == 1:
            self.game.b = 1
        if self.var.get() == 2:
            self.game.b = 2
        if self.var.get() == 3:
            self.game.b = 3
            
    
    def cell_clicked(self, event):
        x, y = event.x, event.y
        i, j = 0, 0
        if (MARGIN < x < self.width - MARGIN and MARGIN < y < self.height - MARGIN):

            i = floor((y - MARGIN)/self.side)
            j = floor((x - MARGIN)/self.side)
            if  self.game.S[i][j] == 0:
                self.game.S[i][j] = 1
                self.color_rectangle(i,j)
            else:
                self.game.S[i][j] = 0
                self.color_rectangle(i,j)
                

    def draw_grid(self, grid_rows, grid_cols):
        
        for i in range(grid_cols+1):
            color = "black"

            x0 = MARGIN + i * self.side
            y0 = MARGIN
            x1 = MARGIN + i * self.side
            y1 = y0+(grid_rows*self.side)
            self.canvas.create_line(x0, y0, x1, y1, fill=color)
            
        for j in range(grid_rows+1):
            
            color = "black"
            x0 = MARGIN
            y0 = MARGIN + j * self.side
            x1 = x0+(grid_cols*self.side)
            y1 = MARGIN + j * self.side
            self.canvas.create_line(x0, y0, x1, y1, fill=color)
    
                    

#### ---- MAIN ---- ####

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Enter Data")
        self.geometry("300x125")

        tk.Label(self, text="Anzahl Zeile").grid(row=0)
        tk.Label(self, text="Anzahl Spalten").grid(row=1)
        tk.Label(self, text="Groß Grid").grid(row=2)

        self.e_Zeile = tk.Entry(self)
        self.e_Spalten = tk.Entry(self)
        self.size_grid = tk.Entry(self)
        self.e_Zeile.grid(row=0, column=1)
        self.e_Spalten.grid(row=1, column=1)
        self.size_grid.grid(row=2, column=1)
        
        tk.Button(self, text="Generate Playfield", command=self.generate_playfield).grid(row=5, column=1, sticky=tk.W, pady=4)
        
    def generate_playfield(self):
        rows = int(self.e_Zeile.get())
        cols = int(self.e_Spalten.get())
        size_grid = int(self.size_grid.get())
        
        self.destroy()
        
        game_grid = [[0] * cols for i in range(rows)]
        
        game = Life(game_grid,"23/3",1)
        gui = LifeUI(game, size_grid)
        
        gui.mainloop()
        

if __name__ == "__main__":
    root = Root()
    root.mainloop()
    
