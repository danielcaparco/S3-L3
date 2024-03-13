def perimetro():
        print ("Calcoliamo il perimoetro di una forma geometrica")
        print ("Quadrato > 1")
        print ("Cerchio > 2")
        print ("Rettangolo > 3")

        print ("Iserire la scelta:")
        scelta = int(input(" >> "))
        if scelta == 1:
                lato = float(input("Inserire il valore del lato del quadrato:"))
                print ("Il perimetro del quadrato con lato", lato, "e`", lato * 4)

        elif scelta == 2:
                raggio = float(input("Inserire il valore del raggio del cerchio:"))
                print ("La circonferenza del cerchioo con raggio", raggio, "e`", 2 * 3,14 * raggio)

        elif scelta == 3:
                base = float(input("Inserire il valore della base del rettangolo:"))
                altezza = float(input("Inserire il valore dell`altezza del rettangolo:"))
                print ("Il perimetro del rettangolo con base", base, "e altezza", altezza, "e`", base * 2 + altezza * 2)

        else:
                print ("Hai inserito una scelta non valida")



perimetro()

