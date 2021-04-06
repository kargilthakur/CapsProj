from guizero import App , Text
app = App(title="Hello world")
welcome_message = Text(app, text="Welcome to XYZ Bank ATM" , size=40, font="Times New Roman", color="orange")
app.display()