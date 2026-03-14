from Reto6 import Auto

toyota_auto = Auto.crear_auto()
print(toyota_auto.__dict__)

auto_daniela = Auto("Mazda", "Furgon", 2020, 10000)
auto_joselyn = Auto("KIA", "Automovil", 2020, 10000)

print(Auto.mismo_km(auto_daniela, auto_joselyn))

kia_auto = Auto.crear_auto2()
print(kia_auto.__dict__)

print(Auto.mismo_año(auto_daniela, auto_joselyn))