from tkinter import *
window = Tk()
window.title("Miles to Km Project")
window.config(padx=20, pady=20)

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.60934
    kilometer_result_label.config(text=km)

miles_input = Entry(width=7)
miles_input.grid(row = 1, column = 0)

miles_label = Label(text = "Miles")
miles_label.grid(row = 1, column = 1)

is_equal_label = Label(text = "is equal to")
is_equal_label.grid(row = 2, column = 0)

kilometer_result_label = Label(text = "0")
kilometer_result_label.grid(row = 2, column = 1)

kilometer_label = Label(text = "Km")
kilometer_label.grid(row = 2, column = 2)

calculate_button = Button(text = "Calculate",command = miles_to_km)
calculate_button.grid(row = 3, column = 1)


window.mainloop()