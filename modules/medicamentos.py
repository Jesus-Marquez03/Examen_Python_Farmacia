import json
import utils.functions as functions
import utils.coreFiles as core
from pathlib import Path
from datetime import datetime

RUTA_ARCHIVO = Path("data/")
NAME_FILE = "medicamentos.json"
def registerMedicine ():
    globalMedicines = {}
    idMedicines = {}
    medicines = {}
    while True:
        functions.eliminar()
        nombre = input("Digite el nombre del medicamento: ").lower()
        precio = float(input("Digite el precio: "))
        stock = int(input("Digite el stock: "))
        while True:
            fechaExpiracion = input("Digite la fecha de expiracion (dd/mm/aaaa): ")
            fechaExpiracion = functions.validateDate(fechaExpiracion)
            if fechaExpiracion is None:
                functions.pausar()
            else:
                break
        while True:
            proveedor_buscado = input("Digite el nombre del proveedor: ")
            encontrado = False
            with open(RUTA_ARCHIVO/"proveedores.json", "r", encoding="utf-8") as proveedores:
                SaveInfoProv = json.load(proveedores)
            for id, value in SaveInfoProv.items():
                if value["nombre"] == proveedor_buscado:
                    nombre_prov = value["nombre"] 
                    contacto_prov = value["contacto"]
                    encontrado = True
                    break
            if encontrado:
                break
            else:
                print("No se encontro el proveedor")
                functions.pausar()   
        proveedorBuscado = {
            "nombre": nombre_prov,
            "contacto": contacto_prov
        }
        medicines.update(proveedorBuscado)
        functions.pausar()
        fechaExpiracion = datetime.strftime(fechaExpiracion, "%d/%m/%Y")
        medicine = {
            "nombre": nombre,
            "precio": precio,
            "stock": stock,
            "fechaExpiracion": fechaExpiracion,
            "proveedor": medicines
        }
        core.checkFile(NAME_FILE, {})
        globalMedicines = core.readFile(NAME_FILE)
        nuevo_id = str(len(globalMedicines) + 1)
        globalMedicines[nuevo_id] = medicine
        core.createFile(NAME_FILE, globalMedicines)
        if functions.repeatRegister():
            functions.pausar()
        else:
            return
        
def viewMedicine():
    readMedicine = core.readFile(NAME_FILE)
    for id, value in readMedicine.items():
        print(f"{id}. ")
        for key, dato in value.items():
            if isinstance(dato, dict):
                print(f"{key}:")
                for subKey, subValue in dato.items():
                    print(f"{subKey}: {subValue}")
            else:
                print(f"{key}: {dato}")
    functions.pausar()