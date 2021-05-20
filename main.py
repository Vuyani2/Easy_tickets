# Import libraries
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Easy Ticket")
root.geometry('500x500')


# Creating a variables for prices
sc = 40
mv = 75
th = 100

# Creating Tkinter widgets
var = StringVar()

entry1 = Entry(root, width=23)
entry1.place(x=200,y=50)

cat = ttk.Combobox(root, textvariable=var, width=10, value=["Soccer", "Movie", "Theater"])
cat.place(x=250, y=100, width=180)

num = ttk.Spinbox(root, from_=0, to=100, state="readonly")
num.place(x=250, y=150)

lblcell = Label(root, text="Cellphone number: ")
lblcell.place(x=50,y=50)

lblcat = Label(root, text="Ticket Category: ")
lblcat.place(x=50, y=100)

lbltik = Label(root, text="Number of tickets: ")
lbltik.place(x=50, y=150)

ans = Label(root)
ans.place(x=350, y=250)


#Creating class
class clsTiketSales:
    def __init__(self, celno, num_tickets, price):
        self.celno = celno
        self.num_tickets = num_tickets
        self.price = price
        return

# Creates function for button
    def calc():

# Passes through class
        sale = clsTiketSales(entry1.get(), float(num.get()), cat.get())

        if cat.get() == "Soccer":
            scprice = sc * int(num.get()) + (14/100)
            ans.config(text="Price:"+ str(scprice) + "\n" + "tickets:"+str(num.get()) + "\n" +"Number:"+ str(entry1.get()))
        if cat.get() == "Movie":
            mvprice = mv * int(num.get()) + (14/100)
            ans.config(text="Price:"+ str(mvprice) + "\n" + "tickets:"+str(num.get()) + "\n" +"Number:"+ str(entry1.get()))
        if cat.get() == "Theater":
            thprice = th * int(num.get()) + (14/100)
            ans.config(text="Price:"+ str(thprice) + "\n" + "tickets:"+str(num.get()) + "\n" +"Number:"+ str(entry1.get()))

# function

#Creating button
    btn = Button(root, text="calculate", command=calc, width=20, height=1)
    btn.place(x=50, y=250)
# Adds widgets


root.mainloop()
