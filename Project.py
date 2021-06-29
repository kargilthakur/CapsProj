
from guizero import App, Text, PushButton, Window, TextBox, ButtonGroup
from tts import welcome,enter_pin,incorrect_pin,Options,canform,middle
from speechdetect import listening,mounty
from NotesDispensed import nota
import time
def  secret():
    chocolate = listening()
    selected_option(chocolate)

def secret2():
    global cake
    cake = mounty()
    textbox2.value = cake
    confirm("1")

def secret3():
    nota(int(cake))
    op1.hide()
    startprog()

def exitmachine():
    mainpage.destroy()

def card_detected():
    mainpage.hide()
    pinpage.show()
    mainpage.after(500,enter_pin)

# Gui for snooping alert
def startprog():
    mainpage.after(3000, card_detected)
    mainpage.show()

def check_camera():
    if pinpage.enabled:
        if snooping:
            if pinpage.yesno(title="Snooping alert", text="Someone is snooping ! Do you want to continue?"):
                pass
            else:
                pinpage.destroy()
                startprog()

# Function for checking the ATM pin
def check_pin():
    # To be checked using the database
    if len(textbox1.value) == 4:
        if textbox1.value == "1234":
            pinpage.destroy()
            optionpage.show()
            optionpage.after(500,Options)
            optionpage.after(14000,secret)
        else:
            # pinpage.info("Incorrect pin", "Please enter correct pin")
            textbox1.clear()
            pinpage.after(0,incorrect_pin)

# Selected transaction
def selected_option(chocolate):
    if chocolate == "withdrawal":
        optionpage.destroy()
        op1.show()
        op1.after(200,middle(1))
        op1.after(800,secret2)
    elif chocolate == "deposit":
        optionpage.destroy()
        op2.show()
        op2.after(200,middle(2)) 
    elif chocolate == "change pin":
        optionpage.destroy()
        op3.show()
        op3.after(200,middle(3))
    elif chocolate == "balance":
        optionpage.destroy()
        op4.show()
        op4.after(200,middle(4))

# UI for exit button
def exitall(a):

    if a == "1":
        op1.destroy()
        mainpage.show()

    elif a == "2":
        op2.destroy()
        mainpage.show()

    elif a == "3":
        op3.destroy()
        mainpage.show()

    elif a == "4":
        op4.destroy()
        mainpage.show()

# UI for confirm button after entering details for transaction
def confirm(x):

    if x == "1":
        op1.after(100,secret3)
        # op1.info("transaction successful", "Please collect money from dispenser")
       

    elif x == "2":
        op2.after(100,canform(int(x)))
        op2.info("transaction successful", "Your money is deposited")
        op2.hide()
        startprog()

    elif x == "3":
        op3.after(100,canform(int(x)))
        op3.info("transaction successful", "Your PIN is changed")
        op3.hide()
        startprog()

    elif x == "4":
        op4.after(100,canform(int(x)))
        op4.info("transaction successful", "Please collect enquiry receipt")
        op4.hide()
        startprog()

def counter():
    txt69.value = int(txt69.value) + 1

def counter1():
    txt99.value = int(txt99.value) + 1



mainpage = App("Bank of India ATM", width=600, height=600)
mainpage.bg = 246, 185, 72
txt1 = Text(mainpage, "Welcome to Bank of India ATM", size=32, font="Open sans", align="top")
txt2 = Text(mainpage, "\n\n\nPlease enter card to begin transaction\n\n\n", size=20)
txt3 = Text(mainpage, "Blind mode on", align="bottom", size=10)
exitm = PushButton(mainpage, command=exitmachine, text="Stop Machine", align="bottom")

mainpage.after(500,welcome)

# after command is used to automatically call a command after a specified time
mainpage.after(5000, card_detected)

# Second screen interface
pinpage = Window(mainpage, title="ATM pin screen", width=600, height=600, visible=False)
pinpage.bg = 246, 185, 72
txt4 = Text(pinpage, "Please enter your ATM pin:", size=20)
txt5 = Text(pinpage, "Blind mode on", align="bottom", size=10)
textbox1 = TextBox(pinpage, text="",command=check_pin)

snooping = True
pinpage.after(6000, check_camera)
# push1 = PushButton(pinpage, command=check_pin, text="Enter")


# Options page interface
optionpage = Window(mainpage, title="ATM options", width=600, height=600, visible=False)
optionpage.bg = 246, 185, 72
txt6 = Text(optionpage, "Choose from the following options:", size=24)
txt7 = Text(optionpage, "Blind mode ON", align="bottom", size=10)
txt69 = Text(optionpage,"1",align="right",size=10)
choice = ButtonGroup(optionpage, options=["1.Cash Withdrawal", "2.Cash Deposit", "3.Change PIN", "4.Balance Enquiry"])
choice.text_size = 24
choice.text_color = "black"
push2 = PushButton(optionpage, command=selected_option("magic"), text="continue")
txt69.repeat(1000, counter)



# UI for option 1
op1 = Window(mainpage, "Cash Withdrawal", width=600, height=600, bg=(246, 185, 72), visible=False)
txt12 = Text(op1, "Please enter the amount to be withdrawn", size=20)
textbox2 = TextBox(op1)
confirm1 = PushButton(op1, text="Confirm", command=confirm, args="1")
txt8 = Text(op1, "Blind mode on", align="bottom", size=10)
txt99 = Text(op1,"1",align="right",size=10)
exitbutton1 = PushButton(op1, text="Cancel transaction", command=exitall, args="1", align="bottom")
txt99.repeat(1000,counter1)

# UI for option 2
op2 = Window(mainpage, "Cash Deposit", width=600, height=600, bg=(246, 185, 72), visible=False)
txt13 = Text(op2, "Enter keep the cash in deposit machine", size=20)
txt14 = Text(op2, "The amount to be deposited is:10000", size=20)
confirm2 = PushButton(op2, text="Confirm", command=confirm, args="2")
txt9 = Text(op2, "Blind mode on", align="bottom", size=10)
exitbutton2 = PushButton(op2, text="Cancel transaction", command=exitall, args="2", align="bottom")



# UI for option 3
op3 = Window(mainpage, "Change PIN", width=600, height=600, bg=(246, 185, 72), visible=False)
txt15 = Text(op3, "Enter the current PIN", size=20)
textbox3 = TextBox(op3)
txt16 = Text(op3, "Enter the new PIN", size=20)
textbox4 = TextBox(op3)
confirm3 = PushButton(op3, text="Confirm", command=confirm, args="3")
txt10 = Text(op3, "Blind mode on", align="bottom", size=10)
exitbutton3 = PushButton(op3, text="Cancel transaction", command=exitall, args="3", align="bottom")



# UI for option 4
op4 = Window(mainpage, "Balance enquiry", width=600, height=600, bg=(246, 185, 72), visible=False)
txt17 = Text(op4, "The balance is :10000", size=20)
confirm4 = PushButton(op4, text="Confirm", command=confirm, args="4")
txt11 = Text(op4, "Blind mode on", align="bottom", size=10)
exitbutton4 = PushButton(op4, text="Cancel transaction", command=exitall, args="4", align="bottom")

# Start for program
mainpage.display()



