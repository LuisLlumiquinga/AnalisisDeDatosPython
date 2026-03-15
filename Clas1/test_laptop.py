from laptop import Laptop
from laptop_gaming import Laptop_Gaming
from Laptop_Business import Laptop_Business

laptop_pepito = Laptop("lenovo", "i7", 32)
laptop_maria = Laptop("lenovo", "i7", 32, 600)

# print(laptop_pepito.__dict__)
# print(f"El valor de descuento: {laptop_pepito.valor_descuento(10)}")

print(Laptop.comparar_costo(laptop_pepito, laptop_maria))

# for numero in range(1,1001):
#     asus_laptop = Laptop.asus_laptop(numero)
#     print(asus_laptop.__dict__)

laptop_juanito = Laptop_Gaming("MSI", "I7", 4, "RTX 8GB")

print(laptop_juanito.realizar_diagnostico_sistema())

laptop_empresa = Laptop_Business("Dell", "i7", 16, 512, 10)
print("\nLAPTOP EMPRESA")
print(laptop_empresa.realizar_diagnostico_sistema())