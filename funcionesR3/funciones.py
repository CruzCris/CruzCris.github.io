import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from numpy import linalg
from scipy.integrate import quad
from mpl_toolkits import mplot3d
plt.style.use('seaborn-poster')

delimitador = True

def grafica(delimitador):

    #ingresamos los valores
    print("\nPara comenzar, ingrese las coordenadas del punto de impacto (x,y) y la altura máxima")
    x = input("Coordenada X: ")
    y = input("Coordenada Y: ")
    h = input("Altura máxima: ")

    #validamos los valores ingresados
    def validacion1(x, y, h):
        try:
            float(x)
            float(y)
            float(h)
            return True
        except ValueError:
            return False

    def validacion2(h):
        try:
            h = float(h)
            if (h>0):
                return True
        except ValueError:
            return False

    if validacion1(x, y, h):
        if validacion2(h):
            x = float(x)
            y = float(y)
            h = float(h)
            pi = [x, y]
            print("\nLos valores ingresados son:")
            print("Altura: ", h)
            print("Punto de impacto: ", pi)
        else:
            print("La altura debe de ser mayor a 0")
            exit()
    else:
        print("Sólo se pueden ingresar números reales")
        exit()

    #comenzamos el análisis
    h=float(h)
    y=float(y)
    x=float(x)

    '''tendremos 3 casos:
    cuando x=0
    cuando y=0
    cuando ambos sean diferentes de 0'''

    def grafica_y(h,y,x):

        '''sistema de ecuaciones
        z=ay^2+by+c
        0=a(0)^2+b(0)+c --> ecuación 1 (origen y=0, z=0)
        9=a(3.5)^2+b(3.5)+c --> ecuación 2 (altura máxima y mitad de coordenada Y de impacto)
        0=a(7)^2+b(7)+c --> ecuación 3 (coordenadas de impacto --> z=0)'''

        c=0
        y1=y/2 #punto medio de Y
        y1_2=y1*y1
        z2=0
        y2=y
        y2_2=y*y
        Y = y

        nrow1 = [y1_2,y1]
        nrow2 = [y2_2,y2]
        nmat = np.array([nrow1,nrow2])
        cons = np.array([h,z2])
        answer = linalg.solve(nmat,cons)
        aval = answer[0]
        bval = answer[1]

        def f(y):
            return aval*y**2 + bval*y + c
        print("\nLa ecuación de la parábola es: ",aval,"y^2 +",bval,"y +",c)

        print("\nLa ecuación vectorial sería: (",c,", t, ",aval,"t^2 +",bval,"t)")

        #graficamos
        t = sp.Symbol('t')
        function_x = sp.sympify('0*t')
        function_y = sp.sympify('t')
        function_z = sp.sympify(aval*t**2+bval*t)
        interval = np.arange(y+1)
        x_values = [function_x.subs(t, value) for value in interval]
        y_values = [function_y.subs(t, value) for value in interval]
        z_values = [function_z.subs(t, value) for value in interval]
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot(x_values, y_values, z_values)
        ax.set_title('Tiro Parabólico con Funciones Vectoriales')
        ax.set_xlabel('x', labelpad=20)
        ax.set_ylabel('y', labelpad=20)
        ax.set_zlabel('z', labelpad=20)

        # para calcular la tangente
        y = sp.Symbol('y')
        dy = sp.Derivative(f(y), y)
        dy = dy.doit()
        print("\nLa derivada de la ecuación es: ", dy)
        dye = dy.doit().subs({y:y1})
        vdx = 0
        vdy = 1
        vdz = dye
        vd = [vdx, vdy, vdz]
        vx = 0
        vy = y1
        vz = f(y1)
        v1 = [vx, vy, vz]
        print("Coordenada: ", v1)
        print("Vector director: ",vd)
        function_x2 = sp.sympify(vx+vdx*t)
        function_y2 = sp.sympify(vy+vdy*t)
        function_z2 = sp.sympify(vz+vdz*t)
        interval2 = np.arange(y1+10)
        x2_values = [function_x2.subs(t, value) for value in interval2]
        y2_values = [function_y2.subs(t, value) for value in interval2]
        z2_values = [function_z2.subs(t, value) for value in interval2]
        ax.plot(x2_values, y2_values, z2_values)

        # para la longitud del arco
        #dy = dy * dy
        dz1 = aval*2
        def f(y):
            return (1+(dz1*y+bval)**2)**(1/2)
        i, err = quad(f, c, Y)
        print("\nLa longitud de arco de la parábola es: ",i)

        ax.plot(0,0,0,'bo', c='black')
        ax.plot(vx,vy,vz,'bo', c='purple')
        ax.plot(0,Y,0,'bo', c='brown')
        plt.show()

    def grafica_x(h,y,x):

        '''sistema de ecuaciones
        z=ax^2+bx+c
        0=a(0)^2+b(0)+c --> ecuación 1 (origen x=0, z=0)
        9=a(3.5)^2+b(3.5)+c --> ecuación 2 (altura máxima y mitad de coordenada Y de impacto)
        0=a(7)^2+b(7)+c --> ecuación 3 (coordenadas de impacto --> z=0)'''

        c = 0
        x1 = x / 2
        x1_2 = x1 * x1
        z2 = 0
        x2 = x
        x2_2 = x * x
        X = x

        nrow1 = [x1_2, x1]
        nrow2 = [x2_2, x2]
        nmat = np.array([nrow1, nrow2])
        cons = np.array([h, z2])
        answer = linalg.solve(nmat, cons)
        aval = answer[0]
        bval = answer[1]

        def f(x):
            return aval * x ** 2 + bval * x + c
        print("\nEcuación de la parábola: ", aval, "x^2 +", bval, "x +", c)

        print("\nLa ecuación vectorial sería: (t, ", c, ", ", aval, "t^2 +", bval, "t)")

        # graficamos
        t = sp.Symbol('t')
        function_x = sp.sympify('t')
        function_y = sp.sympify('0*t')
        function_z = sp.sympify(aval * t ** 2 + bval * t)
        interval = np.arange(x + 1)
        x_values = [function_x.subs(t, value) for value in interval]
        y_values = [function_y.subs(t, value) for value in interval]
        z_values = [function_z.subs(t, value) for value in interval]
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot(x_values, y_values, z_values)
        ax.set_title('Tiro Parabólico con Funciones Vectoriales')
        ax.set_xlabel('x', labelpad=20)
        ax.set_ylabel('y', labelpad=20)
        ax.set_zlabel('z', labelpad=20)

        # para calcular la tangente
        x = sp.Symbol('x')
        dx = sp.Derivative(f(x), x)
        dx = dx.doit()
        print("\nLa derivada de la ecuación es: ", dx)
        dxe = dx.doit().subs({x: x1})
        vdx = x1
        vdy = 0
        vdz = dxe
        vd = [vdx, vdy, vdz]
        vx = x1
        vy = 0
        vz = f(x1)
        v1 = [vx, vy, vz]
        print("Coordenada: ", v1)
        print("Vector director: ", vd)
        function_x2 = sp.sympify(vx + vdx * t)
        function_y2 = sp.sympify(vy + vdy * t)
        function_z2 = sp.sympify(vz + vdz * t)
        interval2 = np.arange(x1 + 10)
        x2_values = [function_x2.subs(t, value) for value in interval2]
        y2_values = [function_y2.subs(t, value) for value in interval2]
        z2_values = [function_z2.subs(t, value) for value in interval2]
        ax.plot(x2_values, y2_values, z2_values)

        # para la longitud del arco
        dz1 = aval * 2
        def f(x):
            return (1 + (dz1 * x + bval)**2)**(1/2)
        i, err = quad(f,c,X)
        print("\nLa longitud de arco de la parábola es: ", i)

        ax.plot(0, 0, 0, 'bo', c='black')
        ax.plot(vx, vy, vz, 'bo', c='purple')
        ax.plot(X, 0, 0, 'bo', c='brown')
        plt.show()

    def grafica_xy(h,y,x):

        '''en este caso haremos uso de dos ecuaciones: una de parábola y una de línea recta
        la parábola la usaremos en el plano yz, por lo que la ecuación sería -> z=ay^2+by+c
        la ecuación de línea recta la usaremos ya que viendo la parábola desde una vista superior,
        sólo se notaría una línea recta, por lo que usaremos -> (y-y1)=m(x-x1)
        y como usamos a y en la parábola y en la recta entonces -> y=t
        '''

        c = 0
        z1 = h #punto medio de z
        y1 = y/2 #punto medio de y
        y1_2 = y1*y1
        z2 = 0
        y2 = y
        y2_2 = y*y
        x1 = x
        Y = y

        #para calcular la ecuación de la recta
        #puntos para calcularla -> (0,0), (x,y)
        m = (y2-0)/(x1-0)
        def f(y):
            return (1/m)*y
        print("\nLa ecuación de la recta es: y/",m)
        y = sp.Symbol('y')
        dY = sp.Derivative(f(y), y)
        dY = dY.doit()
        vx = f(y1)

        #para calular la ecuación de la parábola
        nrow1 = [y1_2, y1]
        nrow2 = [y2_2, y2]
        nmat = np.array([nrow1, nrow2])
        cons = np.array([z1, z2])
        answer = linalg.solve(nmat, cons)
        aval = answer[0]
        bval = answer[1]

        def f(y):
            return aval*y**2 + bval*y + c
        print("La ecuación de la parábola es: ",aval,"y^2 +",bval,"y +",c)
        dy = sp.Derivative(f(y), y)
        dy = dy.doit()

        print("\nLa ecuación vectorial sería: (t/",m,", t, ",aval,"t^2+",bval,"t)")

        # graficamos
        t = sp.Symbol('t')
        function_x = sp.sympify(t/m)
        function_y = sp.sympify('t')
        function_z = sp.sympify(aval * t ** 2 + bval * t)
        if(x1 < 0):
            if(y2 < 0):
                interval = np.arange(Y,1)
                print(interval)
            else:
                interval = np.arange(Y+1)
                print(interval)
        elif(y2 < 0):
            interval = np.arange(Y,1)
            print(interval)
        else:
            interval = np.arange(Y+1)
        x_values = [function_x.subs(t, value) for value in interval]
        y_values = [function_y.subs(t, value) for value in interval]
        z_values = [function_z.subs(t, value) for value in interval]
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot(x_values, y_values, z_values)
        ax.set_title('Tiro Parabólico con Funciones Vectoriales')
        ax.set_xlabel('x', labelpad=20)
        ax.set_ylabel('y', labelpad=20)
        ax.set_zlabel('z', labelpad=20)

        #para la tangente
        print("\nLa derivada de la ecuación de la parábola es: ",dy)
        print("La derivada de la ecuación de la recta es: ",dY)
        dye = dy.doit().subs({y:y1})
        dYe = dY.doit().subs({y:y1})
        vdx = dYe
        vdy = 1
        vdz = dye
        vd = [vdx,vdy,vdz]
        vy = y1
        vz = f(y1)
        v1 = [vx,vy,vz]
        print("\nCoordenadas: ",v1)
        print("Vector director: ",vd)
        function_x2 = sp.sympify(vx + vdx * t)
        function_y2 = sp.sympify(vy + vdy * t)
        function_z2 = sp.sympify(vz + vdz * t)
        interval2 = np.arange(y1+15)
        x2_values = [function_x2.subs(t, value) for value in interval2]
        y2_values = [function_y2.subs(t, value) for value in interval2]
        z2_values = [function_z2.subs(t, value) for value in interval2]
        ax.plot(x2_values, y2_values, z2_values)

        # para la longitud del arco
        dz1 = aval * 2
        dY = dY ** 2
        def f(y):
            return (1 + dY + (aval*y + bval)**2)**(1/2)
        i, err = quad(f,c,Y)
        print("\nLa longitud de arco de la parábola es: ",i)

        ax.plot(0, 0, 0, 'bo', c='black')
        ax.plot(vx, vy, vz, 'bo', c='purple')
        ax.plot(x1, Y, 0, 'bo', c='brown')
        plt.show()

    if (x == 0):
        if(y == 0):
            print("\nDebido a que el punto de impacto es el mismo del origen, nunca hubo ningún tiro\n")
        else:
            grafica_y(h, y, x)
    elif (y == 0):
        grafica_x(h, y, x)
    elif (h == 0):
        print("\nDebido a que la altura es cero, nunca hubo ningún tiro\n")
    else:
        grafica_xy(h, y, x)

    delimitador = True
    return delimitador

while(delimitador==True):
    grafica(delimitador)