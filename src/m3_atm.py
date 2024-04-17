import tkinter as tk

###############################################################################
# DONE: 1. (2 pts)
#
#   The todos in this module are in one comment because you will be modifying
#   the same bit of code each time. Here you will create a basic ATM
#   application that allows a user to withdraw funds and deposit funds
#
#   For this _todo_, you will create a window with the title "ATM" and call its
#   mainloop() method so it runs.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 2. (3 pts)
#
#   For this _todo_, you will create an area where the user's current balance
#   is displayed. There should be a label that says "Current Balance ($):" and
#   below it another label that has the dollar amount of their current balance
#   displayed. For the purposes of this problem, we will assume that all users
#   start out with 1000 dollars in their account. So, this label should start
#   out with "1000" as its text.
#
#   All of the elements on this window should be centered.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 3 (3 pts)
#
#   For this _todo_, create two more labels: one that says "Amount ($):" and
#   another that starts out empty beneath it. This is where the user's amount
#   that they will either withdraw or deposit will display.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 4. (7 pts)
#
#   For this _todo_, you will create all the buttons that the user needs:
#
#       - One for each digit 0-9
#       - A withdrawal button
#       - A deposit button
#
#   They should be in the standard configuration for a numberpad (see the
#   images in the README file on GitHub). Each button is 75px by 75px.
#
#   HINT: I used a frame to surround the buttons and grid for this.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 5. (10 pts)
#
#   For this _todo_, using the command keyword on each button to have each
#   number button type that digit in the amount label above (just like you
#   would if you were typing in an amount). Pressing each button should add
#   that number to end of the text in the label.
#
#   HINT: I found that the easiest way to accomplish this was to use a
#   different handler for each button.
#
#   You also need a handler for the withdrawal and deposit buttons.
#
#   The withdrawal button should subtract the amount typed into the amount box
#   from the user's current balance. It should clear the amount label and
#   update the current balance label.
#
#   The deposit button should add the amount typed into the amount box to the
#   user's current balance. It should also clear the amount label and update
#   the current balance label.
#
#   Remember that, for these handlers, you will need to convert the strings in
#   the label's to floats before you do your calculations.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 5. (3 pts)
#
#   For this _todo_, bind the window to any keypress so that if the user types
#   a number, it also types that number into the amount label. Remember, you
#   can use isdigit() to check if the key pressed is a digit.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

window = tk.Tk()
window.title("ATM")

balance_label = tk.Label(text="Current Balance ($):")
balance_label.pack()
balance = tk.Label(text="1000")
balance.pack()

amount_label = tk.Label(text="Amount ($):")
amount_label.pack()
amount = tk.Label(text="")
amount.pack()

frame = tk.Frame(height=225, width=225)
frame.pack()
frame.rowconfigure([0, 1, 2, 3], minsize=75, weight=1)
frame.columnconfigure([0, 1, 2], minsize=75, weight=1)

def one():
   current_amount = amount["text"]
   amount.config(text = current_amount + "1")
def two():
   current_amount = amount["text"]
   amount.config(text = current_amount + "2")
def three():
   current_amount = amount["text"]
   amount.config(text = current_amount + "3")
def four():
   current_amount = amount["text"]
   amount.config(text = current_amount + "4")
def five():
   current_amount = amount["text"]
   amount.config(text = current_amount + "5")
def six():
   current_amount = amount["text"]
   amount.config(text = current_amount + "6")
def seven():
   current_amount = amount["text"]
   amount.config(text = current_amount + "7")
def eight():
   current_amount = amount["text"]
   amount.config(text = current_amount + "8")
def nine():
   current_amount = amount["text"]
   amount.config(text = current_amount + "9")
def zero():
   current_amount = amount["text"]
   amount.config(text = current_amount + "0")
def deposit():
   current_amount = float(amount["text"])
   amount.config(text="")
   current_balance = float(balance["text"])
   balance.config(text = current_balance + current_amount)
def withdrawal():
   current_amount = float(amount["text"])
   amount.config(text="")
   current_balance = float(balance["text"])
   balance.config(text = current_balance - current_amount)
def handler(event):
    key = event.char
    if key.isdigit() == True:
        current_amount = amount["text"]
        amount.config(text = current_amount + key)

window.bind("<Any-KeyPress>", handler)

button1 = tk.Button(master=frame, text="1", height=75, width=75, command=one)
button1.grid(row=0, column=0)
button2 = tk.Button(master=frame, text="2", height=75, width=75, command=two)
button2.grid(row=0, column=1)
button3 = tk.Button(master=frame, text="3", height=75, width=75, command=three)
button3.grid(row=0, column=2)
button4 = tk.Button(master=frame, text="4", height=75, width=75, command=four)
button4.grid(row=1, column=0)
button5 = tk.Button(master=frame, text="5", height=75, width=75, command=five)
button5.grid(row=1, column=1)
button6 = tk.Button(master=frame, text="6", height=75, width=75, command=six)
button6.grid(row=1, column=2)
button7 = tk.Button(master=frame, text="7", height=75, width=75, command=seven)
button7.grid(row=2, column=0)
button8 = tk.Button(master=frame, text="8", height=75, width=75, command=eight)
button8.grid(row=2, column=1)
button9 = tk.Button(master=frame, text="9", height=75, width=75, command=nine)
button9.grid(row=2, column=2)
buttonW = tk.Button(master=frame, text="Withdrawal", height=75, width=75, command=withdrawal)
buttonW.grid(row=3, column=0)
button0 = tk.Button(master=frame, text="0", height=75, width=75, command=zero)
button0.grid(row=3, column=1)
buttonD = tk.Button(master=frame, text="Deposit", height=75, width=75, command=deposit)
buttonD.grid(row=3, column=2)

window.mainloop()
