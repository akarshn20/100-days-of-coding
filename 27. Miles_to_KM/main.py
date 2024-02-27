from tkinter import *


def miles_to_km():
    miles = float(input_miles.get())
    km = miles * 1.609
    km_result.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(height=300, width=400)
window.config(padx=50, pady=50)

equal_to = Label(text="is equal to", font=("Ariel", 20, "normal"))
equal_to.grid(column=0, row=1)
equal_to.config(padx=20, pady=20)

miles_label = Label(text="Miles", font=("Ariel", 20, "normal"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=20, pady=20)

km_label = Label(text="Km", font=("Ariel", 20, "normal"))
km_label.grid(column=2, row=1)
km_label.config(padx=20, pady=20)

input_miles = Entry(width=12)
input_miles.grid(column=1, row=0)

calc_button = Button(text="Calculate", command=miles_to_km)
calc_button.grid(column=1, row=2)
calc_button.config(padx=20, pady=20)

km_result = Label(text="0")
km_result.grid(column=1, row=1)



window.mainloop()