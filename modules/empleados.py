import json
import utils.functions as functions
import utils.coreFiles as core
from datetime import datetime

NAME_FILE = "empleados.json"
def registerEmploys():
    employs = {}
    while True:
        functions.eliminar()
        nombre = input("Ingresa el nombre del empleado: ")
        cargo = input("Ingresa el cargo del empleado: ")
        while True:
            fechaContratacion = input("Ingresa la fecha (dd/mm/yyyy): ")
            fechaContratacion = functions.validateDate(fechaContratacion)
            if fechaContratacion is None:
                functions.pausar()
            else:
                fechaContratacion = datetime.strftime(fechaContratacion, "%d/%m/%Y")
                print(fechaContratacion)
                employ = {
                    "nombre": nombre,
                    "cargo": cargo,
                    "fecha_contratacion": fechaContratacion
                }
                core.checkFile(NAME_FILE, {})
                fileEmp = core.readFile(NAME_FILE)
                fileEmp.update({str(len(fileEmp)+1):employ})
                employs.update(fileEmp)
                core.createFile(NAME_FILE, employs)
                break
        if functions.repeatRegister():
            functions.pausar()
        else:
            return

def viewEmploys():
    readFile = core.readFile(NAME_FILE)
    for keys, value in readFile.items():
        print(f"{keys}.")
        for key, value in value.items():
            print(f"{key}: {value}")

    functions.pausar()


                