"""UCS Squad(Unit Convertor Squad)
Mrs.Luce
Group Members: Michael, Andrew, Victor
An application that is able to convert different temperatures, mass, time, and pressures
"""





from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askfloat
from tkinter.messagebox import showerror
import winsound
import time
unit1 = int(0)
unit2=int(0)
num=float(0)
root= Tk()

#labels, size, titles for the program, sets orange window color
production=Label(root,text="A UCSquad Production ©", width=50,bg= "#ffaa19", font=("Times New Roman", 10))
production.place(x=170,y=460)
title_label=Label(root,text="Converter", width=20,bg= "#ffaa19", font=("Courier", 35,"bold","italic"))
title_label.place(x=-33,y=50)
root.title("Converter") 
root.configure(background="#ffaa19") 
root.geometry ("500x500")


#incase for unexpected errors
class error(Exception):
    pass

#Function to place all the  different unit category buttons
def category(): 
    mas.place (x=125,y=150)
    distan.place (x=275,y=150)
    currenc.place(x=275,y=200)
    temp.place (x=125,y=200)
    tm.place(x = 125, y=250)
    pres.place(x = 275, y=250)



#Function to quit application, will close the window
def quitt():
    winsound.PlaySound(None, winsound.SND_ALIAS) 
    root.destroy()    

#when a category button is selected, all of them disappear
def byebuttons(): 
    distan.place_forget()
    mas.place_forget()
    temp.place_forget()
    tm.place_forget()
    pres.place_forget()
    currenc.place_forget()
    qui.place_forget()

#back function when a category is selected. Removes all buttons and places the category buttons back. Resets values
def back(): 
    global unit1
    global unit2
    gra.place_forget()
    kilogra.place_forget()
    milligra.place_forget()
    metr.place_forget()
    kilom.place_forget()
    centim.place_forget()
    celsi.place_forget()
    kelvi.place_forget()
    fahren.place_forget()
    sec.place_forget()
    mn.place_forget()
    hr.place_forget()
    atm.place_forget()
    kPas.place_forget()
    mmHg.place_forget()
    can.place_forget()
    euro.place_forget()
    us.place_forget()
    bac.place_forget()
    unit1=0
    category()
    qui.place(x=275,y=300)

#when a category is selected. calls on the units for their specified category
def mass(): 
    byebuttons()
    bac.place(x=275,y=300)
    gra.place (x=125,y=150)
    kilogra.place (x=125,y=200)
    milligra.place (x=125,y=250)
    
def distance():
    byebuttons()
    bac.place(x=275,y=300)
    metr.place (x=275,y=150)
    kilom.place (x=275,y=200)
    centim.place (x=275,y=250)

def temperature():
    byebuttons()
    bac.place(x=275,y=300)
    celsi.place (x=125,y=150)
    kelvi.place (x=125,y=200)
    fahren.place (x=125,y=250)
    
def currency():
    byebuttons()
    bac.place(x=275,y=300)
    can.place (x=275,y=150)
    us.place (x=275,y=200)
    euro.place (x=275,y=250)
    
def time():
    byebuttons()
    bac.place(x=275,y=300)
    sec.place (x=125,y=150)
    mn.place (x=125,y=200)
    hr.place (x=125,y=250)

def pressure():
    byebuttons()
    bac.place(x=275,y=300)
    atm.place (x=275,y=150)
    kPas.place (x=275,y=200)
    mmHg.place (x=275,y=250)

#when you finish a conversion, the buttons for the category you're in comes back
def buttons():
    global unit1
    if unit1 == 1 or unit1 == 2 or unit1 ==3:      
        mass()
    elif unit1==4 or unit1==5 or unit1==6:
        distance()
    elif unit1==7 or unit1==8 or unit1==9:
        currency()
    elif unit1==10 or unit1==11 or unit1==12:
        temperature()
    elif unit1==13 or unit1==14 or unit1==15:
        time()
    elif unit1==16 or unit1==17 or unit1==18:
        pressure()

 #resets choice values  
