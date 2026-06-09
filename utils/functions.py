import sys
import subprocess
from datetime import datetime

def eliminar():
    if sys.platform == "linux" or sys.platform == "darwin":
        subprocess.run(["clear"], check=False)
    else:
        subprocess.run(["cmd", "/c", "cls"], check=False)

def pausar():
    if sys.platform == "linux" or sys.platform == "darwin":
        input("Presiones cualquier tecla para continuar... ")
    else:
        subprocess.run(["cmd", "/c", "pause"])

def repeatRegister():
    opciones = ["s".lower,"n".lower]
    while True:
        seleccion = input("Seleccione s(Si) para realizar otro registro o n(No) si no desea: ").lower
        if seleccion == "s".lower and seleccion in opciones:
            return True
        elif seleccion == "n".lower and seleccion in opciones:
            return False
        else:
            print("Escogiste una opcion invalida, vuelve a intentar")
            pausar()

def validateDate(fecha):
    try:
        fecha = datetime.strptime(fecha,"%d/%m/%Y")
        return fecha
    except ValueError:
        return print("Formato incorrecto")
            