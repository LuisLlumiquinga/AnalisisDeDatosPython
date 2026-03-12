datos = []

cantidad = int(input("¿Cuántos datos desea ingresar? "))

for i in range(cantidad):
    valor = input(f"Ingrese el dato {i + 1}: ")

    if valor.strip('-').isnumeric():
        datos.append(int(valor))

    elif valor.replace('.', '', 1).lstrip('-').isnumeric():
        datos.append(float(valor))

    else:
        datos.append(valor)

print(f"Su lista es: {datos}")