def again(): 
    global unit1
    global unit2
    buttons()
    unit1=0
    unit2=0
    messagebox.showinfo("RESTART", "Program has been reset")




"""
Logic for how to pick unit
if first unit selected, will set unit2 equal to the number associated with the function
Proceed to do math depending on the first unit was selected
else, when there is no first unit selected, set unit1 equal to the number associated with the function and ask for value
"""


def grams ():
    global unit1
    global unit2
    global num
    unit2 = 1 
    if unit1 == 2 and unit2 == 1: #if kilograms then grams is selected
        num *= 1000
        messagebox.showinfo("Result", "Your conversion is {0:.2f}g".format(num))
        again()
    elif unit1 ==3 and unit2 == 1: #if milligrams then grams is selected
        num /= 1000
        messagebox.showinfo("Result", "Your conversion is {0:.2f}g".format(num))
        again()
    else:
        unit1 = 1
        while True:#if this button is the first choice, then ask user for their value
            try:
                num = askfloat("Gram", "Please enter a number")
                if num == None:
                    unit1= 0
                    break
                elif num <= 0:
                    messagebox.showinfo("Error", "Your value can't be zero or negative")
                else:
                    messagebox.showinfo("ACCEPTED", "Your value has been accepted")
                    gra.place_forget()
                    break
            except (ValueError,error):
                showerror ("Error", "Enter a valid number")
                continue   
        
def kilog ():
    global unit1
    global unit2
    global num
    unit2 = 2 #sets this unit as second choice if first has been selected
    if unit1 == 1 and unit2 == 2: #if grams then kilograms is selected
        num /=1000
        messagebox.showinfo("Result", "Your conversion is {0:.2f}kg".format(num))
        again()
    elif unit1 ==3 and unit2 == 2: #if milligrams then kilograms is selected
        num /=1000000
        messagebox.showinfo("Result", "Your conversion is {0:.2f}kg".format(num))
        again()
    else:
        unit1 = 2
        while True:#if this button is the first choice, then ask user for their value
            try:
                num = askfloat("Kilogram", "Please enter a number")
                if num == None:
                    unit1= 0
                    break
                elif num <= 0:
                    messagebox.showinfo("Error", "Your value can't be zero or negative")
                else:
                    messagebox.showinfo("ACCEPTED", "Your value has been accepted")
                    kilogra.place_forget()
                    break
            except (ValueError,error):
                showerror ("Error", "Enter a valid number")
                continue
    
def millig ():
    global unit1
    global unit2
    global num
    unit2 = 3 #sets this unit as second choice if first has been selected
    if unit1 == 1 and unit2 == 3: #if grams then milligram is selected
        num *=1000
        messagebox.showinfo("Result", "Your conversion is {0:.2f}mg".format(num))
        again()
    elif unit1 ==2 and unit2 == 3: #if kilograms then milligrams is selected
        num *=1000000
        messagebox.showinfo("Result", "Your conversion is {0:.2f}mg".format(num))
        again()
    else:
        unit1 = 3
        while True:#if this button is the first choice, then ask user for their value
            try:
                num = askfloat("Milligram", "Please enter a number")
                if num == None: #if no value is entered
                    unit1= 0
                    break
                elif num <= 0:
                    messagebox.showinfo("Error", "Your value can't be zero or negative")
                else:
                    messagebox.showinfo("ACCEPTED", "Your value has been accepted")
                    milligra.place_forget()
                    break
            except (ValueError,error):
                showerror ("Error", "Enter a valid number")
                continue

#distance
def met ():
    global unit1
    global unit2
    global num
    unit2 = 4 #sets this unit as second choice if first has been selected
    if unit1 == 5 and unit2 == 4: #if kilometre then metre is selected
        num *=1000
        messagebox.showinfo("Result", "Your conversion is {0:.2f}m".format(num))
        again()
    elif unit1 ==6 and unit2 == 4: #if centimetre then metre is selected
        num /=100
        messagebox.showinfo("Result", "Your conversion is {0:.2f}m".format(num))
        again()
    else:
        unit1 = 4
        while True:#if this button is the first choice, then ask user for their value
            try:
                num = askfloat("Metre", "Please enter a number")
                if num == None:
                    unit1= 0
                    break
                elif num <= 0:
                    messagebox.showinfo("Error", "Your value can't be zero or negative")
                else:
                    messagebox.showinfo("ACCEPTED", "Your value has been accepted")
                    metr.place_forget()
                    break
            except (ValueError,error):
                
                showerror ("Error", "Enter a valid number")
                continue

        
