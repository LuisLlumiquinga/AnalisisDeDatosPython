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
    
    @classmethod
    def crear_auto(cls):
        marca = "Toyota"
        año = 2026
        modelo = "Camioneta"
        return cls(marca, año, modelo)
    
    @staticmethod
    def mismo_km(auto1, auto2):
        if auto1.kilometraje == auto2.kilometraje:
            return "Tienen el mismo kilometraje"
        return "Tienen diferente kilometraje"

    @classmethod
    def crear_auto2(cls):
        marca = "KIA"
        año = 2020
        modelo = "Furgon"
        return cls(marca, año, modelo)
    
    @staticmethod
    def mismo_año(auto1, auto2):
        if auto1.año == auto2.año:
            return "Tienen el mismo año de fabricacion"
        return "Tienen diferente año de fabricacion"

# auto_Daniela = Auto("Toyota", "Prius", 2026)
# auto_Daniela.mostrar_informacion()
# auto_Daniela.actualizar_kilometraje(-10)
# auto_Daniela.realizar_viaje(-10)

# auto_Daniela.estado_auto()