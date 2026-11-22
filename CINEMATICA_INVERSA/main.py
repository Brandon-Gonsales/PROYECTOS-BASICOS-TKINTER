import tkinter
import tkinter
import numpy as np
def degree(angle:float):
    x=(180*angle)/(np.pi)
    return x
def get_angles(x: float, y: float, a1: float, a2: float):
    q2=np.arccos((x**2+y**2-a1**2-a2**2)/2*a1*a2)
    q1=np.arctan(y/x)-np.arctan((a2*np.sin(q2)/(a1+a2*np.cos(q2))))
    q1=degree(q1)
    q2=degree(q2)
    return q1,q2

def funcion_de_calculo():
    #primero capturamos nuestras 4 variables de entrada
    #que estan en los entrys
    x = float(x_entry.get())
    y = float(y_entry.get())
    a1 = float(a1_entry.get())
    a2 = float(a2_entry.get())
    #mandamos esas cuatro variables a nuestra funcion get angles
    q1,q2=get_angles(x,y,a1,a2)
    q1=round(q1,2)
    q2=round(q2,2)
    #la funcion nos devolvera los 2 angulo y ahora podemos mostrarlos en nuestra interfaz grafica
    #modificando los textos de q1_result y q2_result
    q1_result.config(text=f"{q1}")
    q2_result.config(text=f"{q2}")
   

import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()
raiz.title("Calculadora de Cinematica Inversa")
raiz.geometry("500x500")
raiz.resizable(False,False)

#frame del titulo
header = tk.Frame(raiz, borderwidth=5)
header.grid(row=0, column=0)
#titulazo
titulo_programa =tk.Label(header, text="Calculadora de Cinematica Inversa", font=("Arial",20))
titulo_programa.pack()

#AQUI EMPIEZA EL CUERPO DEL PROGRAMA --------------------------------------------------------------------------
body=tk.Frame(raiz, borderwidth=5)
body.grid(row=1, column=0)
#TODO ESTO ES LO QUE VA EN LA PARTE IZQUIERDA--------------------------------------------------------------------
left=tk.Frame(body, borderwidth=5)
left.grid(row=0, column=0)


#frame de las variables de entrada
input_frame=tk.Frame(left, borderwidth=5)
input_frame.grid(row=0, column=0)



subtitle_input=tk.Label(input_frame, text="Datos de Entrada", font=("Arial",10))

x=tk.Label(input_frame, text="Posicion en x:")
x_entry=tk.Entry(input_frame)

y=tk.Label(input_frame, text="Posicion en y:")
y_entry=tk.Entry(input_frame)

a1=tk.Label(input_frame, text="Longitud del brazo 1:")
a1_entry=tk.Entry(input_frame)

a2=tk.Label(input_frame, text="Longitud del brazo 2:")
a2_entry=tk.Entry(input_frame)

subtitle_input.grid(row=0, column=0, columnspan=2)
x.grid(row=1, column=0)
x_entry.grid(row=1, column=1)
y.grid(row=2, column=0)
y_entry.grid(row=2, column=1)
a1.grid(row=3, column=0)
a1_entry.grid(row=3, column=1)
a2.grid(row=4, column=0)
a2_entry.grid(row=4, column=1)

#frame de las variables de salida
output_frame=tk.Frame(left, borderwidth=5)
output_frame.grid(row=1, column=0)

subtitle_output=tk.Label(output_frame, text="Datos de Salida", font=("Arial",10))

q1=tk.Label(output_frame, text="Angulo q1:")
q1_result=tk.Label(output_frame, text="------")

q2=tk.Label(output_frame, text="Angulo q2:")
q2_result=tk.Label(output_frame, text="------")

subtitle_output.grid(row=0, column=0, columnspan=2)
q1.grid(row=1, column=0)
q1_result.grid(row=1, column=1)
q2.grid(row=2, column=0)
q2_result.grid(row=2, column=1)
#TODO ESTO ES LO QUE VA EN LA PARTE DERECHA -----------------------------------------------------------
right=tk.Frame(body, borderwidth=5)
right.grid(row=0, column=1)
lienzo=tk.Canvas(right, width=200, height=200, bg="white")
leyenda=tk.Label(right, text="Brazo Robotico con dos grados de libertad")
boton=tk.Button(right,text="CALCULAR",command=funcion_de_calculo)
lienzo.grid(row=0, column=0)
leyenda.grid(row=1, column=0)
boton.grid(row=2, column=0)



raiz.mainloop()