def kilomet ():
    global unit1
    global unit2
    global num
    unit2 = 5 #sets this unit as second choice if first has been selected
    if unit1 == 4 and unit2 == 5: #if metre then kilometre is selected
        num /=1000
        messagebox.showinfo("Result", "Your conversion is {0:.2f}km".format(num))
        again()
    elif unit1 ==6 and unit2 == 5: #if centimetre then kilometre is selected
        num /=100000
        messagebox.showinfo("Result", "Your conversion is {0:.2f}km".format(num))
        again()
    else:
        unit1 = 5
        while True:#if this button is the first choice, then ask user for their value
            try:
                num = askfloat("Kilometre", "Please enter a number")
                if num == None:
                    unit1= 0
                    break
                elif num <= 0:
                    messagebox.showinfo("Error", "Your value can't be zero or negative")
                else:
                    messagebox.showinfo("ACCEPTED", "Your value has been accepted")
                    kilom.place_forget()
                    break
            except (ValueError,error):
                showerror ("Error", "Enter a valid number")
                continue

def centi ():
    global unit1
    global unit2
    global num
    unit2 = 6 #sets this unit as second choice if first has been selected
    if unit1 == 4 and unit2 == 6: #if metre then centimetre is selected
        num *=100
        messagebox.showinfo("Result", "Your conversion is {0:.2f}cm".format(num))
        again()
    elif unit1 ==5 and unit2 == 6: #if kilometre then centimetre is selected
        num *=100000
        messagebox.showinfo("Result", "Your conversion is {0:.2f}cm".format(num))
        again()
    else: #if the first choice has not been selected
        unit1 = 6
        while True: #if this button is the first choice, then ask user for their value
            try:
                num = askfloat("Centimetre", "Please enter a number")
                if num == None:
                    unit1= 0
                    break
                elif num <= 0:
                    messagebox.showinfo("Error", "Your value can't be zero or negative")
                else:
                    messagebox.showinfo("ACCEPTED", "Your value has been accepted")
                    centim.place_forget()
                    break
            except (ValueError,error):
                showerror ("Error", "Enter a valid number")
                continue



#definitions for the units added currency, temperature, pressure, and time


#currency added June 7
def cad():
    global unit1
    global unit2
    global num
    unit2 = 7 #sets this unit as second choice if first has been selected
    if unit1 == 8 and unit2 == 7: #if usd then cad is selected
        num *=1.30
        messagebox.showinfo("Result", "Your conversion is ${0:.2f}CAD".format(num))
        again()
    elif unit1 ==9 and unit2 == 7: #if euro then cad is selected
        num *=1.53
        messagebox.showinfo("Result", "Your conversion is ${0:.2f}CAD".format(num))
        again()
    else: #if the first choice has not been selected
        unit1 = 7
        while True: #if this button is the first choice, then ask user for their value
            try:
                num = askfloat("Canadian Dollar", "Please enter a number")
                if num == None:
                    unit1= 0
                    break
                elif num <= 0:
                    messagebox.showinfo("Error", "Your value can't be zero or negative")
                else:
                    messagebox.showinfo("ACCEPTED", "Your value has been accepted")
                    can.place_forget()
                    break
            except (ValueError,error):
                showerror ("Error", "Enter a valid number")
                continue
            
