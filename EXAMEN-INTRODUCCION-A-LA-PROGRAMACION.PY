"""
Examen 1 - Cajero Automático
Por:Linderman Guerrero Ballesteros

Objetivo:
Simular un sistema de cajero automático que permita al usuario realizar operaciones básicas como:

- consultar saldo
- retirar dinero
- depositar dinero 
- Salir. 

Todo debe hacerse mediante el uso de funciones, condicionales y repetitivas.


Requisitos:
- El programa inicia con un saldo inicial de $1000.
- Mostrar un menú con las siguientes opciones:
    Consultar saldo
    Depositar dinero
    Retirar dinero
    Salir
- El menú debe repetirse hasta que el usuario seleccione "Salir" o 0 (Cero).
- Utilizar funciones separadas para cada operación (ConsultarSaldo(), Depositar(), Retirar()).

Validar lo siguiente:
- Que el monto a depositar o retirar sea mayor que cero.
- Que no se pueda retirar más dinero del disponible.
- Utilizar condicionales dentro de las funciones para realizar validaciones.
- Mostrar mensajes claros para el usuario en cada operación.

"""

def consultarsaldo(saldo):
    saldo=saldo
    print("Su saldo es ",saldo,"pesos")
    return saldo

def retirar(monto,saldo):
    monto=int(input("Ingrese el monto a retirar: "))
    if monto<=0:
        print("Monto invalido, debe ser mayor que cero ")
        input("Presione enter para continuar...")
    elif monto>saldo:
        print("Saldo insuficiente. Hay ",saldo,"pesos en la cuenta.")
        input("Presione enter para continuar ...")
    else:
        saldo=saldo-monto
        print("Retiraste ",monto,"pesos de manera exitosa")
        input("Presione enter para continuar ...")
    return saldo

def depositar(monto,saldo):
    monto=int(input("Ingrese el monto a depositar: "))
    if monto<=0:
        print("Monto invalido, debe ser mayor que cero ")
        input("Presione enter para continuar...")
    else:
        saldo=saldo+monto
        print("Depositaste ",monto,"pesos de manera exitosa")
        input("Presione enter para continuar ...")
    return saldo


saldo=1000
opcion=str("z")
monto=0



while opcion!=str("d"):
    print("""
===== CAJERO ATM =====
a.Consultar saldo
b.Depositar dinero
c.Retirar dinero
d.Salir
""")
    opcion=str(input("Seleccione una opción: "))
    match opcion:
        case str("a"):
            saldo=consultarsaldo(saldo)
            input("Presione enter para continuar...")
        case str("b"):
            saldo=depositar(monto,saldo)
        case str("c"):
            saldo=retirar(monto,saldo)
        case str("d"):
            print("Gracias por usar el cajero ATM")
        case _:
             print("Opcion invalida")
             input("Presione enter para volver al menú...")