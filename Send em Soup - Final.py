#...
# Heath Hilton
# 10/2022

# Program: Send 'em Soup - Final Project

# This program is meant to simulate a very simple 'Wix.com' style webpage where you are able to mail someone a can of soup instead of a 'get well' card.
# ...

import tkinter as tk
from tkinter import *
from tkinter import messagebox
      
       
#From Start Page To Tomato
def fromStartToTom():
   startButton.place(x=-1000, y=310)
   exitButton.place(x=-1000, y=310)
   advanceToTom()

   
#From Order Page Back To Tomato
def fromStartToTom():
   orderFormButtonsRemove
   advanceToTom()
          
       
   
#Tomato Page   
def advanceToTom():
   label = Label(root, image=bg2)   
   label.place(x=0, y=0)
   tomatoButtonsOn()
   
def tomatoButtonsOn():
   previousButtonTom = tk.Button(root, bg = "#F17E01", border = "-2", fg = "white", text="   <==   ", command = advanceToPump)
   previousButtonTom.place(x=400, y=445)
   orderButtonTom = tk.Button(root, bg = "#F17E01", border = "-2", fg = "white", text="   Order   ", command = placeOrder)
   orderButtonTom.place(x=440, y=445)
   nextButtonTom = tk.Button(root, bg = "#F17E01", border = "-2", fg = "white", text="   ==>   ", command = advanceToWed)
   nextButtonTom.place(x=495, y=445)
   lbl = tk.Label(root, fg = "white", bg = "#F17E01", font=("Arial", 12), text="  Send someone you love a tasty can of Tomato Soup!  ")
   lbl.place(x=400, y=420)
   
def advanceFromTom():
   tomatoButtonsOff()
   
def tomatoButtonsOff():
   previousButtonTom.place(x=-1000, y=450)
   orderButtonTom.place(x=-1000, y=450)
   nextButtonTom.place(x=-1000, y=450)
   lbl.place(x=-1000, y=420)
   
   
#Wedding Page
def advanceToWed():
   label = Label(root, image=bg3)   
   label.place(x=0, y=0)
   weddingButtonsOn()
   
def weddingButtonsOn():   
   previousButtonWed = tk.Button(root, bg = "#E8E7ED", border = "-2", fg = "#46752E", text="   <==   ", command = advanceToTom)
   previousButtonWed.place(x=785, y=220)
   orderButtonWed = tk.Button(root, bg = "#E8E7ED", border = "-2", fg = "#46752E", text="   Order   ", command = placeOrder)
   orderButtonWed.place(x=825, y=220)
   nextButtonWed = tk.Button(root, bg = "#E8E7ED", border = "-2", fg = "#46752E", text="   ==>   ", command = advanceToPump)
   nextButtonWed.place(x=870, y=220)
   lbl = tk.Label(root, fg = "#46752E", bg = "#E8E7ED", font=("Arial", 12), text="  Italian Wedding Soup to celebrate life's special events!  ")
   lbl.place(x=515, y=200)
   
def advanceFromWed():
   weddingButtonsOff()
      
def weddingButtonsOff():   
   previousButtonWed.place(x=-1000, y=450)
   orderButtonWed.place(x=-1000, y=450)
   nextButtonWed.place(x=-1000, y=450)
   lbl.place(x=-1000, y=420)
   
   
#Pumpkin Page
def advanceToPump():
   label = Label(root, image=bg4)   
   label.place(x=0, y=0)
   pumpkinButtonsOn()
   