def usd():
    global unit1
    global unit2
    global num
    unit2 = 8 #sets this unit as second choice if first has been selected
    if unit1 == 7 and unit2 == 8: #if cad then usd is selected
        num *=0.77
        messagebox.showinfo("Result", "Your conversion is ${0:.2f}USD".format(num))
        again()
    elif unit1 ==9 and unit2 == 8: #if euro then usd is selected
        num *=1.18
        messagebox.showinfo("Result", "Your conversion is ${0:.2f}USD".format(num))
        again()
    else: #if the first choice has not been selected
        unit1 = 8
        while True: #if this button is the first choice, then ask user for their value
            try:
                num = askfloat("American Dollar", "Please enter a number")
                if num == None:
                    unit1= 0
                    break
                elif num <= 0:
                    messagebox.showinfo("Error", "Your value can't be zero or negative")
                else:
                    messagebox.showinfo("ACCEPTED", "Your value has been accepted")
                    us.place_forget()
                    break
            except (ValueError,error):
                showerror ("Error", "Enter a valid number")
                continue
def europ():
    global unit1
    global unit2
    global num
    unit2 = 9 #sets this unit as second choice if first has been selected
    if unit1 == 7 and unit2 == 9: #if cad then euro is selected
        num *=0.77
        messagebox.showinfo("Result", "Your conversion is ${0:.2f}EUR".format(num))
        again()
    elif unit1 ==8 and unit2 == 9: #if usd then euro is selected
        num *=0.85
        messagebox.showinfo("Result", "Your conversion is ${0:.2f}EUR".format(num))
        again()
    else: #if the first choice has not been selected
        unit1 = 9
        while True: #if this button is the first choice, then ask user for their value
            try:
                num = askfloat("European Dollar", "Please enter a number")
                if num == None:
                    unit1= 0
                    break
                elif num <= 0:
                    messagebox.showinfo("Error", "Your value can't be zero or negative")
                else:
                    messagebox.showinfo("ACCEPTED", "Your value has been accepted")
                    euro.place_forget()
                    break
            except (ValueError,error):
                showerror ("Error", "Enter a valid number")
                continue

#temperature added June 7
def celsius ():
    global unit1
    global unit2
    global num
    unit2 = 10 #sets this unit as second choice if first has been selected
    if unit1 == 11 and unit2 == 10: #if kelvins then celsius is selected
        num -= 273
        messagebox.showinfo("Result", "Your conversion is {0:.2f}°C".format(num))
        again()
    elif unit1 == 12 and unit2 == 10: #if fahrenheit then celsius is selected
        num = (num-32)*(5/9)
        messagebox.showinfo("Result", "Your conversion is {0:.2f}°C".format(num))
        again()
    else: #if the first choice has not been selected
        unit1 = 10
        while True: #if this button is the first choice, then ask user for their value
            try:
                num = askfloat("Celsius", "Please enter a number")
                if num == None:
                    unit1= 0
                    break
                elif num <= 0:
                    messagebox.showinfo("Error", "Your value can't be zero or negative")
                else:
                    messagebox.showinfo("ACCEPTED", "Your value has been accepted")
                    celsi.place_forget()
                    break
            except (ValueError,error):
                showerror ("Error", "Enter a valid number")
                continue

def kelvins ():
    global unit1
    global unit2
    global num
    unit2 = 11 #sets this unit as second choice if first has been selected
    if unit1 == 10 and unit2 == 11: #if celsius then kelvins is selected
        num += 273
        messagebox.showinfo("Result", "Your conversion is {0:.2f}K".format(num))
        again()
    elif unit1 == 12 and unit2 == 11: #if fahrenheit then kelvins is selected
        num = (num-32)*(5/9) + 273 
        messagebox.showinfo("Result", "Your conversion is {0:.2f}K".format(num))
        again()
    else: #if the first choice has not been selected
        unit1 = 11
        while True: #if this button is the first choice, then ask user for their value
            try:
                num = askfloat("Kelvins", "Please enter a number")
                if num == None:
                    unit1= 0
                    break
                elif num <= 0:
                    messagebox.showinfo("Error", "Your value can't be zero or negative")
                else:
                    messagebox.showinfo("ACCEPTED", "Your value has been accepted")
                    kelvi.place_forget()
                    break
            except (ValueError,error):
                showerror ("Error", "Enter a valid number")
                continue

