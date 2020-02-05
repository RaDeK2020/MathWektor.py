# import numpy as np
# import matplotlib.plot as plt
import math

while True:
    try:

        a = float(input("Podaj wartość x wektora AB: "))
        b = float(input("Podaj wartość y wektora AB: "))

        c = float(input("Podaj wartość x wektora DC: "))
        d = float(input("Podaj wartość y wektora DC: "))

        f = int(input("Wybierz działanie: 1 - suma, 2 - różnica, 3 - iloczyn, 4 - długość wektora: "))



# punkt_zero = [0,0]

        def iloczyn():
            ktora = input("Który wektor ma być mnożony: a - AB czy b - DC ?")
            i = float(input("o ile pomnożony ma być wktor: "))
            if (ktora == "a" or ktora == "A"):
                iloczynA = i*a
                iloczynA1 = i*b
                suma_iloczynowA = [iloczynA, iloczynA1]
                print(suma_iloczynowA)
            #    plt.plot(0,0, [iloczynA, iloczynA1], color="red")
            #    plt.show()
            elif (ktora == "b" or ktora == "B"):
                iloczynB = i*c
                iloczynB1 = i*d
                suma_iloczynowB = [iloczynB, iloczynB1]
                print(suma_iloczynowB)
                plt.plot(0,0, [iloczynB, iloczynB1], color="blue")
                plt.show()

        def odlegloscWektora():
            jakiWektor = input("Dla jakiego wektora chcesz obliczyć dłuość? Wybierz: 1 - AB, 2 - DC")
            if (jakiWektor == "1"):
                odlegloscAB = math.sqrt((a*a)+(b*b))
                print("|AB| =", odlegloscAB )
                print("|AB| ≈", round(odlegloscAB))
            elif (jakiWektor == "2"):
                odlegloscDC = math.sqrt((c*c)+(d*d))
                print("|DC| =", odlegloscDC )
                print("|DC| ≈", round(odlegloscDC))

        def KierunekZwrot():
            if ((a/c) == (b/d)):
                print("Wektory mają ten sam kierunek")
                if ((a/c) >= 0 or (b/d) >= 0):
                    print("Wektory mają ten sam zwrot")
                else:
                    print("Wektory mają przeciwny zwrot")
            else:
             print("Wektory mają przeciwny kierunek")


        if(f == 1):
            suma = a+c
            suma1 = b+d
            s = [suma, suma1]
            print("Suma wektora AB i DC to: ",s)
        #    plt.plot(0,0, [suma, suma1], color="green")
        #    plt.show()
            

        elif(f == 2):
            roznica = a-c
            roznica1 = b-d
            r = [roznica, roznica1]
            print("Różnica wektora AB i DC to: ",r)
        #    plt.plot(0,0, [roznica, roznica1], color="blue")
        #    plt.show()


        elif(f == 3):
            iloczyn()

        elif(f == 4):
            odlegloscWektora()

        KierunekZwrot()

    except ValueError:
        print("Ups.. Wpisz pnownie dane w postaci liczb np.: 10, 2.8")
