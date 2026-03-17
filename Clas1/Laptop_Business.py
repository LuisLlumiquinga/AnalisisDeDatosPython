from laptop import Laptop
import random

class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria, espacio_disco, duracion_bateria, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.espacio_disco = espacio_disco
        self.duracion_bateria = duracion_bateria
    
    def __str__(self):
        return f"Marca: {self.marca}\nProcesador: {self.procesador}\nMemoria: {self.memoria}\nEspacio disco: {self.espacio_disco}\nCosto: {self.costo}\nImpuesto: {self.impuesto}"

    def realizar_diagnostico_sistema(self):
        resultado_diagnostico=super().realizar_diagnostico_sistema()
        resultado_red = self.verificar_conectividad_red()
       
        resultado_diagnostico["ALMACENAMIENTO"] = "OK" if self.espacio_disco >= 256 else "Almacenamiento bajo"
        resultado_diagnostico["BATERIA DURACION"] = "OK" if self.duracion_bateria >= 8 else "Bateria insuficiente para jornada laboral"
        resultado_diagnostico["CONECTIVIDAD"] = resultado_red
        
        return resultado_diagnostico

    def verificar_conectividad_red(self):
        latencia = random.randint(1, 200)
        resultado = {
            "WIFI": random.choice([True, False]),
            "SERVIDOR_EMPRESARIAL": random.choice([True, False]),
            "LATENCIA":f"{latencia}ms-"+("OK" if latencia <= 50 else "Alta latencia")
        }
        return resultado

    pass