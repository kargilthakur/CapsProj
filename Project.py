from guizero import App , Text , TextBox , PushButton , info
app = App(title="ATM interface")
welcome_message = Text(app, text="Welcome to XYZ Bank ATM" , size=20, font="Times New Roman", color="brown")
pin_message = Text(app, text="Enter your ATM pin ")
def say_my_name():
    pin_message.value = "Your ATM pin is " + my_name.value
my_name = TextBox(app)
update_text = PushButton(app, command=say_my_name, text="Submit")
app1=App(title="second page",width=200,height=200,layout="grid")
app1.display()
info("Transaction","Transaction completed")
