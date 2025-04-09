class vehiculo:
    def __init__(self, marca, modelo):
        # DATOS /////////////////////////////////
        self.marca = marca
        self.modelo = modelo
        self.encendido = False # El auto comienza apagado
        self.velocidad = 0 # El auto comienza estacionado

        # COMPORTAMIENTOS //////////////////////
    # Mostrar los datos del vehiculo
    def mostrar_vehiculo(self):
        print(f"Este es un {self.marca}, modelo {self.modelo}")

    # Encender vehiculo
    def encender(self):
        self.encendido = True
        print("El vehiculo está encendido")

    # Apagar vehiculo
    def apagar(self):
        if self.velocidad > 0:
            print(f"No debería apagarse el vehiculo estando en movimiento, aunque se ha apagado de todos modos")
            self.encendido = False
        else:
            self.encendido = False
            print("El vehiculo está apagado")
    
    # Acelerar vehiculo
    def acelerar(self, incremento):
        # Si el vehiculo está encendido
        if self.encendido:
            # Incrementar la velocidad
            self.velocidad += incremento
            print(f"Vehiculo acelerado: {self.velocidad} km/h")
        # Sino, avisar que el vehiculo está apagado
        else:
            print(f"No se puede acelerar, encienda el vehiculo.")
    
    # Frenar vehiculo
    def frenar(self, decremento):
        # Si el vehiculo está encendido
        if self.encendido:
            # Si la velocidad menos, el decremento de velocidad es mayor o igual a 0
            if self.velocidad - decremento >= 0:
                # Reducir la velocidad
                self.velocidad -= decremento
                print(f"El vehiculo desaceleró a: {self.velocidad} km/h")
            # Sino, la velocidad será 0
            else:
                self.velocidad = 0
                print(f"El vehiculo se detuvo")
        # Sino, avisar que el vehiculo está apagado
        else:
            print(f"No se puede frenar, encienda el vehiculo")

# Creamos un objeto en base a la clase
vehiculo1 = vehiculo("Toyota", "Corolla")

# Utilizamos los metodos de instancia
# Mostramos los datos del vehiculo
vehiculo1.mostrar_vehiculo()

# Encendemos el vehiculo
vehiculo1.encender()

# Aceleramos 10 km/h el vehiculo
vehiculo1.acelerar(10)

# Desaceleramos 10 km/h el vehiculo
vehiculo1.frenar(10)

# Apagamos el motor
vehiculo1.apagar()