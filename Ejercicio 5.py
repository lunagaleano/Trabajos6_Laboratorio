#Ejercicio 5
'''Crea una clase base llamada Pago con un método virtual procesarPago().
Luego, crea dos clases derivadas: TarjetaCredito y PayPal, que implementen el método procesarPago() de manera diferente.
Objetivo: Simular un sistema de pagos donde se procesen diferentes tipos de pagos utilizando el polimorfismo. '''
class Pago:
    def procesarPago(self, monto):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

class TarjetaCredito(Pago):
    def __init__(self, numero_tarjeta):
        self.numero_tarjeta = numero_tarjeta
        
    def procesarPago(self, monto):
        return f"Procesando pago de ${monto:.2f} con Tarjeta de Crédito (Terminada en {self.numero_tarjeta[-4:]})... ¡Aprobado!"

class PayPal(Pago):
    def __init__(self, email):
        self.email = email
        
    def procesarPago(self, monto):
        return f"Redirigiendo a PayPal para el usuario {self.email}... Pago de ${monto:.2f} procesado con éxito."

def main():
    pagos = [
        TarjetaCredito("1234567890123456"),
        PayPal("usuario@correo.com"),
        TarjetaCredito("9876543210987654"),
        PayPal("cliente_nuevo@correo.com")
    ]
    
    monto_compra = 150.50
    
    for pago in pagos:
        print(pago.procesarPago(monto_compra))

if __name__ == "__main__":
    main()