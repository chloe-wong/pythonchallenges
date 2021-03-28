import tkinter
import pandas as pd
import random as rand
df = pd.read_excel(r'C:\Users\chloe\Documents\names.xlsx')
mylist = df['Names'].tolist()
window = tkinter.Tk()
def RandomNumber():
    MyRandom = rand.choice(mylist)
    number_chosen.configure(text = "Number chosen:" + str(MyRandom))
MyTitle = tkinter.Label(window, text="Random Name Generator", font="Helvetica 16 bold")
MyTitle.pack()
MyButton = tkinter.Button(window, text = "OK", command=RandomNumber)
MyButton.pack()
number_chosen = tkinter.Label(window, font="Helvetica 16 bold")
number_chosen.pack()
window.mainloop()