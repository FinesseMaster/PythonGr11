"""
TicTacToe
Michael Kagnew and Sandra Fang

Has working reset button, what the game should be"""
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Michael And Sandula's tic tac toe")
messagebox.showinfo("Rules", "Welcome to Tic Tac Toe! The rules are very straight forward, get 3 in a row diagonally, vertically, or horizontally to win!")
messagebox.showinfo("Placeholders", "user 1, you are X's, user 2 you are O's")


#variable that changes from false(user X) to true (user O), global variable if all sqaures filled and tie game#
bclick = True
counter = int(0)

#The function for the changing between X and O, as well as who wins#
def tictactoe(buttons):
    global bclick
    global counter
    if buttons["text"]==" " and bclick == True:
        buttons["text"]= "X"
        counter+= 1
        bclick = False
        
        if(button1["text"] == "X" and button2["text"]== "X" and button3 ["text"]== "X" or
         button1["text"] == "X" and button5["text"]== "X" and button9 ["text"]== "X" or
         button1["text"] == "X" and button4["text"]== "X" and button7 ["text"]== "X" or
         button4["text"] == "X" and button5["text"]== "X" and  button6 ["text"]== "X" or
         button7["text"] == "X" and button8["text"]== "X" and  button9 ["text"]== "X" or
         button3["text"] == "X" and button5["text"]== "X" and  button7 ["text"]== "X" or
         button2["text"] == "X" and button5["text"]== "X" and  button8 ["text"]== "X" or
         button3["text"] == "X" and button6["text"]== "X" and  button9 ["text"]== "X" ):
            messagebox.showinfo("Results", "WINNER WINNER CHICKEN DINNER user X!")
        if counter == 9:
            messagebox.showinfo("Results", "TIE GAME!")

   

    elif buttons["text"]==" "and bclick == False:
         buttons["text"]= "O"
         counter+= 1
         bclick =True
         
         if(button1["text"] == "O" and button2["text"]== "O" and  button3 ["text"]== "O" or
         button1["text"] == "O" and button5["text"]== "O" and  button9 ["text"]== "O" or
         button1["text"] == "O" and button4["text"]== "O" and  button7 ["text"]== "O" or
         button4["text"] == "O" and button5["text"]== "O" and  button6 ["text"]== "O" or
         button7["text"] == "O" and button8["text"]== "O" and  button9 ["text"]== "O" or
         button3["text"] == "O" and button5["text"]== "O" and  button7 ["text"]== "O" or
         button2["text"] == "O" and button5["text"]== "O" and button8 ["text"]== "O" or
         button3["text"] == "O" and button6["text"]== "O" and  button9 ["text"]== "O" ):
             messagebox.showinfo("Results", "WINNER WINNER CHICKEN DINNER user O!")

#to reset, clears each button of its placeholder so user can play again#             
def resetGame():
    global counter
    global bclick

    bclick = True
    counter = 0
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "


#location of each button, its size as well as the function it follows, which is tictactoe#
buttons=StringVar()
button1=Button(root, text=" ", font=("Arial 35 bold"), height=3, width= 8, command=lambda:tictactoe(button1))
button1.grid(row=1, column=0, sticky=W+E+N+S)

button2=Button(root, text=" ", font=("Arial 35 bold"), height=3, width= 8, command=lambda:tictactoe(button2))
button2.grid(row=1, column=1, sticky=W+E+N+S)

button3=Button(root, text=" ", font=("Arial 35 bold"), height=3, width= 8, command=lambda:tictactoe(button3))
button3.grid(row=1, column=2, sticky=W+E+N+S)

button4=Button(root, text=" ", font=("Arial 35 bold"), height=3, width= 8, command=lambda:tictactoe(button4))
button4.grid(row=2, column=0, sticky=W+E+N+S)

button5=Button(root, text=" ", font=("Arial 35 bold"), height=3, width= 8, command=lambda:tictactoe(button5))
button5.grid(row=2, column=1, sticky=W+E+N+S)

button6=Button(root, text=" ", font=("Arial 35 bold"), height=3, width= 8, command=lambda:tictactoe(button6))
button6.grid(row=2, column=2, sticky=W+E+N+S)

button7=Button(root, text=" ", font=("Arial 35 bold"), height=3, width= 8, command=lambda:tictactoe(button7))
button7.grid(row=3, column=0, sticky=W+E+N+S)

button8=Button(root, text=" ", font=("Arial 35 bold"), height=3, width= 8, command=lambda:tictactoe(button8))
button8.grid(row=3, column=1, sticky=W+E+N+S)

button9=Button(root, text=" ", font=("Arial 35 bold"), height=3, width= 8, command=lambda:tictactoe(button9))
button9.grid(row=3, column=2, sticky=W+E+N+S)

#this is seperate from the other buttons, functions as the reset#
button10=Button(root, text="Reset",font=("Arial 35 bold"), height=2, width=4, command=resetGame)
button10.grid(row=4, column=1, sticky=W+E+N+S,columnspan=1)



root.mainloop()
