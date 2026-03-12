destino=input("Ingrese el destino: ")
zona=input("Ingrese la zona: ")
velocidad=int(input("Ingrese la velocidad: "))

if destino=="Ecuador":
    if zona=="Urbana":
        if velocidad<10:
            print("Velocidad inferior a la permitida")
        elif velocidad>50:
            print("Velocidad superior a la permitida")
        else:
            print("Velocidad adecuada")
    elif zona=="Rural":
        if velocidad<51:
            print("Velocidad inferior a la permitida")
        elif velocidad>70:
            print("Velocidad superior a la permitida")
        else:
            print("Velocidad adecuada")
    if zona=="Perimetral":
        if velocidad<71:
            print("Velocidad inferior a la permitida")
        elif velocidad>90:
            print("Velocidad superior a la permitida")
        else:
            print("Velocidad adecuada")

if destino=="Colombia":
    if zona=="Urbana":
        if velocidad<10:
            print("Velocidad inferior a la permitida")
        elif velocidad>30:
            print("Velocidad superior a la permitida")
        else:
            print("Velocidad adecuada")
    elif zona=="Rural":
        if velocidad<31:
            print("Velocidad inferior a la permitida")
        elif velocidad>80:
            print("Velocidad superior a la permitida")
        else:
            print("Velocidad adecuada")
    if zona=="Perimetral":
        if velocidad<81:
            print("Velocidad inferior a la permitida")
        elif velocidad>100:
            print("Velocidad superior a la permitida")
        else:
            print("Velocidad adecuada")

if destino=="Peru":
    if zona=="Urbana":
        if velocidad<10:
            print("Velocidad inferior a la permitida")
        elif velocidad>40:
            print("Velocidad superior a la permitida")
        else:
            print("Velocidad adecuada")
    elif zona=="Rural":
        if velocidad<41:
            print("Velocidad inferior a la permitida")
        elif velocidad>60:
            print("Velocidad superior a la permitida")
        else:
            print("Velocidad adecuada")
    if zona=="Perimetral":
        if velocidad<61:
            print("Velocidad inferior a la permitida")
        elif velocidad>120:
            print("Velocidad superior a la permitida")
        else:
            print("Velocidad adecuada")