def fahrenheit ():
    global unit1
    global unit2
    global num
    unit2 = 12 #sets this unit as second choice if first has been selected
    if unit1 == 10 and unit2 == 12: #if celsius then fahrenheit is selected
        num = (9/5)*num + 32
        messagebox.showinfo("Result", "Your conversion is {0:.2f}°F".format(num))
        again()
    elif unit1 == 11 and unit2 == 12: #if kelvins then fahrenheit is selected
        num = (9/5)*(num-273) + 32 
        messagebox.showinfo("Result", "Your conversion is {0:.2f}°F".format(num))
        again()
    else: #if the first choice has not been selected
        unit1 = 12
        while True: #if this button is the first choice, then ask user for their value
            try:
                num = askfloat("Celsius", "Please enter a number")
                if num == None:
                    unit1= 0
                    break
                elif num <= 0:
                    messagebox.showinfo("Error", "Your value can't be zero or negative")
                else:
                    messagebox.showinfo("ACCEPTED", "Your value has been accepted")
                    fahren.place_forget()
                    break
            except (ValueError,error):
                showerror ("Error", "Enter a valid number")
                continue

#time added June 7
def second ():
    global unit1
    global unit2
    global num
    unit2 = 13 #sets this unit as second choice if first has been selected
    if unit1 == 14 and unit2 == 13: #if minutes then seconds is selected
        num *= 60
        messagebox.showinfo("Result", "Your conversion is {0:.2f}secs".format(num))
        again()
    elif unit1 == 15 and unit2 == 13: #if hours then seconds is selected
        num *= 3600
        messagebox.showinfo("Result", "Your conversion is {0:.2f}secs".format(num))
        again()
    else: #if the first choice has not been selected
        unit1 = 13
        while True: #if this button is the first choice, then ask user for their value
            try:
                num = askfloat("Seconds", "Please enter a number")
                if num == None:
                    unit1= 0
                    break
                elif num <= 0:
                    messagebox.showinfo("Error", "Your value can't be zero or negative")
                else:
                    messagebox.showinfo("ACCEPTED", "Your value has been accepted")
                    sec.place_forget()
                    break
            except (ValueError,error):
                showerror ("Error", "Enter a valid number")
                continue

def minute ():
    global unit1
    global unit2
    global num
    unit2 = 14 #sets this unit as second choice if first has been selected
    if unit1 == 13 and unit2 == 14: #if seconds then minutes is selected
        num /= 60
        messagebox.showinfo("Result", "Your conversion is {0:.2f}mins".format(num))
        again()
    elif unit1 == 15 and unit2 == 14: #if hours then minutes is selected
        num *= 60
        messagebox.showinfo("Result", "Your conversion is {0:.2f}mins".format(num))
        again()
    else: #if the first choice has not been selected
        unit1 = 14
        while True: #if this button is the first choice, then ask user for their value
            try:
                num = askfloat("Minutes", "Please enter a number")
                if num == None:
                    unit1= 0
                    break
                elif num <= 0:
                    messagebox.showinfo("Error", "Your value can't be zero or negative")
                else:
                    messagebox.showinfo("ACCEPTED", "Your value has been accepted")
                    mn.place_forget()
                    break
            except (ValueError,error):
                showerror ("Error", "Enter a valid number")
                continue


def hour ():
    global unit1
    global unit2
    global num
    unit2 = 15 #sets this unit as second choice if first has been selected
    if unit1 == 13 and unit2 == 15: #if seconds then hours is selected
        num /= 3600
        messagebox.showinfo("Result", "Your conversion is {0:.2f}hrs".format(num))
        again()
    elif unit1 == 14 and unit2 == 15: #if minutes then hours is selected
        num /= 60
        messagebox.showinfo("Result", "Your conversion is {0:.2f}hrs".format(num))
        again()
    else: #if the first choice has not been selected
        unit1 = 15
        while True: #if this button is the first choice, then ask user for their value
            try:
                num = askfloat("Hours", "Please enter a number")
                if num == None:
                    unit1= 0
                    break
                elif num <= 0:
                    messagebox.showinfo("Error", "Your value can't be zero or negative")
                else:
                    messagebox.showinfo("ACCEPTED", "Your value has been accepted")
                    hr.place_forget()
                    break
            except (ValueError,error):
                showerror ("Error", "Enter a valid number")
                continue
            
