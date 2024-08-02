import tkinter
from tkinter import END

window = tkinter.Tk()



window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


# label
my_label = tkinter.Label(text="I Am A Label", font=("Arial", 24, "bold"))
# updating/ replacing the values
my_label["text"] = "new text"
# to update more values
my_label.config(text="new_text", font=("Arial", 10, "normal"))
# my_label.pack(side="left")  # , expand = True, side="left"
# by using pack we can use place for good co ordination and then grid  also
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(pady=50, padx=50)




# todo : we cannot use both grid and the pack at the same time if grid in use whole program is with grid
# click the button to change the text
def button_clicked():
    # when i click the button the input value goes to the label
    # here the (input.get()) is used to get the input value in the inuput entry
    my_label.config(text=Input.get(), font=("Arial", 10, "normal"))
# buttons
button = tkinter.Button(text="click  me", command=button_clicked)
button.grid(column=1, row=1)




# input entry box
Input = tkinter.Entry(width=10)
Input.focus()
# used to insert a default value to the input
Input.insert(END, string="Some text to begin with.")
# the "get" is used to get the input in the input box
print(Input.get())
Input.grid(column=3, row=2)



# task for adding grid
button_2 = tkinter.Button(text="click me 2")
button_2.grid(column=2, row=0)



window.mainloop()
