# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:01:57 2020

@author: bhaum
"""

from tkinter import *
from tkinter import ttk            
root = Tk()
root.title("TIC TAC TOE")

b=[[0,0,0],
   [0,0,0],
   [0,0,0]]
states= [[0,0,0],
         [0,0,0],
         [0,0,0]]

k = 0
mylabel = ttk.Label(root,font=("Arial",20), text="TictakToe Game")
mylabel.grid(column=1, row=0) 
for i in range(3):
    for j in range(3):
        b[i][j]=Button(root,font=("Arial",60),width=4,bg='powder blue',
                       command= lambda r=i,c=j:callback(r,c))

        b[i][j].grid(row=i+2,column=j)

mylabel1 = ttk.Label(root,font=("Arial",20), text="Player 1 Turn")
mylabel1.grid(column=1, row=1) 
player='x'
stop_game = False
root.mainloop()

def callback(r,c):
    global player,k
    if player=='x' and states [r][c]==0 and stop_game== False:
        b[r][c].configure(text='x' ,fg='blue',bg='white')
        states[r][c] ='x'
        player= 'o'
        k = k+1
        mylabel1.configure(text="Player 2 Turn")
    
        
    if player=='o' and states [r][c]==0 and stop_game== False:
        b[r][c].configure(text='o' ,fg='orange',bg='white')
        states[r][c] ='o'
        player= 'x'
        k=k+1
        mylabel1.configure(text="Player 1 Turn")
    
        
    if(k<9):
        check_for_winner()
        print(k)
    else:
        mylabel1.configure(text="No Player has won")
    
        
    
def check_for_winner():
    global stop_game
    
    for i in range(3):
        if states[i][0] == states[i][1]==states[i][2]!=0:
            b[i][0].config(bg='black')
            b[i][1].config(bg='black')
            b[i][2].config(bg='black')
            mylabel1.configure(text="You have won")
            stop_game =True
    for i in range(3):
        if states[0][i] == states[1][i]==states[2][i]!=0:
            b[0][i].config(bg='black')
            b[1][i].config(bg='black')
            b[2][i].config(bg='black')
            mylabel1.configure(text="You have won")
            stop_game =True

        if states[0][0] == states[1][1]==states[2][2]!=0:
            b[0][0].config(bg='black')
            b[1][1].config(bg='black')
            b[2][2].config(bg='black')
            mylabel1.configure(text="You have won")
            stop_game =True

        if states[2][0] == states[1][1]==states[0][2]!=0:
            b[2][0].config(bg='black')
            b[1][1].config(bg='black')
            b[0][2].config(bg='black')
            mylabel1.configure(text="You have won")
            stop_game =True
        
            

        