def pumpkinButtonsOn():
   previousButtonPump = tk.Button(root, bg = "#DDEAF1", border = "-2", fg = "#CA9630", text="   <==   ", command = advanceToWed)
   previousButtonPump.place(x=400, y=560)
   orderButtonPump = tk.Button(root, bg = "#DDEAF1", border = "-2", fg = "#CA9630", text="   Order   ", command = placeOrder)
   orderButtonPump.place(x=440, y=560)
   nextButtonPump = tk.Button(root, bg = "#DDEAF1", border = "-2", fg = "#CA9630", text="   ==>   ", command = advanceToTom)
   nextButtonPump.place(x=485, y=560)
   lbl = tk.Label(root, fg = "#CA9630", bg = "#DDEAF1", font=("Arial", 12), text="  Pumpkin Spice Soup for all of your soccer moms that can't get enough.  ")
   lbl.place(x=210, y=540)
   
def advanceFromPump():
   pumpkinButtonsOff()
   
def pumpkinButtonsOff():
   previousButtonPump.place(x=-1000, y=450)
   orderButtonPump.place(x=-1000, y=450)
   nextButtonPump.place(x=-1000, y=450)
   lbl.place(x=-1000, y=420)
   
   
   
#Order Form Page
def placeOrder():
   tomatoButtonsOff()
   weddingButtonsOff()
   pumpkinButtonsOff()
   label = Label(root, image=bg5)   
   label.place(x=0, y=0)
   orderFormButtonsPlace()

def orderFormButtonsPlace():
   borderValue = 1
   
   nameCustomer = tk.Entry(root, width=60, borderwidth=borderValue)
   nameCustomer.insert(0, "Your Name")
   nameRecipient = tk.Entry(root, width=60, borderwidth=borderValue)
   nameRecipient.insert(0, "Recipient")
   address1 = tk.Entry(root, width=60, borderwidth=borderValue)
   address1.insert(0, "Address 1")
   address2 = tk.Entry(root, width=60, borderwidth=borderValue)
   address2.insert(0, "Address 2")
   addressCity = tk.Entry(root, width=30, borderwidth=borderValue)
   addressCity.insert(0, "City")
   addressState = tk.Entry(root, width=10, borderwidth=borderValue)
   addressState.insert(0, "State (XX)")
   addressZip = tk.Entry(root, width=15, borderwidth=borderValue)
   addressZip.insert(0, "Zip Code")
   phone = tk.Entry(root, width=60, borderwidth=borderValue)
   phone.insert(0, "(xxx) xxx-xxxx")
   soupOption = tk.Entry(root, width=60, borderwidth=borderValue)
   soupOption.insert(0, "Soup")
   customMessage = tk.Entry(root, width=60, borderwidth=borderValue)
   customMessage.insert(0, "Message")
   
   nameCustomer.place(x=100, y=50)
   nameRecipient.place(x=100, y=70)
   address1.place(x=100, y=90)
   address2.place(x=100, y=110)
   addressCity.place(x=100, y=130)
   addressState.place(x=295, y=130)
   addressZip.place(x=370, y=130)
   phone.place(x=100, y=150)
   soupOption.place(x=100, y=170)
   customMessage.place(x=100, y=200)
   
   button = tk.Button(root, text='Return', command = fromStartToTom)
   button.place(x=150, y=225)
   button2 = tk.Button(root, text='Order', command = finalThankYouPage)
   button2.place(x=350, y=225)

def orderFormButtonsRemove():   
   nameCustomer.place(x=-1000, y=50)
   nameRecipient.place(x=-1000, y=70)
   address1.place(x=-1000, y=90)
   address2.place(x=-1000, y=110)
   addressCity.place(x=-1000, y=130)
   addressState.place(x=-1000, y=130)
   addressZip.place(x=-1000, y=130)
   phone.place(x=-1000, y=150)
   soupOption.place(x=-1000, y=170)
   customMessage.place(x=-1000, y=200)
   button.place(x=-1000, y=310)
   button1.place(x=-1000, y=310)
   
def outputOrderInfo():
   print("\"" + nameCustomer.get() + "\",\"" + nameRecipient.get() + "\",\"" + address1.get() + "\",\"" + address2.get() + "\",\"" + addressCity.get() + "\",\"" + addressState.get() + "\",\"" + addressZip.get() + "\",\"" + phone.get() + "\",\"" + soupOption.get() + "\",\"" + customMessage.get() + "\"")


