# Ejercicio 1
"""Crea una clase base llamada Figura con un método virtual area().
Luego, crea dos clases derivadas: Circulo y Rectangulo, que implementen el método area() de manera diferente.
Objetivo: Demostrar cómo se puede llamar al método area() de diferentes objetos de tipo Figura. """

import math

# Clase base Figura con método area
class Figura:
    def area(self):
        # Método base que será sobrescrito
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

# Clase Circulo hereda de Figura
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        # Fórmula del área del círculo: π * r^2
        return math.pi * (self.radio ** 2)

# Clase Rectangulo hereda de Figura
class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        # Fórmula del área del rectángulo: ancho * alto
        return self.ancho * self.alto




# Función para demostrar el polimorfismo
def main():
    # Crear objetos de Circulo y Rectangulo
    figuras = [
        Circulo(5),
        Rectangulo(4, 6),
        Circulo(3),
        Rectangulo(10, 2)
    ]
    
    # Usar polimorfismo: llamar al método area sin importar el tipo específico
    for figura in figuras:
        print(f"Área de {figura.__class__.__name__}: {figura.area():.2f}")

if __name__ == "__main__":
    main()