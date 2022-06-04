#!/usr/bin/env python

# Name: BMI Calculator
# adapted from TokyoEdtech -YT: https://www.youtube.com/watch?v=driAxDI--Uc 
# Purpose: Practicing Functions, tkinter library
# Misc: BMI = weight/height ** 2



import tkinter


def calculate_bmi():
  weight = float(entry_weight.get())
  height = float(entry_height.get())
  bmi = round(weight/(height**2),2)
  label_result['text'] = 'bmi: {}'.format(bmi)

def clear():
  entry_weight.delete(0, 'end')
  entry_height.delete(0, 'end')


root = tkinter.Tk()
root.title("BMI Calculator")

# Weight GUI and Entry Field
label_weight = tkinter.Label(root, text="weight (kg): ")
label_weight.grid(column=0, row=0)

entry_weight = tkinter.Entry(root)
entry_weight.grid(column=1, row=0)


# Height GUI and Entry Field
label_height = tkinter.Label(root, text="height (m): ")
label_height.grid(column=0, row=1)

entry_height = tkinter.Entry(root)
entry_height.grid(column=1, row=1)

# Button Creator

button_calculate = tkinter.Button(root, text="calculate", command=calculate_bmi)
button_calculate.grid(column=0, row=3)

# Output 

label_result = tkinter.Label(root, text="bmi: ")
label_result.grid(column=1, row=3)

button_clear= tkinter.Button(root, text="clear", command=clear)
button_clear.grid(column=1, row=4)











root.mainloop()
