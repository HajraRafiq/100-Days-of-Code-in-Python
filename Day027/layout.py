from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width = 500,height = 300)

my_label = Label(text="I am a label" , font=("Arial",24,"bold"))
my_label.place(x=100, y = 200) # for custom positioning






def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text = "Click Me" , command=button_clicked)
button.grid(column=1,row=1)

input = Entry(width=10)
print(input.get())
input.grid(column=2,row=2)




mainloop()