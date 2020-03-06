import math

while True:
    try:

        a = float(input("Podaj wartość x wektora AB: "))
        b = float(input("Podaj wartość y wektora AB: "))

        c = float(input("Podaj wartość x wektora DC: "))
        d = float(input("Podaj wartość y wektora DC: "))

        f = int(input("Wybierz działanie: 1 - suma, 2 - różnica, 3 - iloczyn, 4 - długość wektora: "))



        def iloczyn():
            ktora = input("Który wektor ma być mnożony: a - AB czy b - DC ?")
            i = float(input("o ile pomnożony ma być wktor: "))
            if (ktora == "a" or ktora == "A"):
                suma_iloczynowA = [i*a, i*b]
                print(suma_iloczynowA)
            elif (ktora == "b" or ktora == "B"):
                suma_iloczynowB = [i*c, i*d]
                print(suma_iloczynowB)

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
            s = [a+c, b+d]
            print("Suma wektora AB i DC to: ",s)

        elif(f == 2):
            r = [a-c, b-d]
            print("Różnica wektora AB i DC to: ",r)

        elif(f == 3):
            iloczyn()

        elif(f == 4):
            odlegloscWektora()

        KierunekZwrot()

    except ValueError:
        print("Ups.. Wpisz pnownie dane w postaci liczb np.: 10, 2.8")
