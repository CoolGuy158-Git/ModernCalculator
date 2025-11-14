import customtkinter

# set of colors
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("500x400")
root.title("Modern Calculator")
root.resizable(False, False)

Screen = customtkinter.CTkLabel(root, width=15, height=1, text=" ", font=("Arial", 40), anchor="e")
Screen.pack(pady=20)
MAX_CHARS = 21
def show_input(value):
    current = Screen.cget("text")
    if len(current) < MAX_CHARS:
        Screen.configure(text=current + value)

# Calculation
def calculate():
    try:
        expression = Screen.cget("text")
        result = eval(expression)
        Screen.configure(text=str(result))
    except (SyntaxError, ZeroDivisionError, TypeError, NameError):
        Screen.configure(text="Error")
        Screen.after(1000, lambda: Screen.configure(text=""))

# Keypress handling
def keypress(event):
    key = event.char
    if key.isdigit() or key in "+-*/":
        show_input(key)
    elif key == "\r" or key == "=":
        calculate()
    elif key.lower() == "c":
        Screen.configure(text="")
def clear_screen():
    Screen.configure(text="")

root.bind("<Key>", keypress)
one = customtkinter.CTkButton(root, width=100, height=50, text="1", command=lambda: show_input("1"),fg_color=None, border_width=2, border_color="gray", hover_color="gray" )
one.place(x=34, y=110)
two = customtkinter.CTkButton(root, width=100, height=50, text="2", command=lambda: show_input("2"),fg_color=None, border_width=2, border_color="gray", hover_color="gray")
two.place(x=34, y=160)
three = customtkinter.CTkButton(root, width=100, height=50, text="3", command=lambda: show_input("3"),fg_color=None, border_width=2, border_color="gray", hover_color="gray")
three.place(x=34, y=210)
four = customtkinter.CTkButton(root, width=100, height=50, text="4", command=lambda: show_input("4"),fg_color=None, border_width=2, border_color="gray", hover_color="gray")
four.place(x=34, y=260)
five = customtkinter.CTkButton(root, width=100, height=50, text="5", command=lambda: show_input("5"),fg_color=None, border_width=2, border_color="gray", hover_color="gray")
five.place(x=34, y=310)
six = customtkinter.CTkButton(root, width=100, height=50, text="6", command=lambda: show_input("6"),fg_color=None, border_width=2, border_color="gray", hover_color="gray")
six.place(x=134, y=110)
seven = customtkinter.CTkButton(root, width=100, height=50, text="7", command=lambda: show_input("7"),fg_color=None, border_width=2, border_color="gray", hover_color="gray")
seven.place(x=134, y=160)
eight = customtkinter.CTkButton(root, width=100, height=50, text="8", command=lambda: show_input("8"),fg_color=None, border_width=2, border_color="gray", hover_color="gray")
eight.place(x=134, y=210)
nine = customtkinter.CTkButton(root, width=100, height=50, text="9", command=lambda: show_input("9"),fg_color=None, border_width=2, border_color="gray", hover_color="gray")
nine.place(x=134, y=260)
zero = customtkinter.CTkButton(root, width=100, height=50, text="0", command=lambda: show_input("0"),fg_color=None, border_width=2, border_color="gray", hover_color="gray")
zero.place(x=134, y=310)

# Operations
addition = customtkinter.CTkButton(root, width=100, height=50, text="+", command=lambda: show_input("+"),fg_color=None, border_width=2, border_color="gray", hover_color="gray",)
addition.place(x=234, y=110)
subtraction = customtkinter.CTkButton(root, width=100, height=50, text="-", command=lambda: show_input("-"),fg_color=None, border_width=2, border_color="gray", hover_color="gray")
subtraction.place(x=234, y=160)
division = customtkinter.CTkButton(root, width=100, height=50, text="/", command=lambda: show_input("/"),fg_color=None, border_width=2, border_color="gray", hover_color="gray")
division.place(x=234, y=210)
multiplication = customtkinter.CTkButton(root, width=100, height=50, text="*", command=lambda: show_input("*"),fg_color=None, border_width=2, border_color="gray", hover_color="gray")
multiplication.place(x=234, y=260)
equal = customtkinter.CTkButton(root, width=100, height=110, text="=",fg_color=None, border_width=2, border_color="gray", hover_color="gray", command=calculate,)
equal.place(x=380, y=170)

# Extras
Clear = customtkinter.CTkButton(root, width=100, height=50, text="Clear",fg_color=None, border_width=2, border_color="gray", hover_color="gray", command=clear_screen)
Clear.place(x=234, y=310)

root.mainloop()


