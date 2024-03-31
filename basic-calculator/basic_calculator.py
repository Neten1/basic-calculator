from tkinter import *
from random import uniform
##### All functions ######
#function_name - defines function connected to a button
#any other function is just an utility
def number_add(number):
    global state
    if number == 0 and str(output.get()) == "0":
        return
    elif length_limit():
         previous_number_label.configure(text="Given number exceeds this calculator's size limit. (32)")
         return
    elif str(output.get()) == "0":
        clear()
        state = False
    elif state:
        clear()
        state = False
    output.insert(INSERT, number)

def number_remove_last():
    value = output.get()
    value = value[0:len(value)-1]
    clear()
    output.insert(INSERT, value)

def function_clear():
    global first
    first = 0
    clear()
    output.insert(INSERT, 0)
    previous_number_label.configure(text="")
    button_empty.configure(state=NORMAL)

def function_empty():
    global first, state, operation
    if operation == "√":
        function_clear()
    elif first == 0:
        if str(output.get()) != "0":
            function_clear()
        else:
            operation = "random"
            previous_number_label.configure(text="Random number between : ")
    else:
        previous_number_label.configure(text=f"{output.get()} {operation}")
        clear()
        output.insert(INSERT, 0)
        state = True

def clear():
    output.delete(0, END)

def set_previous_label():
    global operation, first
    previous_number_label.configure(text=f"{first} {operation}")

def length_limit():
    if len(str(output.get())) >= 32:
        return True
    else:
        return False

def get_fraction_len(number):
    length = len(str(number)) - 1
    if length == 0:
        return 0
    return length-1
## OPERATIONS ##
def function_equal():
    try:
        second = float(output.get())
    except:
        error_handling()
        second = 0
    finally:
        global operation, first, state, random_end
        match operation:
            case "+":
                val = first + second
            case "-":
                val = first - second
            case "*":
                val = first * second
            case "/":
                if second != 0:
                    val = first / second
                else:
                    val = 0
                    previous_number_label.configure(text=f"Divison by zero!")
                    operation = "error"
            case "^":
                val = first ** second
            case "√":
                if first < 0:
                    val = 0
                    previous_number_label.configure(text="Negative square root!")
                else:
                    val = first ** 0.5
            case "random":
                first = int(float(output.get()))
                if str(first) != output.get():
                    first = second
                operation = "random number"
                previous_number_label.configure(text=f"Random number between : {first} - ")
                state = True
                button_empty.configure(state=DISABLED)
                return
            case "random number":
                if str(int(second)) == output.get():
                    second = int(second)
                random_end = second
                if second == first:
                    function_clear()
                    previous_number_label.configure(text="This range has only 1 possible value!")
                    return
                by_amount = max(get_fraction_len(first), get_fraction_len(second))
                val = round(uniform(min(first, second) , max(first, second)),by_amount)
                previous_number_label.configure(text=f"Random number between : {first} - {second}")
                state = True
                clear()
                output.insert(INSERT, val)
                operation = "random again"
                return
            case "random again":
                if random_end == first:
                    function_clear()
                    previous_number_label.configure(text="This range has only 1 possible value!")
                    return
                by_amount = max(get_fraction_len(first), get_fraction_len(random_end))
                val = round(uniform(min(first, random_end) , max(first, random_end)),by_amount)
                previous_number_label.configure(text=f"Random number between : {first} - {random_end}")
                state = True
                clear()
                output.insert(INSERT, val)
                return
            case _:
                val = 0
        if val <= 99999999999999999999999999999999:
            if operation != "error" and operation != "√":
                set_previous_label()
                previous_number_label.configure(text=f"{previous_number_label.cget("text")} {second} =")
            clear()
            if val // 1 == val:
                val = int(val)
            state = True
            output.insert(INSERT, val)
            button_empty.configure(state=NORMAL)
        else:
            previous_number_label.configure(text="This result exceeds calculator's size limit. (32)")
            clear()
            output.insert(INSERT, 0)

def function_add():
    global first, operation, state
    first = float(output.get())
    operation = "+"
    state = True
    previous_number_label.configure(text=f"{first} +")

def function_subtract():
    global first, operation, state
    first = float(output.get())
    operation = "-"
    state = True
    previous_number_label.configure(text=f"{first} -")

def function_multiply():
    global first, operation, state
    first = float(output.get())
    operation = "*"
    state = True
    previous_number_label.configure(text=f"{first} *")

def function_divide():
    global first, operation, state
    first = float(output.get())
    operation = "/"
    state = True
    previous_number_label.configure(text=f"{first} /")

def function_power():
    global first, operation, state
    first = float(output.get())
    operation = "^"
    state = True
    previous_number_label.configure(text=f"{first} ^")

def function_root():
    global first, operation, state
    first = float(output.get())
    operation = "√"
    state = True
    previous_number_label.configure(text=f"√{first} =")
    function_equal()

