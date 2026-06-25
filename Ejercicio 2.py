#Ejercicio 2
'''Define una clase base llamada Animal con un método virtual hacerSonido(). Crea dos clases derivadas:
Perro y Gato, que implementen el método hacerSonido() para devolver "Guau" y "Miau", respectivamente.
Objetivo: Crear una lista de animales y hacer que cada uno emita su sonido utilizando el polimorfismo.'''

class Animal:
    def hacerSonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

class Perro(Animal):
    def hacerSonido(self):
        return "Guau"

class Gato(Animal):
    def hacerSonido(self):
        return "Miau"

def main():
    animales = [
        Perro(),
        Gato(),
        Perro(),
        Gato()
    ]
    
    for animal in animales:
        print(f"El {animal.__class__.__name__} hace: {animal.hacerSonido()}")

if __name__ == "__main__":
    main()