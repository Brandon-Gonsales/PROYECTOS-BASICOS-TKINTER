

def delta_estrella(RA:float,RB:float,RC:float):
    den=RA+RB+RC
    R1=(RB*RC)/den
    R2=(RA*RC)/den
    R3=(RA*RB)/den
    return R1,R2,R3

def estrella_delta(R1:float,R2:float,R3:float):
    num=R1*R2+R2*R3+R1*R3
    RA=num/R1
    RB=num/R2
    RC=num/R3
    return RA,RB,RC

def funcion_delta_estrella():
    R1=float(R1_entry.get())
    R2=float(R2_entry.get())
    R3=float(R3_entry.get())
    RA,RB,RC=delta_estrella(R1,R2,R3)
    cad=f"RA={RA:.2f}, RB={RB:.2f}, RC={RC:.2f}"
    result_label1.config(text=cad)

def funcion_estrella_delta():
    pass
import tkinter as tk
from tkinter import ttk   
raiz = tk.Tk()
raiz.title("Calculadora Delta-Estrella y Estrella-Delta")
raiz.geometry("500x500")
raiz.resizable(False,False)

header = tk.Frame(raiz, borderwidth=5)
header.grid(row=0, column=0)
titulo_programa =tk.Label(header, text="Calculadora Delta Estrella", font=("Arial",20))
titulo_programa.pack()

body=tk.Frame(raiz, borderwidth=5)
body.grid(row=1, column=0)

left=tk.Frame(body, borderwidth=5)
left.grid(row=0, column=0)

sub1=tk.Label(left, text="DELTA-ESTRELLA", font=("Arial",10))
sub1.grid(row=0,column=0, columnspan=2)

#la imagen ira en la fila 1, columna cero y ocupara 2 columnas

R1_label=tk.Label(left, text="R1:")
R1_entry=tk.Entry(left)

R2_label=tk.Label(left, text="R2:")
R2_entry=tk.Entry(left)

R3_label=tk.Label(left, text="R3:")
R3_entry=tk.Entry(left)

R1_label.grid(row=2, column=0)
R1_entry.grid(row=2,column=1)

R2_label.grid(row=3, column=0)
R2_entry.grid(row=3,column=1)

R3_label.grid(row=4, column=0)
R3_entry.grid(row=4,column=1)

bot1=tk.Button(left,text="CALCULAR",command=funcion_delta_estrella)
bot1.grid(row=5, column=0, columnspan=2,sticky="we")

result_label1=tk.Label(left, text="----------", font=("Arial",10))
result_label1.grid(row=6, column=0, columnspan=2)











right=tk.Frame(body, borderwidth=5)
right.grid(row=0, column=1)



sub2=tk.Label(right, text="ESTRELLA-DELTA", font=("Arial",10))
sub2.grid(row=0,column=0, columnspan=2)

#la imagen ira en la fila 1, columna cero y ocupara 2 columnas

RA_label=tk.Label(right, text="R1:")
RA_entry=tk.Entry(right)

RB_label=tk.Label(right, text="R2:")
RB_entry=tk.Entry(right)

RC_label=tk.Label(right, text="R3:")
RC_entry=tk.Entry(right)

RA_label.grid(row=2, column=0)
RA_entry.grid(row=2,column=1)

RB_label.grid(row=3, column=0)
RB_entry.grid(row=3,column=1)

RC_label.grid(row=4, column=0)
RC_entry.grid(row=4,column=1)

bot2=tk.Button(right,text="CALCULAR",command=funcion_estrella_delta)
bot2.grid(row=5, column=0, columnspan=2,sticky="we")

result_label2=tk.Label(right, text="----------", font=("Arial",10))
result_label2.grid(row=6, column=0, columnspan=2)




raiz.mainloop()