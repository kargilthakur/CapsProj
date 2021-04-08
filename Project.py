import guizero
from guizero import App, Text, PushButton, Window, TextBox
import time

# Interface for first screen
app1 = App("Bank of India ATM", width=600, height=600)
app1.bg = 246, 185, 72
txt1 = Text(app1, "Welcome to Bank of India ATM", size=32, font="Open sans", align="top")
txt2 = Text(app1, "\n\n\nPlease enter card to begin transaction\n\n\n", size=20)
txt3 = Text(app1, "Blind mode on", align="bottom", size=10)

def card_detected():

    app1.hide()
    window1.show()

# after command is used to automatically call a command after a specified time
app1.after(5000,card_detected)

# Second screen interface
window1 = Window(app1,title="ATM pin screen", width=600, height=600,visible=False)
window1.bg = 246, 185, 72
txt4 = Text(window1, "Please enter your ATM pin:",size=20)
txt5 = Text(window1, "Blind mode on", align="bottom", size=10)
textbox1 = TextBox(window1, text="", hide_text=True)

# Gui for snooping alert
snooping = True
def check_camera():
    print(window1.enabled)
    if window1.enabled:
        if snooping:
            if window1.yesno("Snooping alert", "Do you want to continue?"):
                pass
            else:
                window1.destroy()
                app1.show()

# Function for checking the ATM pin
def check_pin():
    # To be checked using the database
    if textbox1.value == "1234":
        print("correct pin")
        window1.hide()
    else:
        window1.info("Incorrect pin","Please enter correct pin")
        textbox1.clear()

window1.after(7000, check_camera)
push1=PushButton(window1,command=check_pin,text="Enter")


# push1=PushButton(app1,command=card_detected,text="Exit")
app1.display()