#Thank You Page
def finalThankYouPage():
   messagebox.showinfo
   messagebox.showinfo("You Sent Them Soup","Your order has been placed.")
   outputOrderInfo()
   label = Label(root, image=bg6)   
   label.place(x=0, y=0)
   orderedExitButton = tk.Button(root, bg = "black", border = "-2", fg = "white", text="   Thank You   ", command = finalExit)
   orderedExitButton.place(x=465, y=300)


#The End
def finalExit():   
    root.destroy()



# Main Window
root = tk.Tk()
root.configure(width=1000, height=667)

bg1 = PhotoImage(file = "tomato-start.png")
bg2 = PhotoImage(file = "soup-tomato.png")
bg3 = PhotoImage(file = "soup-wedding.png")
bg4 = PhotoImage(file = "soup-pumpkin.png")
bg5 = PhotoImage(file = "place-order.png")
bg6 = PhotoImage(file = "order-thankyou.png")


#Place the main start page image
label = Label(root, image=bg1)
label.place(x=0, y=0)


#Program Start Buttons and Text
lbl = tk.Label(root, fg = "white", bg = "black", font=("Arial", 20), text="  Send 'em Soup  ")
lbl.place(x=160, y=250)

startButton = tk.Button(root, bg = "black", border = "-2", fg = "white", text="   Begin   ", command = fromStartToTom)
startButton.place(x=200, y=310)
exitButton = tk.Button(root, bg = "black", border = "-2", fg = "white", text="   Exit   ", command = finalExit)
exitButton.place(x=300, y=310)



#Soup Button Options
previousButtonTom = tk.Button(root, bg = "black", border = "-2", fg = "white", text="   <==   ", command = advanceFromPump)
orderButtonTom = tk.Button(root, bg = "black", border = "-2", fg = "white", text="   Order   ", command = placeOrder)
nextButtonTom = tk.Button(root, bg = "black", border = "-2", fg = "white", text="   ==>   ", command = advanceToWed)

previousButtonWed = tk.Button(root, bg = "black", border = "-2", fg = "white", text="   <==   ", command = advanceFromTom)
orderButtonWed = tk.Button(root, bg = "black", border = "-2", fg = "white", text="   Order   ", command = placeOrder)
nextButtonWed = tk.Button(root, bg = "black", border = "-2", fg = "white", text="   ==>   ", command = advanceToPump)

previousButtonPump = tk.Button(root, bg = "black", border = "-2", fg = "white", text="   <==   ", command = advanceFromWed)
orderButtonPump = tk.Button(root, bg = "black", border = "-2", fg = "white", text="   Order   ", command = placeOrder)
nextButtonPump = tk.Button(root, bg = "black", border = "-2", fg = "white", text="   ==>   ", command = advanceToTom)


#Soup Ordered Page
orderedExitButton = tk.Button(root, bg = "black", border = "-2", fg = "white", text="   Thank You   ", command = finalExit)



nameCustomer = tk.Entry(root)
nameCustomer.insert(0, "Your Name")
nameRecipient = tk.Entry(root)
nameRecipient.insert(0, "Recipient")
address1 = tk.Entry(root)
address1.insert(0, "Address 1")
address2 = tk.Entry(root)
address2.insert(0, "Address 2")
addressCity = tk.Entry(root)
addressCity.insert(0, "City")
addressState = tk.Entry(root)
addressState.insert(0, "State (XX)")
addressZip = tk.Entry(root)
addressZip.insert(0, "Zip Code")
phone = tk.Entry(root)
phone.insert(0, "(xxx) xxx-xxxx")
soupOption = tk.Entry(root)
soupOption.insert(0, "Soup")
customMessage = tk.Entry(root)
customMessage.insert(0, "Message")













root.mainloop()
