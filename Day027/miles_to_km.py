from tkinter import *
from turtle import color



def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width = 500,height = 300)
window.config(padx=20,pady=20)


miles_input = Entry(width = 9, border='5')
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal = Label(text="is equals to")
is_equal.grid(column=0, row=1)


km_result = Label(text="0")
km_result.grid(column=1, row=1)

km_label = Label(text = "Km")
km_label.grid(column=2 , row=1)

calculate = Button(text="Calculate", command=miles_to_km , bg="blue" , fg='white' , border=5)
calculate.grid(column=1, row=2)


mainloop()