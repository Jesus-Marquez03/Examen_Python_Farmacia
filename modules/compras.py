import utils.coreFiles as core
import utils.functions as functions
from datetime import datetime

NAME_FILE = "compras.json"


def registerPurchase():

    core.checkFile(NAME_FILE, {})

    compras = core.readFile(NAME_FILE)
    medicamentos = core.readFile("medicamentos.json")
    proveedores = core.readFile("proveedores.json")

    fechaCompra = datetime.now().strftime("%d/%m/%Y")

    # ==========================
    # BUSCAR PROVEEDOR
    # ==========================

    nombreProveedor = input("Digite el nombre del proveedor: ")

    proveedorEncontrado = None

    for idProv, proveedor in proveedores.items():

        if proveedor["nombre"].lower() == nombreProveedor.lower():

            proveedorEncontrado = proveedor
            break

    if proveedorEncontrado is None:
        print("Proveedor no encontrado")
        functions.pausar()
        return

    # ==========================
    # REGISTRAR 3 MEDICAMENTOS
    # ==========================

    medicamentosComprados = []

    for i in range(3):

        print(f"\nMedicamento #{i+1}")

        nombreMedicamento = input("Nombre medicamento: ")

        encontrado = False

        for idMed, medicamento in medicamentos.items():

            if medicamento["nombre"].lower() == nombreMedicamento.lower():

                cantidad = int(input("Cantidad comprada: "))
                precioCompra = float(input("Precio de compra: "))

                medicamento["stock"] += cantidad

                compraMedicamento = {
                    "nombreMedicamento": medicamento["nombre"],
                    "cantidadComprada": cantidad,
                    "precioCompra": precioCompra
                }

                medicamentosComprados.append(compraMedicamento)

                encontrado = True
                break

        if not encontrado:

            print("Medicamento no encontrado")
            functions.pausar()
            return

    # ==========================
    # CREAR COMPRA
    # ==========================

    compra = {
        "fechaCompra": fechaCompra,
        "proveedor": {
            "nombre": proveedorEncontrado["nombre"],
            "contacto": proveedorEncontrado["contacto"]
        },
        "medicamentosComprados": medicamentosComprados
    }

    nuevoId = str(len(compras) + 1)

    compras[nuevoId] = compra

    core.createFile(NAME_FILE, compras)

    # ACTUALIZAR STOCK
    core.createFile("medicamentos.json", medicamentos)

    print("Compra registrada correctamente")
    functions.pausar()


def viewPurchases():

    core.checkFile(NAME_FILE, {})

    compras = core.readFile(NAME_FILE)

    for idCompra, compra in compras.items():

        print(f"\nCOMPRA #{idCompra}")
        print(f"Fecha: {compra['fechaCompra']}")

        print("\nProveedor:")

        for key, value in compra["proveedor"].items():
            print(f"{key}: {value}")

        print("\nMedicamentos Comprados:")

        for medicamento in compra["medicamentosComprados"]:

            print(
                f"{medicamento['nombreMedicamento']} | "
                f"Cantidad: {medicamento['cantidadComprada']} | "
                f"Precio Compra: {medicamento['precioCompra']}"
            )

    functions.pausar()