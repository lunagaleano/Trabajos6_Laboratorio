#Ejercicio 3
'''Crea una clase base llamada Vehiculo con un método virtual mover().
Luego, crea dos clases derivadas: Coche y Bicicleta, que implementen el método mover() de manera diferente.
Objetivo: Crear una función que reciba una lista de vehículos y llame
al método mover() para cada uno, mostrando cómo se comportan de manera diferente. '''

class Vehiculo:
    def mover(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

class Coche(Vehiculo):
    def mover(self):
        return "está conduciendo por la carretera a alta velocidad."

class Bicicleta(Vehiculo):
    def mover(self):
        return "está siendo pedaleada por la ciclovía de forma ecológica."

def main():
    vehiculos = [
        Coche(),
        Bicicleta(),
        Coche(),
        Bicicleta()
    ]
    
    for vehiculo in vehiculos:
        print(f"El {vehiculo.__class__.__name__} {vehiculo.mover()}")

if __name__ == "__main__":
    main()