def function_switch():
    value = output.get()
    if str(value) != "0":
        clear()
        value = float(value)
        if value // 1 == value:
            value = int(value)
        value *= -1
        output.insert(INSERT, value)

def function_comma():
    value = float(output.get())
    if value // 1 == value:
        clear()
        value = str(int(value))+"."
        output.insert(INSERT, value)

def function_invert():
    value = float(output.get())
    if value == 0:
        return
    value = 1/value
    clear()
    output.insert(INSERT, value)


##### GUI CREATION #####
#Initializing global variables with base values
global state, first, operation, random_end
operation = "+"
state = False
first = 0

#Creating the main GUI
root = Tk()
root.title("Basic Calculator")
root.iconbitmap('icon.ico')

window_width = 420
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 -  window_height/ 2)

root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.resizable(False, False)

#Creating all contents
output = Entry(root, width=32, borderwidth=16, font=("Arial", 16))
output.grid(row=0, column=0, columnspan=4, pady=3)
output.insert(INSERT, 0)
previous_number_label = Label(root, text="Hello user!", font=("Arial", 12), fg="#858585")
previous_number_label.grid(row=1, column=0, columnspan=4, sticky=W)

button_comma = Button(root, text=",", font=("Arial", 12), width=9, height=3, command=function_comma)
button_switch = Button(root, text="+/-", font=("Arial", 12), width=9, height=3, command=function_switch)
button_0 = Button(root, text="0", font=("Arial", 12), width=9, height=3, command=lambda: number_add(0))
button_1 = Button(root, text="1", font=("Arial", 12), width=9, height=3, command=lambda: number_add(1))
button_2 = Button(root, text="2", font=("Arial", 12), width=9, height=3, command=lambda: number_add(2))
button_3 = Button(root, text="3", font=("Arial", 12), width=9, height=3, command=lambda: number_add(3))
button_4 = Button(root, text="4", font=("Arial", 12), width=9, height=3, command=lambda: number_add(4))
button_5 = Button(root, text="5", font=("Arial", 12), width=9, height=3, command=lambda: number_add(5))
button_6 = Button(root, text="6", font=("Arial", 12), width=9, height=3, command=lambda: number_add(6))
button_7 = Button(root, text="7", font=("Arial", 12), width=9, height=3, command=lambda: number_add(7))
button_8 = Button(root, text="8", font=("Arial", 12), width=9, height=3, command=lambda: number_add(8))
button_9 = Button(root, text="9", font=("Arial", 12), width=9, height=3, command=lambda: number_add(9))
button_equals = Button(root, text="=", font=("Arial", 12), width=14, height=3, command=function_equal, bg="#ffbe52")
button_add = Button(root, text="+", font=("Arial", 12), width=14, height=3, command=function_add, bg="#dddddd")
button_subtract = Button(root, text="-", font=("Arial", 12), width=14, height=3, command=function_subtract, bg="#dddddd")
button_multiply = Button(root, text="*", font=("Arial", 12), width=14, height=3, command=function_multiply, bg="#dddddd")
button_divide = Button(root, text="/", font=("Arial", 12), width=14, height=3, command=function_divide, bg="#dddddd")
button_power = Button(root, text="^", font=("Arial", 12), width=9, height=3, command=function_power, bg="#dddddd")
button_square_root = Button(root, text="√", font=("Arial", 12), width=9, height=3, command=function_root, bg="#dddddd")
button_invert = Button(root, text="1/x", font=("Arial", 12), width=9, height=3, command=function_invert, bg="#dddddd")

button_clear = Button(root, text="C", font=("Arial", 12), width=19, height=3, command=function_clear, bg="#c1c1c1")
button_empty = Button(root, text="CE", font=("Arial", 12), width=9, height=3, command=function_empty, bg="#c1c1c1")
button_delete_last = Button(root, text="<", font=("Arial", 12), width=14, height=3, command=number_remove_last, bg="#c1c1c1")

#Positioning all contents
button_clear.grid(row=2, column=0, columnspan=2, ipadx=2)
button_empty.grid(row=2, column=2)
button_delete_last.grid(row=2, column=3)

button_invert.grid(row=3, column=0)
button_power.grid(row=3, column=1)
button_square_root.grid(row=3, column=2)
button_divide.grid(row=3, column=3)

button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)
button_multiply.grid(row=4, column=3)

button_4.grid(row=5, column=0)
button_5.grid(row=5, column=1)
button_6.grid(row=5, column=2)
button_subtract.grid(row=5, column=3)

button_1.grid(row=6, column=0)
button_2.grid(row=6, column=1)
button_3.grid(row=6, column=2)
button_add.grid(row=6, column=3)

button_switch.grid(row=7, column=0)
button_0.grid(row=7, column=1)
button_comma.grid(row=7, column=2)
button_equals.grid(row=7, column=3)

#Mainloop
root.mainloop()
