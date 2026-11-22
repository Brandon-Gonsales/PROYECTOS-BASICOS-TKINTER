global pareja, fila,lista_labels,lista_entrys
pareja=2 #el numero de la pareja que toca mostrar
fila=4 #el numero de la fila donde debemos mostrar
def paralelo(lista):
    num=1
    den=0
    for R in lista:
        ter=1/R
        den=den+ter
    Req=num/den
    return Req

def serie(lista):
    Req=0
    for R in lista:
        Req=Req+R
    return Req


def funcion_serie():
    lista_res=[]
    for entry in lista_entrys:
        if entry.get()!="":
            valor=entry.get()
            lista_res.append(float(valor))
    Req=serie(lista_res)
    rpta_serie.config(text=Req)

def funcion_paralelo():
    lista_res=[]
    for entry in lista_entrys:
        if entry.get()!="":
            valor=entry.get()
            lista_res.append(float(valor))
    
def funcion_mas():
    global pareja, fila,lista_labels,lista_entrys
    if pareja<=9:
        lista_labels[pareja].grid(row=fila,column=0)
        lista_entrys[pareja].grid(row=fila,column=1)
        pareja=pareja+1
        fila=fila+1
    else:
        print("Máximo 10 resistencias")
def funcion_menos():
    global pareja, fila,lista_labels,lista_entrys
    if pareja>=3:

        lista_labels[pareja-1].grid_forget()
        lista_entrys[pareja-1].delete(0, tk.END)
        lista_entrys[pareja-1].grid_forget()
        pareja=pareja-1
        fila=fila-1
    else:
        print("Mínimo 2 resistencias")
    

import tkinter as tk
from tkinter import ttk   
raiz = tk.Tk()
raiz.title("Calculadora Delta-Estrella y Estrella-Delta")
raiz.geometry("500x500")
raiz.resizable(False,False)

header = tk.Frame(raiz, borderwidth=5)
header.grid(row=0, column=0)
titulo_programa =tk.Label(header, text="Calculadora de Resistencias", font=("Arial",20))
titulo_programa.pack()

body=tk.Frame(raiz, borderwidth=5)
body.grid(row=1, column=0)



left=tk.Frame(body, borderwidth=5)
left.grid(row=0, column=0)

sub1=tk.Label(left, text="Datos de los Resistores", font=("Arial",10))
sub1.grid(row=0,column=0, columnspan=2)
bot_mas=tk.Button(left, text="+", command=funcion_mas)
bot_mas.grid(row=1, column=0)
bot_menos=tk.Button(left, text="-", command=funcion_menos)
bot_menos.grid(row=1, column=1)

R1_label=tk.Label(left, text="R1:")
R1_entry=tk.Entry(left)
R2_label=tk.Label(left, text="R2:")
R2_entry=tk.Entry(left)
R3_label=tk.Label(left, text="R3:")
R3_entry=tk.Entry(left)
R4_label=tk.Label(left, text="R4:")
R4_entry=tk.Entry(left)
R5_label=tk.Label(left, text="R5:")
R5_entry=tk.Entry(left)
R6_label=tk.Label(left, text="R6:")
R6_entry=tk.Entry(left)
R7_label=tk.Label(left, text="R7:")
R7_entry=tk.Entry(left)
R8_label=tk.Label(left, text="R8:")
R8_entry=tk.Entry(left)
R9_label=tk.Label(left, text="R9:")
R9_entry=tk.Entry(left)
R10_label=tk.Label(left, text="R10:")
R10_entry=tk.Entry(left)

lista_labels=[R1_label,R2_label,R3_label,R4_label,R5_label,R6_label,R7_label,R8_label,R9_label,R10_label]
lista_entrys=[R1_entry,R2_entry,R3_entry,R4_entry,R5_entry,R6_entry,R7_entry,R8_entry,R9_entry,R10_entry]

R1_label.grid(row=2,column=0)
R1_entry.grid(row=2,column=1)
R2_label.grid(row=3,column=0)
R2_entry.grid(row=3,column=1)




right=tk.Frame(body, borderwidth=5)
right.grid(row=0, column=1)

sub2=tk.Label(right, text="Configuracion Serie", font=("Arial",10))
sub2.grid(row=0,column=0, columnspan=2)

#la imagen ira en la fila 1, columna cero y ocupara 2 columnas

bot_serie=tk.Button(right, text="Calcular", command=funcion_serie)
bot_serie.grid(row=2, column=0)

rpta_serie=tk.Label(right, text="----------", font=("Arial",10))
rpta_serie.grid(row=2,column=1)
#------------------------------------------------------------------
sub3=tk.Label(right, text="Configuracion Paralelo", font=("Arial",10))
sub3.grid(row=3,column=0, columnspan=2)

#la imagen ira en la fila 4, columna cero y ocupara 2 columnas

bot_paralelo=tk.Button(right, text="Calcular", command=funcion_paralelo)
bot_paralelo.grid(row=5, column=0)

rpta_paralelo=tk.Label(right, text="----------", font=("Arial",10))
rpta_paralelo.grid(row=5,column=1)


raiz.mainloop()
