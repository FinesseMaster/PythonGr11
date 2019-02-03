"""
TicTacToe
Michael Kagnew and Sandra Fang

NO First complete fail attempt at making a reset button, atrocious"""


from tkinter import *
from tkinter import messagebox
import sys
import os
messagebox.showinfo("Rules", "Rules are very straight forward, get 3 in a row diagonally, vertically, or horizontally to win!")
##class Window(Frame):
##    def __init__(self, master= None):
##        Frame.__init__(self, master)
##
##        self.master=master
##        self.init_window()
##
##    def init_window(self):
##        self.master.title("GUI")
##
##        self.pack(fill=BOTH, expand=1)
##
##        startButton= Button(self, text="Start", command=self.client_start)
##
##        startButton.place(x=30, y=30)
##
##    def client_start(self):
##        pass
##        
##
##root = Tk()
##w= Label(root, text="The Start")
##w.pack
##app=Window(root)






##
##def start(self):
##     break
##
##
##     bl=Button( text="Start", command=self)
##     bl.pack()
    
    
   

   









root= Tk()
root.title("Michael And Sandula's tic tac toe")

bclick= True
counter = int(0)




def tictactoe(buttons):
    global bclick
    global counter
    if buttons["text"]==" " and bclick ==True:
        buttons["text"]= "X"
        counter+= 1
        bclick =False
        
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

   

    elif buttons["text"]==" "and bclick ==False:
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


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
if __name__ == "__main__":
    answer = input("Do you want to restart this program ? ")
    if answer.lower().strip() in "y yes".split():
        restart_program()
root.mainloop()