#pressure added June 7    
def atmosphere ():
    global unit1
    global unit2
    global num
    unit2 = 16 #sets this unit as second choice if first has been selected
    if unit1 == 17 and unit2 == 16: #if kilopascals then atmospheres is selected
        num = num/101.325
        messagebox.showinfo("Result", "Your conversion is {0:.2f}Atm".format(num))
        again()
    elif unit1 == 18 and unit2 == 16: #if mmHg then atmospheres is selected
        num = num/760
        messagebox.showinfo("Result", "Your conversion is {0:.2f}Atm".format(num))
        again()
    else: #if the first choice has not been selected
        unit1 = 16
        while True: #if this button is the first choice, then ask user for their value
            try:
                num = askfloat("Atmospheres", "Please enter a number")
                if num == None:
                    unit1= 0
                    break
                elif num <= 0:
                    messagebox.showinfo("Error", "Your value can't be zero or negative")
                else:
                    messagebox.showinfo("ACCEPTED", "Your value has been accepted")
                    atm.place_forget()
                    break
            except (ValueError,error):
                showerror ("Error", "Enter a valid number")
                continue

def kPascal ():
    global unit1
    global unit2
    global num
    unit2 = 17 #sets this unit as second choice if first has been selected
    if unit1 == 16 and unit2 == 17: #if atmospheres then kilopascals is selected
        num = num*101.325
        messagebox.showinfo("Result", "Your conversion is {0:.2f}kPa".format(num))
        again()
    elif unit1 == 18 and unit2 == 17: #if mmHg then kilopascals is selected
        num = num*0.133322
        messagebox.showinfo("Result", "Your conversion is {0:.2f}kPa".format(num))
        again()
    else: #if the first choice has not been selected
        unit1 = 17
        while True: #if this button is the first choice, then ask user for their value
            try:
                num = askfloat("kilo Pascals", "Please enter a number")
                if num == None:
                    unit1= 0
                    break
                elif num <= 0:
                    messagebox.showinfo("Error", "Your value can't be zero or negative")
                else:
                    messagebox.showinfo("ACCEPTED", "Your value has been accepted")
                    kPas.place_forget()
                    break
            except (ValueError,error):
                showerror ("Error", "Enter a valid number")
                continue

def mmHgUnit ():
    global unit1
    global unit2
    global num
    unit2 = 18 #sets this unit as second choice if first has been selected
    if unit1 == 16 and unit2 == 18: #if atmospheres then mmHg is selected
        num = num*760
        messagebox.showinfo("Result", "Your conversion is {0:.2f}mmHg".format(num))
        again()
    elif unit1 == 17 and unit2 == 18: #if kilopascals then mmHg is selected
        num = num*7.50062
        messagebox.showinfo("Result", "Your conversion is {0:.2f}mmHg".format(num))
        again()
    else: #if the first choice has not been selected
        unit1 = 18
        while True: #if this button is the first choice, then ask user for their value
            try:
                num = askfloat("mmHg", "Please enter a number")
                if num == None:
                    unit1= 0
                    break
                elif num <= 0:
                    messagebox.showinfo("Error", "Your value can't be zero or negative")
                else:
                    messagebox.showinfo("ACCEPTED", "Your value has been accepted")
                    mmHg.place_forget()
                    break
            except (ValueError,error):
                showerror ("Error", "Enter a valid number")
                continue
    
        
#Function for user to cycle through available music, music must be on user's computer
winsound.PlaySound("C:\\Users\\kon12673\\Downloads\\Mii Channel Music.wav", winsound.SND_ALIAS | winsound.SND_ASYNC)
def mus1():
    music=Button(root,text="Big Time Rush Theme Song", command=mus2, height=1 , width = 35)
    music.place (x=125,y=350)
    winsound.PlaySound("C:\\Users\\kon12673\\Downloads\\Big Time Rush Theme Song.wav", winsound.SND_ALIAS | winsound.SND_ASYNC)
