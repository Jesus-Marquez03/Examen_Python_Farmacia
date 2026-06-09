import utils.coreFiles as core
import utils.functions as functions
from datetime import datetime

def informeVentas():

    ventas = core.readFile("ventas.json")

    if not ventas:
        print("No hay ventas registradas")
        functions.pausar()
        return

    totalIngresos = 0

    for idVenta, venta in ventas.items():

        print(f"\nVENTA #{idVenta}")
        print(f"Fecha: {venta['fechaVenta']}")

        print(f"Paciente: {venta['paciente']['nombre']}")
        print(f"Empleado: {venta['empleado']['nombre']}")

        for medicamento in venta["medicamentosVendidos"]:

            subtotal = (
                medicamento["cantidadVendida"]
                * medicamento["precio"]
            )

            totalIngresos += subtotal

            print(
                f"{medicamento['nombreMedicamento']} "
                f"x {medicamento['cantidadVendida']} "
                f"= ${subtotal}"
            )

    print(f"\nTOTAL INGRESOS: ${totalIngresos}")

    functions.pausar()

def informeCompras():

    compras = core.readFile("compras.json")

    if not compras:

        print("No hay compras registradas")
        functions.pausar()
        return

    for idCompra, compra in compras.items():

        print(f"\nCOMPRA #{idCompra}")
        print(f"Fecha: {compra['fechaCompra']}")

        print(
            f"Proveedor: "
            f"{compra['proveedor']['nombre']}"
        )

        for medicamento in compra["medicamentosComprados"]:

            print(
                f"{medicamento['nombreMedicamento']} - "
                f"{medicamento['cantidadComprada']}"
            )

    functions.pausar()

def informeCaducidad():

    medicamentos = core.readFile("medicamentos.json")

    fechaActual = datetime.now()

    for _, medicamento in medicamentos.items():

        fechaExp = datetime.strptime(
            medicamento["fechaExpiracion"],
            "%d/%m/%Y"
        )

        dias = (fechaExp - fechaActual).days

        if dias <= 180:

            print(
                f"{medicamento['nombre']} "
                f"vence el "
                f"{medicamento['fechaExpiracion']}"
            )

    functions.pausar()