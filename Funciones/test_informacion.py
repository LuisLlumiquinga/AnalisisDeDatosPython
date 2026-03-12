from informacion import agregar_nombre, agregar_edad, nombre_paciente, edad

cantidad = int(input("¿Cuántos pacientes desea ingresar? "))

for i in range(cantidad):
    informacion = input(f"Ingrese nombre, apellido y año de nacimiento del paciente {i + 1}: ")
    agregar_nombre(informacion)
    agregar_edad(informacion)

print("Lista de nombres:")
print(nombre_paciente)

print("\nLista de edades:")
print(edad)

edad_mayor = max(edad)
edad_menor = min(edad)

indice_mayor = edad.index(edad_mayor)
indice_menor = edad.index(edad_menor)

print(f"\n{nombre_paciente[indice_mayor]} con la edad de {edad_mayor} años es mayor a los demás pacientes.")
print(f"{nombre_paciente[indice_menor]} con la edad de {edad_menor} años es menor a los demás pacientes.")