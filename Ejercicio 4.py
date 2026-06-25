#Ejercicio 4
'''Define una clase base llamada Empleado con un método virtual calcularSalario().
Crea dos clases derivadas: EmpleadoPorHora y EmpleadoFijo, que implementen el método calcularSalario() de manera diferente.
Objetivo: Crear una lista de empleados y calcular el salario total utilizando el polimorfismo.'''
class Empleado:
    def calcularSalario(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

class EmpleadoPorHora(Empleado):
    def __init__(self, horas_trabajadas, tarifa_hora):
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora
        
    def calcularSalario(self):
        return self.horas_trabajadas * self.tarifa_hora

class EmpleadoFijo(Empleado):
    def __init__(self, salario_mensual):
        self.salario_mensual = salario_mensual
        
    def calcularSalario(self):
        return self.salario_mensual

def main():
    empleados = [
        EmpleadoPorHora(40, 15),
        EmpleadoFijo(2500),
        EmpleadoPorHora(20, 18),
        EmpleadoFijo(3200)
    ]
    
    salario_total = 0
    
    for empleado in empleados:
        salario_actual = empleado.calcularSalario()
        print(f"Salario de {empleado.__class__.__name__}: ${salario_actual:.2f}")
        salario_total += salario_actual
        
    print("-" * 40)
    print(f"Salario total de la nómina: ${salario_total:.2f}")

if __name__ == "__main__":
    main()
