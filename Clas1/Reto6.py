class Auto:
    def __init__(self, marca, modelo, año, kilometraje=0):
        self.marca=marca
        self.modelo=modelo
        self.año=año
        self.kilometraje=kilometraje
    
    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
    
    def actualizar_kilometraje(self, nuevoKm):
        if nuevoKm<self.kilometraje:
            print("No se puede reducir el kilometraje actual")
        else:
            self.kilometraje=nuevoKm

    def realizar_viaje(self, kmRecorridos):
        if kmRecorridos<0:
            print("Los km ingresados deben ser positivos")
        else:
            self.kilometraje=self.kilometraje+kmRecorridos

    def estado_auto(self):
        print(f"\nKilometraje: {self.kilometraje}")

        if self.kilometraje<20000:
            print("Estoy como nuevo")
        elif self.kilometraje>=20000 and self.kilometraje<=100000:
            print("Ya estoy usado")
        elif self.kilometraje>100000:
            print("¡Ya déjame descansar por favor!")

auto_Daniela = Auto("Toyota", "Prius", 2026)
auto_Daniela.mostrar_informacion()
auto_Daniela.actualizar_kilometraje(-10)
auto_Daniela.realizar_viaje(-10)

auto_Daniela.estado_auto()