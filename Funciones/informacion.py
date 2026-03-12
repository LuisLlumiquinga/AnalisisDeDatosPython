# nombre_paciente=[]

# def agregar_nombre(nombre, apellido):
#     nombre_completo=nombre+" "+apellido
#     nombre_paciente.append(nombre_completo)

# edad=[]
# anio_actual=2026

# def agregar_edad(anio_nacimiento):
#     edad_actual=anio_actual-anio_nacimiento

nombre_paciente = []
edad = []

año_actual = 2026

def agregar_nombre(informacion):
    partes = informacion.split()
    nombre = partes[0] + " " + partes[1]
    nombre_paciente.append(nombre)

def agregar_edad(informacion):
    partes = informacion.split()
    año_nacimiento = int(partes[-1])
    edad_actual = año_actual - año_nacimiento
    edad.append(edad_actual)