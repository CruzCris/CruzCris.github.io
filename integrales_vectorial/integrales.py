import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

delimitador = True

def calculadora_area(delimitador):

    #ingresamos los valores
    print("\nPara comenzar, ingrese lo siguiente:")
    a = input("Valor de a: ")
    b = input("Valor de b: ")
    c = input("Valor de c: ")
    e = input("Valor de e: ")
    f = input("Valor de f: ")
    print("Para la ecuación de la recta de la forma y=mx+b, ingrese:")
    m = input("Valor de m: ")
    br = input("Valor de b: ")
    print("Para la ecuación de la parábola de la forma y=ax^2+bx+c, ingrese:")
    ap = input("Valor de a: ")
    bp = input("Valor de b: ")
    cp = input("Valor de c: ")

    #validamos los datos ingresados
    def validacion1(a,b,c,e,f):
        try:
            int(a)
            int(b)
            int(c)
            int(e)
            int(f)
            return True
        except ValueError:
            return False

    def validacion2(m,br,ap,bp,cp):
        try:
            float(m)
            float(br)
            float(ap)
            float(bp)
            float(cp)
            return True
        except ValueError:
            return False

    if validacion1(a,b,c,e,f):
        if validacion2(m,br,ap,bp,cp):
            if(float(ap)==0):
                print("El coeficiente a de la parábola no puede ser cero")
                delimitador = True
                return delimitador
            else:
                if(int(e)==int(f)):
                    print("Los valores de e y f no pueden ser iguales, ya que el volumen será cero")
                    delimitador = True
                    return delimitador
                else:
                    print("Los datos ingresados son válidos")
        else:
            print("Los valores de las ecuaciones deben pertenecer a los reales")
            delimitador = True
            return delimitador
    else:
        print("Los primeros cuatro valores deben ser números enteros")
        delimitador = True
        return delimitador

    #comenzamos el desarrollo
    a=int(a)
    b=int(b)
    c=int(c)
    e=int(e)
    f=int(f)
    m=float(m)
    br=float(br)
    ap=float(ap)
    bp=float(bp)
    cp=float(cp)

    #calculamos el volumen
    funcion = lambda y,x: x**a + y**b + c*x*y
    recta = lambda x: m*x + br
    parabola = lambda x: ap*x**2 + bp*x + cp
    u1 = lambda y: e
    u2 = lambda y: f
    i, err =integrate.dblquad(funcion,e,f,recta, parabola)
    if(i<0):
        i=i*-1
        print("El volumen de la región es de: ", i)
    else:
        print("El volumen de la región es de: ",i)

    #graficamos la region
    x=range(e-7,f+7)
    plt.title("Region", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'black'})
    plt.plot(x, [recta(i) for i in x], label='recta')
    plt.plot(x, [parabola(i) for i in x], label='parábola')
    plt.legend(loc='upper right')
    #plt.plot(x, [u1(i) for i in x])
    #plt.plot(x, [u2(i) for i in x])
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.show()

    delimitador = True
    return delimitador

while(delimitador == True):
    calculadora_area(delimitador)