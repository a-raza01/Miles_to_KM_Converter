from tkinter import *


def button_clicked():
    value_entered = float(entry.get())
    answer = round(value_entered * 1.60934, 2)
    label_answer.config(text=answer)


window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=150, height=100)
window.config(padx=20, pady=20)

# Labels
label_1 = Label(text="Miles")
label_1.config(padx=10, pady=10)
label_1.grid(column=2, row=0)

label_2 = Label(text="is equal to")
label_2.grid(column=0, row=1)

label_answer = Label()
label_answer.grid(column=1, row=1)

label_3 = Label(text="km")
label_3.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# Entry
entry = Entry()
entry.grid(column=1, row=0)

window.mainloop()
