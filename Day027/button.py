import tkinter as tki

window = tki.Tk()
window.title("My first GUI program")
window.minsize(width = 500,height = 300)

my_label = tki.Label(text="I am a label" , font=("Arial",24,"bold"))
my_label.pack(side="left")

#button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = tki.Button(text = "Click Me" , command=button_clicked)
button.pack()

# Input and Entry
input = tki.Entry(width=10)
input.pack()
print(input.get())




window.mainloop()