def mus2():
    music=Button(root,text="Pokemon Battle Frontier", command=mus3, height=1 , width = 35)
    music.place (x=125,y=350)
    winsound.PlaySound("C:\\Users\\kon12673\\Downloads\\Pokemon Battle Frontier Theme.wav", winsound.SND_ALIAS | winsound.SND_ASYNC)
def mus3():
    music=Button(root,text="NOMA - Brain Power", command=mus4, height=1 , width = 35)
    music.place (x=125,y=350)
    winsound.PlaySound("C:\\Users\\kon12673\\Downloads\\NOMA - Brain Power (original).wav", winsound.SND_ALIAS | winsound.SND_ASYNC)
def mus4():
    music=Button(root,text="BTS - Fake Love", command=mus5, height=1 , width = 35)
    music.place (x=125,y=350)
    winsound.PlaySound("C:\\Users\\kon12673\\Downloads\\bts fakelove.wav", winsound.SND_ALIAS | winsound.SND_ASYNC)
def mus5 ():
    music=Button(root,text="Wii Music", command=mus1, height=1 , width = 35)
    music.place (x=125,y=350)
    winsound.PlaySound("C:\\Users\\kon12673\\Downloads\\Mii Channel Music.wav", winsound.SND_ALIAS | winsound.SND_ASYNC)


#The buttons for the different categories
mas=Button(root, text="Mass", command=mass,height=1, width=15)
distan=Button(root, text="Distance", command=distance, height=1, width=15)
temp=Button(root, text="Temperature", command=temperature,height=1, width=15)
currenc=Button(root, text="Currency", command= currency, height=1, width =15)
tm=Button(root, text="Time", command=time,height=1, width=15)
pres=Button(root, text="Pressure", command=pressure,height=1, width=15)

#The buttons for the units available, depending on which category selected
gra=Button(root, text="Grams", command=grams, height = 1, width =15)
kilogra=Button(root, text="Kilograms", command=kilog, height = 1, width =15)
milligra=Button(root, text="Milligrams", command=millig, height = 1, width =15)
metr=Button(root, text="Metres", command=met, height = 1, width =15)
kilom=Button(root, text="Kilometres", command=kilomet, height = 1, width =15)
centim=Button(root, text="Centimetres", command=centi, height = 1, width =15)
can=Button(root, text="Canadian Dollars", command=cad, height = 1, width =15)
us=Button(root, text="American Dollars", command=usd, height = 1, width =15)
euro=Button(root, text="European Dollars", command=europ, height = 1, width =15)
celsi=Button(root, text="Celsius", command=celsius, height = 1, width =15)
kelvi=Button(root, text="Kelvins", command=kelvins, height = 1, width =15)
fahren=Button(root, text="Fahrenheit", command=fahrenheit, height = 1, width =15)
sec=Button(root, text="Seconds", command=second, height = 1, width =15)
mn=Button(root, text="Minutes", command=minute, height = 1, width =15)
hr=Button(root, text="Hours", command=hour, height = 1, width =15)
atm=Button(root, text="Atmospheres", command=atmosphere, height = 1, width =15)
kPas=Button(root, text="Kilo Pascals", command=kPascal, height = 1, width =15)
mmHg=Button(root, text="Millimetres of Mercury", command=mmHgUnit, height = 1, width =15)

#Button for music
music1=Button(root,text="Wii Music", command=mus1, height=1 , width = 35)
music1.place (x=125,y=350)

#Actual buttons for reset, quit, and back. Display the different categories buttons
pla=Button(root, text="Reset",command = again, height = 1, width =15) 
pla.place (x=125,y=300)
qui=Button(root, text="Quit",command = quitt, height = 1, width =15)
qui.place (x=275,y=300)
bac=Button(root, text="Back",command = back, height = 1, width =15)
category()
 
root.mainloop()
