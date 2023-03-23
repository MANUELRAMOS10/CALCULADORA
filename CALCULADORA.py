from tkinter import*
from math import*
root = Tk()
root.title("CALCULADORA")
root.geometry("300x350")

#FUNCIONES QUE REALIZARAN LAS OPERACIONES AL PRESIONAR UN BOTON
def SUMA():
    try:
        NUMEROA = e_NUMEROA.get()
        NUMEROB = e_NUMEROB.get()

        if NUMEROA == "" or NUMEROB == "":
            e_RES.delete(0, END)
            e_RES.insert(0, "FALTAN VALORES")
            
    
        else:
            resultado = float(NUMEROA) + float(NUMEROB)
            e_RES.delete(0, END)
            e_RES.insert(0, resultado)

               
    except:
        e_RES.delete(0, END)
        e_RES.insert(0, 'SINTAX ERROR')


def RESTA():
    try:
        NUMEROA = e_NUMEROA.get()
        NUMEROB = e_NUMEROB.get()

        if NUMEROA == "" or NUMEROB == "":
            e_RES.delete(0, END)
            e_RES.insert(0, "FALTAN VALORES")
            
    
        else:
            resultado = float(NUMEROA) - float(NUMEROB)
            e_RES.delete(0, END)
            e_RES.insert(0, resultado)

               
    except:
        e_RES.delete(0, END)
        e_RES.insert(0, 'SINTAX ERROR')

def MULT():
    try:
        NUMEROA = e_NUMEROA.get()
        NUMEROB = e_NUMEROB.get()

        if NUMEROA == "" or NUMEROB == "":
            e_RES.delete(0, END)
            e_RES.insert(0, "FALTAN VALORES")
            
    
        else:
            resultado = float(NUMEROA) * float(NUMEROB)
            e_RES.delete(0, END)
            e_RES.insert(0, resultado)

               
    except:
        e_RES.delete(0, END)
        e_RES.insert(0, 'SINTAX ERROR')


def DIV():
    try:
        NUMEROA = e_NUMEROA.get()
        NUMEROB = e_NUMEROB.get()

        if NUMEROA == "" or NUMEROB == "":
            e_RES.delete(0, END)
            e_RES.insert(0, "FALTAN VALORES")
            
    
        else:
            resultado = float(NUMEROA) / float(NUMEROB)
            e_RES.delete(0, END)
            e_RES.insert(0, resultado)

               
    except:
        e_RES.delete(0, END)
        e_RES.insert(0, 'SINTAX ERROR')

def CLR():
        e_NUMEROA.delete(0, END)
        e_NUMEROB.delete(0, END)
        e_RES.delete(0, END)


def IGUAL():
    pass

#CREACION DEL FRAME
frameprin = Frame(root)
frameprin.pack()

#CAMPOS PARA INGRESAR DATOS
label_titulo = Label(frameprin , text = "CALCULADORA", font="ROBOTO 20")
label_titulo.grid(row=0, column=0, columnspan=4, pady=8)

label_NUMEROA = Label(frameprin, text="NUMERO A", font="ARIAL 12")
label_NUMEROA.grid(row=1, column=0)


label_NUMEROB = Label(frameprin, text="NUMERO B", font="ARIAL 12")
label_NUMEROB.grid(row=2, column=0)

label_RES = Label(frameprin, text="RESULTADO", font="ARIAL 12")
label_RES.grid(row=3, column=0)

e_NUMEROA = Entry(frameprin, font="ARIAL 12")
e_NUMEROA.grid(row=1,column=2,padx=5)

e_NUMEROB = Entry(frameprin, font="ARIAL 12")
e_NUMEROB.grid(row=2,column=2,padx=5)

e_RES = Entry(frameprin, font="ARIAL 12")
e_RES.grid(row=3,column=2,padx=5)

#BOTONES
bot_suma = Button(frameprin, text="SUMA",font="ARIAL 10",bg= "#A0A0A0", width=10, command= SUMA)
bot_suma.grid(row=4,column=0,columnspan=4, pady=3)

bot_resta = Button(frameprin, text="RESTA",font="ARIAL 10",bg= "#A0A0A0", width=10, command=RESTA)
bot_resta.grid(row=5,column=0,columnspan=4, pady=3)

bot_mul = Button(frameprin, text="MULTIPLICACION",font="ARIAL 10", bg= "#A0A0A0", width=13, command=MULT)
bot_mul.grid(row=6,column=0, columnspan=4, pady=3)

bot_div = Button(frameprin, text="DIVISION",font="ARIAL 10", bg= "#A0A0A0", width=10, command= DIV)
bot_div.grid(row=7,column=0,columnspan=4, pady=3)

bot_clr = Button(frameprin, text="CLEAR",font="ARIAL 10",bg= "#A0A0A0", width=10, command=CLR)
bot_clr.grid(row=8,column=0,columnspan=4, pady=3)

bot_RES = Button(frameprin, text="=S",font="ARIAL 10",bg= "#A0A0A0", width=10, command= SUMA)
bot_RES.grid(row=9,column=0,columnspan=4, pady=3)


root.mainloop()