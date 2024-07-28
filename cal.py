import customtkinter
import math


app = customtkinter.CTk()
app.title("Calculator")
app.geometry("250x440")
app.resizable(False, False)
customtkinter.set_appearance_mode('dark')



#tab view

tabview = customtkinter.CTkTabview(master=app)
tabview.pack(padx=2, pady=0)

tabview.add("Cal")  # add tab at the end
tabview.add("⚙")  # add tab at the end
tabview.set("Cal")  # set currently visible tab



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
        box1.insert(0,"Error! Cannot devide by 0")
    except:
        clear()
        box1.insert(0,"Unknow Error!")

    
        

def clear():
    cursor_position = box1.index(customtkinter.INSERT)
    box1.delete(0,"end")

def button1_callback():
    cursor_position = box1.index(customtkinter.INSERT)
    box1.insert(cursor_position, 1)
    
def button2_callback():
    cursor_position = box1.index(customtkinter.INSERT)
    box1.insert(cursor_position, 2)

def button3_callback():
    cursor_position = box1.index(customtkinter.INSERT)
    box1.insert(cursor_position, 3)
    
def button4_callback():
    cursor_position = box1.index(customtkinter.INSERT)
    box1.insert(cursor_position, 4)
    
def button5_callback():
    cursor_position = box1.index(customtkinter.INSERT)
    box1.insert(cursor_position, 5)
    
def button6_callback():
    cursor_position = box1.index(customtkinter.INSERT)
    box1.insert(cursor_position, 6)
    
def button7_callback():
    cursor_position = box1.index(customtkinter.INSERT)
    box1.insert(cursor_position, 7)
    
def button8_callback():
    cursor_position = box1.index(customtkinter.INSERT)
    box1.insert(cursor_position, 8)
    
def button9_callback():
    cursor_position = box1.index(customtkinter.INSERT)
    box1.insert(cursor_position, 9)
    
def button0_callback():
    cursor_position = box1.index(customtkinter.INSERT)
    box1.insert(cursor_position, 0)
    
def buttondot_callback():
    cursor_position = box1.index(customtkinter.INSERT)
    box1.insert(cursor_position, '.')
    
def buttondevide_callback():
    cursor_position = box1.index(customtkinter.INSERT)
    box1.insert(cursor_position, '/')
    
def buttonmultiply_callback():
    cursor_position = box1.index(customtkinter.INSERT)
    box1.insert(cursor_position, '*')

def buttonadd_callback():
    cursor_position = box1.index(customtkinter.INSERT)
    box1.insert(cursor_position, '+')

def buttonsubtract_callback():
    cursor_position = box1.index(customtkinter.INSERT)
    box1.insert(cursor_position, '-')
    
def buttonsquare_callback():
    cursor_position = box1.index(customtkinter.INSERT)
    box1.insert(cursor_position,'**2')
    
def buttonnpower_callback():
    cursor_position = box1.index(customtkinter.INSERT)
    box1.insert(cursor_position,'**')
    
def buttonsqrt_callback():
    cursor_position = box1.index(customtkinter.INSERT)
    box1.insert(cursor_position,'math.sqrt()')

def buttondelete_callback():
    eq= box1.get()
    cursor_position = box1.index(customtkinter.INSERT)
    if cursor_position>0:
        eq1 = eq[:cursor_position-1] + eq[cursor_position:]

        box1.delete(0, customtkinter.END)
        box1.insert(0, eq1)  
        box1.icursor(cursor_position-1)

def move_cursor_right():
    current_pos = box1.index(customtkinter.INSERT)
    new_pos=current_pos+1
    box1.icursor(new_pos)

def move_cursor_left():
    current_pos = box1.index(customtkinter.INSERT)
    new_pos=current_pos-1
    box1.icursor(new_pos)

def themesetdark():
    customtkinter.set_appearance_mode('dark')
 
def themesetlight():
    customtkinter.set_appearance_mode('light')   
    
#text box

box1 = customtkinter.CTkEntry(master=tabview.tab("Cal"), state='normal', width=200, height=35, font=('', 15))
box1.pack(side='top', pady=10)


#frame1

myframe = customtkinter.CTkFrame(master=tabview.tab("Cal"))
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

comframe=customtkinter.CTkFrame(master=tabview.tab("Cal"))
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
buttonans = customtkinter.CTkButton(comframe, text="=", command=Cal, font=('',20), width=143)
buttonans.grid(row=3, column=0, padx=1, pady=1, columnspan=2,)

buttonleft = customtkinter.CTkButton(comframe, text="→", command=move_cursor_right, font=('',20), width=70)
buttonleft.grid(row=3, column=2, padx=1, pady=1, columnspan=1,)
buttonright = customtkinter.CTkButton(comframe, text="←", command=move_cursor_left, font=('',20), width=70)
buttonright.grid(row=2, column=2, padx=1, pady=1, columnspan=1)


def segmented_button_callback(value):
    if value=="Dark":
        themesetdark()
    else:
        themesetlight()

segemented_button = customtkinter.CTkSegmentedButton(master=tabview.tab("⚙"), values=["Dark", "Light"],
                                                     command=segmented_button_callback)
segemented_button.set("Dark")
segemented_button.pack(pady=1)


app.mainloop()