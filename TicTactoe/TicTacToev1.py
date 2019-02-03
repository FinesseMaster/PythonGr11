"""
TicTacToe
Michael Kagnew and Sandra Fang

NO working reset button, does not end when immediate winner, just the bare bones"""


from tkinter import *
from tkinter import messagebox 

root= Tk()
root.title("Michael And Sandula's tic tac toe")

bclick= True

def tictactoe(buttons):
    
    global bclick
    if buttons["text"]==" " and bclick ==True:
        buttons["text"]= "X"
        bclick =False

    elif buttons["text"]==" "and bclick ==False:
         buttons["text"]= "O"
         bclick =True

    elif(button1["text"] == "X" and button2["text"]== "X" and button3 ["text"]== "X" or
         button1["text"] == "X" and button5["text"]== "X" and button9 ["text"]== "X" or
         button1["text"] == "X" and button4["text"]== "X" and button7 ["text"]== "X" or
         button4["text"] == "X" and button5["text"]== "X" and  button6 ["text"]== "X" or
         button7["text"] == "X" and button8["text"]== "X" and  button9 ["text"]== "X" or
         button3["text"] == "X" and button5["text"]== "X" and  button7 ["text"]== "X" or
         button2["text"] == "X" and button5["text"]== "X" and  button8 ["text"]== "X" or
         button3["text"] == "X" and button6["text"]== "X" and  button9 ["text"]== "X" ):
       
         messagebox.showinfo("Winner", "WINNER WINNER CHICKEN DINNER user X!")
         
         
         
         
    elif(button1["text"] == "O" and button2["text"]== "O" and  button3 ["text"]== "O" or
         button1["text"] == "O" and button5["text"]== "O" and  button9 ["text"]== "O" or
         button1["text"] == "O" and button4["text"]== "O" and  button7 ["text"]== "O" or
         button4["text"] == "O" and button5["text"]== "O" and  button6 ["text"]== "O" or
         button7["text"] == "O" and button8["text"]== "O" and  button9 ["text"]== "O" or
         button3["text"] == "O" and button5["text"]== "O" and  button7 ["text"]== "O" or
         button2["text"] == "O" and button5["text"]== "O" and button8 ["text"]== "O" or
         button3["text"] == "O" and button6["text"]== "O" and  button9 ["text"]== "O" ):
        
         messagebox.showinfo("Winner", "WINNER WINNER CHICKEN DINNER user O!")
         
    


buttons=StringVar()
button1=Button(root, text=" ", font=("Arial 35 bold"), height=4, width= 8, command=lambda:tictactoe(button1))
button1.grid(row=1, column=0, sticky=W+E+N+S)

button2=Button(root, text=" ", font=("Arial 35 bold"), height=4, width= 8, command=lambda:tictactoe(button2))
button2.grid(row=1, column=1, sticky=W+E+N+S)

button3=Button(root, text=" ", font=("Arial 35 bold"), height=4, width= 8, command=lambda:tictactoe(button3))
button3.grid(row=1, column=2, sticky=W+E+N+S)

button4=Button(root, text=" ", font=("Arial 35 bold"), height=4, width= 8, command=lambda:tictactoe(button4))
button4.grid(row=2, column=0, sticky=W+E+N+S)

button5=Button(root, text=" ", font=("Arial 35 bold"), height=4, width= 8, command=lambda:tictactoe(button5))
button5.grid(row=2, column=1, sticky=W+E+N+S)

button6=Button(root, text=" ", font=("Arial 35 bold"), height=4, width= 8, command=lambda:tictactoe(button6))
button6.grid(row=2, column=2, sticky=W+E+N+S)

button7=Button(root, text=" ", font=("Arial 35 bold"), height=4, width= 8, command=lambda:tictactoe(button7))
button7.grid(row=3, column=0, sticky=W+E+N+S)

button8=Button(root, text=" ", font=("Arial 35 bold"), height=4, width= 8, command=lambda:tictactoe(button8))
button8.grid(row=3, column=1, sticky=W+E+N+S)


button9=Button(root, text=" ", font=("Arial 35 bold"), height=4, width= 8, command=lambda:tictactoe(button9))
button9.grid(row=3, column=2, sticky=W+E+N+S)

root.mainloop()
