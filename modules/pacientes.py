import json
import utils.functions as functions
import utils.coreFiles as core

NAME_FILE = "pacientes.json"

def registerPatients():
    patients = {}
    while True:
        functions.eliminar()
        nombre = input("Ingrese el nombre del paciente: ")
        direccion = input("Ingrese la direccion del paciente: ")
        telefono = int(input("Ingrese el telefono del paciente: "))
        paciente = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono
        }
        core.checkFile(NAME_FILE, {})
        readFile = core.readFile(NAME_FILE)
        readFile.update({str(len(readFile)+1):paciente})
        patients.update(readFile)
        core.createFile(NAME_FILE, patients)
        if functions.repeatRegister():
            functions.pausar()
        else:
            return
        
def viewPatients():
    readFile = core.readFile(NAME_FILE)
    for key, value in readFile.items():
        print(f"{key}.")
        for key, value in value.items():
            print(f"{key}: {value}")
    functions.pausar()

