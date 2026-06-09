import json
import utils.coreFiles as core
import utils.functions as functions

NAME_FILE = "proveedores.json"
def registerProv():
    prov = {}
    while True:
        functions.eliminar()
        nombre = input("Ingrerse el nombre: ")
        contacto = input("Ingrese el contacto: ")
        direccion = input("Ingrese la direccion: ")
        proovedor = {
            "nombre": nombre,
            "contacto": contacto,
            "direccion": direccion
        }
        core.checkFile("proveedores.json", {})
        fileProv = core.readFile(NAME_FILE)
        fileProv.update({str(len(fileProv)+1):proovedor})
        prov["proveedores"] = fileProv
        core.createFile("proveedores.json", fileProv)
        if functions.repeatRegister():
            functions.pausar()
        else:
            break

def viewProv():
    core.checkFile("proveedores.json",{})
    listProv = core.readFile(NAME_FILE)
    for key,value in listProv.items():
        print(f"Provedor-{key}:")
        for key,value in value.items():
            print(f"{key}: {value}")
        print("\n")
    functions.pausar()


    






