import tkinter

window = tkinter.Tk()
window.title("Distance Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)


def calculation():
    mile = int(miles_input.get())
    km = mile * 1.609
    kilo_input_label.config(text=f"{km:.2f}")


# miles entry
miles_input = tkinter.Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles", font=("Arial", 10, "normal"))
miles_label.grid(column=2, row=0)

text_value = tkinter.Label(text="is equal to", font=("Arial", 10, "normal"))
text_value.grid(column=0, row=1)

# kilo entry
kilo_input_label = tkinter.Label(text="0")
kilo_input_label.grid(column=1, row=1)


kilo_label = tkinter.Label(text="Km", font=("Arial", 10, "normal"))
kilo_label.grid(column=2, row=1)


# calculate button
cal_btn = tkinter.Button(text="Calculate", command=calculation)
cal_btn.grid(column=1, row=2)


window.mainloop()
