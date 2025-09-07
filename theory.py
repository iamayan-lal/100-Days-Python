#Unlimited Positional Arguements
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
print(add(1, 2))


# **kwargs: Keyworded Variable-Length Arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)


calculate(2, add=3, multiply=5)


# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
from tkinter import *
window = Tk()
window.title("My First GUI Application")
window.minsize(600, 300)

#Label
my_label = Label(text="My First Label", font=("Arial", 20, "bold"))
my_label.pack()

#Configure a Label
my_label["text"] = "New Label"
#We have another method as well by using "config" keyword
my_label.config(text = "Config New Label")

#Entry : Text Inputs
input = Entry(width=40)
input.pack()

#To create a button
def button_clicked():
    new_text = input.get() #Used to read the input written
    my_label.config(text = new_text)
    input.get()
button = Button(text="Click Me", command=button_clicked)
button.pack()



window.mainloop()
