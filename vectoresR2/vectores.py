import numpy as np
import matplotlib.pyplot as plt

delimitador = True

def grafica_vectores(delimitador):

        #entrada de datos de los coeficientes

    print("A continuación ingresa los valores de los coeficientes (pertenecientes a los números reales)")
    n1 = input("Valor de a: ")
    n2 = input("Valor de b: ")
    n3 = input("Valor de c: ")
    n4 = input("Valor de d: ")

    def validacion(num1, num2, num3, num4):
        try:
            float(num1)
            float(num2)
            float(num3)
            float(num4)
            return True
        except ValueError:
            return False

    if validacion(n1, n2, n3, n4):
        print("\nLos valores ingresados son:")
        print("a:" + n1 + " b:" + n2 + " c:" + n3 + " d:" + n4)
    else:
        print('Sólo se pueden insertar números reales')
        exit()

        #declaración de los principales vectores

    origin=[0,0]
    #vectores en los ejes
    v1=[0,3] #vector B
    v2=[0,-3] #vector D
    v3=[3,0] #vector A
    v4=[-3,0] #vector C

    #vectores 45 grados
    V1=[3,3]
    V2=[-3,3]
    V3=[-3,-3]
    V4=[3,-3]

    def vectores_ejes(origin, v1, v2, v3, v4, n1, n2, n3, n4):
        print('\nPara la gráfica con vectores sobre los ejes:\n')
        print('Los vectores principales son:')
        print(v3, v1, v4, v2)
        # conversión a enteros
        n1 = float(n1)
        n2 = float(n2)
        n3 = float(n3)
        n4 = float(n4)
        # vectores en los ejes
        v1x = int(v1[0])  # B
        v1y = int(v1[1])

        v2x = int(v2[0])  # D
        v2y = int(v2[1])

        v3x = int(v3[0])  # A
        v3y = int(v3[1])

        v4x = int(v4[0])  # C
        v4y = int(v4[1])

        # operaciones con punto escalar
        # vectores en los ejes
        n1x = n2 * v1x
        n1y = n2 * v1y

        n2x = n3 * v4x
        n2y = n3 * v4y

        n3x = n1 * v3x
        n3y = n1 * v3y

        n4x = n4 * v2x
        n4y = n4 * v2y

        # asignación de nuevos vectores
        # vectores en los ejes
        v5 = [n1x, n1y]  # segundo vector B
        v6 = [n2x, n2y]  # segundo vector C
        v7 = [n3x, n3y]  # segundo vector A
        v8 = [n4x, n4y]  # segundo vector D

        print("\nLos nuevos vectores obtenidos son:")
        print(v7, v5, v6, v8)

        # nuevos origenes
        # vectores en los ejes
        yB = n3y + n1y
        v5 = [n1x, yB]  # arriba nada más
        o5 = [n3x, yB]

        xC = n3x + n2x
        v6 = [n2x, n2y]  # a la izquierda nada más
        o6 = [xC, yB]

        yD = n1y + n4y
        v8 = [n4x, n4y]  # abajo nada más
        o8 = [xC, yD]

        print("\nEl vector A está representado con el color naranja\nEl vector B con el color azul\nEl vector C con el color rojo\nEl vector D con el color verde")
        print("\nEl vector resultante se representa en color morado y se ubica en las coordenadas:")
        print(o8)

        fig, ax = plt.subplots()
        ax.set_xlim(-13, 13)
        ax.set_ylim(-13, 13)
        ax.set_title('Operaciones básicas con vectores en los ejes')

        ax.quiver(origin[0], origin[1], v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='blue')  # vector B
        ax.quiver(origin[0], origin[1], v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='green')  # vector D
        ax.quiver(origin[0], origin[1], v3[0], v3[1], angles='xy', scale_units='xy', scale=1, color='orange')  # vector A
        ax.quiver(origin[0], origin[1], v4[0], v4[1], angles='xy', scale_units='xy', scale=1, color='red')  # vector C

        ax.quiver(origin[0], origin[1], v7[0], v7[1], angles='xy', scale_units='xy', scale=1, color='orange')
        ax.quiver(v7[0], v7[1], v5[0], v5[1], angles='xy', scale_units='xy', scale=1, color='blue')
        ax.quiver(o5[0], o5[1], v6[0], v6[1], angles='xy', scale_units='xy', scale=1, color='red')
        ax.quiver(o6[0], o6[1], v8[0], v8[1], angles='xy', scale_units='xy', scale=1, color='green')

        ax.quiver(origin[0], origin[1], o8[0], o8[1], angles='xy', scale_units='xy', scale=1, color='purple')  # vector resultante

        plt.axhline(0, color="black")
        plt.axvline(0, color="black")

        plt.show()

    def vectores_diagonal(origin, V1, V2, V3, V4, n1, n2, n3, n4):
        print('\nPara la gráfica con vectores con ángulos de 45°:\n')
        print('Los vectores principales son:')
        print(V1, V2, V3, V4)
        # conversión a enteros
        n1 = float(n1)
        n2 = float(n2)
        n3 = float(n3)
        n4 = float(n4)

        # vectores 45 grados
        V1x = int(V1[0])  # A
        V1y = int(V1[1])

        V2x = int(V2[0])  # B
        V2y = int(V2[1])

        V3x = int(V3[0])  # C
        V3y = int(V3[1])

        V4x = int(V4[0])  # D
        V4y = int(V4[1])

        # operaciones con punto escalar
        # vectores de 45 grados
        N1x = n1 * V1x
        N1y = n1 * V1y

        N2x = n2 * V2x
        N2y = n2 * V2y

        N3x = n3 * V3x
        N3y = n3 * V3y

        N4x = n4 * V4x
        N4y = n4 * V4y

        # asignación de nuevos vectores
        # vectores de 45 grados
        V1A = [N1x, N1y]
        V2B = [N2x, N2y]
        V3C = [N3x, N3y]
        V4D = [N4x, N4y]

        print("\nLos nuevos vectores obtenidos son:")
        print(V1A, V2B, V3C, V4D)

        # nuevos origenes
        # vectores de 45 grados
        XB = N1x + N2x
        YB = N1y + N2y
        VB = [N2x, N2y]
        OB = [XB, YB]

        XC = XB + N3x
        YC = YB + N3y
        VC = [N3x, N3y]
        OC = [XC, YC]

        VD = [N4x, N4y]

        XD = N1x + N2x + N3x + N4x
        YD = N1y + N2y + N3y + N4y
        OD = [XD, YD]

        print("\nEl vector A está representado con el color verde\nEl vector B con el color azul\nEl vector C con el color naranja\nEl vector D con el color rojo")
        print("\nEl vector resultante se representa en color morado y se ubica en las coordenadas:")
        print(OD)
        print("\n")

        fig, ax = plt.subplots()
        ax.set_xlim(-15, 15)
        ax.set_ylim(-15, 15)    
        ax.set_title('Operaciones básicas con vectores en 45°')

        ax.quiver(origin[0], origin[1], V1[0], V1[1], angles='xy', scale_units='xy', scale=1, color='green')
        ax.quiver(origin[0], origin[1], V2[0], V2[1], angles='xy', scale_units='xy', scale=1, color='blue')
        ax.quiver(origin[0], origin[1], V3[0], V3[1], angles='xy', scale_units='xy', scale=1, color='orange')
        ax.quiver(origin[0], origin[1], V4[0], V4[1], angles='xy', scale_units='xy', scale=1, color='red')

        ax.quiver(origin[0], origin[1], V1A[0], V1A[1], angles='xy', scale_units='xy', scale=1, color='green')
        ax.quiver(V1A[0], V1A[1], VB[0], VB[1], angles='xy', scale_units='xy', scale=1, color='blue')
        ax.quiver(OB[0], OB[1], VC[0], VC[1], angles='xy', scale_units='xy', scale=1, color='orange')
        ax.quiver(OC[0], OC[1], VD[0], VD[1], angles='xy', scale_units='xy', scale=1, color='red')

        ax.quiver(origin[0], origin[1], OD[0], OD[1], angles='xy', scale_units='xy', scale=1, color='purple')

        plt.axhline(0, color="black")
        plt.axvline(0, color="black")

        plt.show()

    vectores_ejes(origin, v1, v2, v3, v4, n1, n2, n3, n4)
    vectores_diagonal(origin, V1, V2, V3, V4, n1, n2, n3, n4)

    delimitador = True
    return delimitador

while(delimitador==True):
    grafica_vectores(delimitador)