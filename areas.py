import tkinter as tk
from tkinter import simpledialog
import math
janela = tk.Tk()
janela.title("Areas")


def calcular_triangulo():
    base= simpledialog.askfloat("entrada","qual a base do triangulo? ")
    altura= simpledialog.askfloat("entrada","qual a altura do triangulo? ")
    if base and altura:
        triangulo_area= (base*altura)/2
        print(f"a area do triangulo é: {triangulo_area}")




def calcular_circulo():
    print(math.pi)
    raio= simpledialog.askfloat("entrada","qual o raio do circulo? ")
    if raio:
        circulo_area= math.pi * (raio ** 2)
        print(f"a area do circulo é: {circulo_area}")




def calcular_quadrado():
    lado= simpledialog.askfloat("entrada","qual o lado do quadrado? ")    
    if lado:
        quadrado_area= lado**2
        print(f"a area do quadrado é: {quadrado_area}")  




def calcular_retangulo():
    base= simpledialog.askfloat("entrada","qual a base do retangulo? ")    
    altura= simpledialog.askfloat("entrada","qual a altura do retangulo? ")    
    if base and altura:
        retangulo_area= base*altura
        print(f"a area do retangulo é: {retangulo_area}")




def calcular_trapezio():
    base_menor= simpledialog.askfloat("entrada","qual a base menor do trapézio?")
    base_maior= simpledialog.askfloat("entrada","qual a base maior do trapézio?")
    altura= simpledialog.askfloat("entrada","qual a altura do trapézio?")
    if base_maior and base_menor and altura:
        trapezio_area= ((base_maior+base_menor)*altura)/2
        print(f"a area do trapezio é: {trapezio_area}")




def calcular_losango():
    diagonal_menor= simpledialog.askfloat("entrada","qual a diagonal menor do losango?")
    diagonal_maior= simpledialog.askfloat("entrada","qual a diagonal maior do losango?")
    if diagonal_menor and diagonal_maior:
        losango_area= (diagonal_maior*diagonal_menor)/2
        print(f"a area do losango é: {losango_area}")




btqua= tk.Button(janela, text="quadrado", command=calcular_quadrado)
bttri= tk.Button(janela, text="triângulo", command= calcular_triangulo)
btlos= tk.Button(janela, text="losango", command=calcular_losango)
btret= tk.Button(janela, text="retângulo", command=calcular_retangulo)
btcir= tk.Button(janela, text="circulo", command=calcular_circulo)
bttra= tk.Button(janela, text="trapezio", command=calcular_trapezio)
btqua.pack()
bttri.pack()
btret.pack()
btcir.pack()
btlos.pack()
bttra.pack()
janela.mainloop()
