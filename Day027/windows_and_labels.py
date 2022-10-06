import tkinter as tki

window = tki.Tk()
window.title("My first GUI program")
window.minsize(width = 500,height = 300)

#Label"
my_label = tki.Label(text="I am a label" , font=("Arial",24,"bold"))
my_label.pack(side="left")

my_label["text"]= "New Text" #Changing text





















window.mainloop()