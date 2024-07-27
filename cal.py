import customtkinter
import math


app = customtkinter.CTk()
app.title("Calculator")
app.geometry("250x350")
app.resizable(False, False)

#commands
def Cal():
    try:
        eq = box1.get()
        # new_eq = eq.replace()
        result = eval(eq)
        clear()
        box1.insert(0,result)
    except ZeroDivisionError:
        clear()
    except:
        clear()
        

def clear():
    box1.delete(0,"end")

def button1_callback():
    box1.insert('end', 1)
    
def button2_callback():
    box1.insert('end', 2)

def button3_callback():
    box1.insert('end', 3)
    
def button4_callback():
    box1.insert('end', 4)
    
def button5_callback():
    box1.insert('end', 5)
    
def button6_callback():
    box1.insert('end', 6)
    
def button7_callback():
    box1.insert('end', 7)
    
def button8_callback():
    box1.insert('end', 8)
    
def button9_callback():
    box1.insert('end', 9)
    
def button0_callback():
    box1.insert('end', 0)
    
def buttondot_callback():
    box1.insert('end', '.')
    
def buttondevide_callback():
    box1.insert('end', '/')
    
def buttonmultiply_callback():
    box1.insert('end', '*')

def buttonadd_callback():
    box1.insert('end', '+')

def buttonsubtract_callback():
    box1.insert('end', '-')
    
def buttonsquare_callback():
    box1.insert('end','**2')
    
def buttonnpower_callback():
    box1.insert('end','**')
    
def buttonsqrt_callback():
    box1.insert('end','math.sqrt()')

def buttondelete_callback():
    eq=box1.get()
    eq1=eq[:len(eq)-1]
    clear()
    box1.insert('end',eq1)


#text box

box1 = customtkinter.CTkEntry(app, state='normal', width=200, height=35, font=('', 15))
box1.pack(side='top', pady=10)

# scroll = customtkinter.CTkScrollbar(app, command=lambda *args: box1.xview(*args) ,orientation='horizontal')
# scroll.pack(side='top', fill='x')
# box1.configure(xscrollcommand=scroll.set)

#frame1

myframe = customtkinter.CTkFrame(app)
myframe.pack(pady=10)

#buttons

button1 = customtkinter.CTkButton(myframe, text="1", command=button1_callback, font=('', 20), width=70)
button1.grid(row=2, column=0, padx=1, pady=1, columnspan=1)
button2 = customtkinter.CTkButton(myframe, text="2", command=button2_callback, font=('', 20), width=70)
button2.grid(row=2, column=1, padx=1, pady=1, columnspan=1)
button3 = customtkinter.CTkButton(myframe, text="3", command=button3_callback, font=('', 20), width=70)
button3.grid(row=2, column=2, padx=1, pady=1, columnspan=1)

button4 = customtkinter.CTkButton(myframe, text="4", command=button4_callback, font=('', 20), width=70)
button4.grid(row=3, column=0, padx=1, pady=1, columnspan=1)
button5 = customtkinter.CTkButton(myframe, text="5", command=button5_callback, font=('', 20), width=70)
button5.grid(row=3, column=1, padx=1, pady=1, columnspan=1)
button6 = customtkinter.CTkButton(myframe, text="6", command=button6_callback, font=('', 20), width=70)
button6.grid(row=3, column=2, padx=1, pady=1, columnspan=1)

button7 = customtkinter.CTkButton(myframe, text="7", command=button7_callback, font=('', 20), width=70)
button7.grid(row=4, column=0, padx=1, pady=1, columnspan=1)
button8 = customtkinter.CTkButton(myframe, text="8", command=button8_callback, font=('', 20), width=70)
button8.grid(row=4, column=1, padx=1, pady=1, columnspan=1)
button9 = customtkinter.CTkButton(myframe, text="9", command=button9_callback, font=('', 20), width=70)
button9.grid(row=4, column=2, padx=1, pady=1, columnspan=1)

button0 = customtkinter.CTkButton(myframe, text="0", command=button0_callback, font=('', 20), width=70)
button0.grid(row=5, column=1, padx=1, pady=1, columnspan=1)


buttondel = customtkinter.CTkButton(myframe, text="C", command=clear, font=('', 20), width=70)
buttondel.grid(row=5, column=0, padx=1, pady=1, columnspan=1)
buttondot = customtkinter.CTkButton(myframe, text=".", command=buttondot_callback, font=('', 20), width=70)
buttondot.grid(row=5, column=2, padx=1, pady=1, columnspan=1)

comframe=customtkinter.CTkFrame(app)
comframe.pack(pady=10)

buttonplus = customtkinter.CTkButton(comframe, text="+", command=buttonadd_callback, font=('', 20), width=70)
buttonplus.grid(row=0, column=0, padx=1, pady=1, columnspan=1)
buttonminus = customtkinter.CTkButton(comframe, text="-", command=buttonsubtract_callback, font=('', 20), width=70)
buttonminus.grid(row=0, column=1, padx=1, pady=1, columnspan=1)
buttondevide = customtkinter.CTkButton(comframe, text="÷", command=buttondevide_callback, font=('', 20), width=70)
buttondevide.grid(row=1, column=1, padx=1, pady=1, columnspan=1)
buttonmultiply = customtkinter.CTkButton(comframe, text="×", command=buttonmultiply_callback, font=('', 20), width=70)
buttonmultiply.grid(row=1, column=0, padx=1, pady=1, columnspan=1)
buttonsquare = customtkinter.CTkButton(comframe, text='a²', command=buttonsquare_callback,font=('', 20), width=70)
buttonsquare.grid(row=1, column=2,pady=1, padx=1, columnspan=1)
buttonnpower = customtkinter.CTkButton(comframe, text='aᵡ', command=buttonnpower_callback,font=('', 20), width=70)
buttonnpower.grid(row=2, column=0,pady=1, padx=1, columnspan=1)
buttonsqrt = customtkinter.CTkButton(comframe, text='√', command=buttonsqrt_callback,font=('', 20), width=70)
buttonsqrt.grid(row=2, column=1,pady=1, padx=1, columnspan=1)
buttondelete = customtkinter.CTkButton(comframe, text='⌫', command=buttondelete_callback,font=('', 20), width=70)
buttondelete.grid(row=0, column=2,pady=1, padx=1, columnspan=1)
buttonans = customtkinter.CTkButton(comframe, text="=", command=Cal, font=('',20), width=70)
buttonans.grid(row=2, column=2, padx=1, pady=1, columnspan=1,)


app.mainloop()