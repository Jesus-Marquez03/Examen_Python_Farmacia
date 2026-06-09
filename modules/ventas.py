import utils.coreFiles as core
import utils.functions as functions
from datetime import datetime

NAME_FILE = "ventas.json"


def registerSale():

    core.checkFile(NAME_FILE, {})

    ventas = core.readFile(NAME_FILE)
    medicamentos = core.readFile("medicamentos.json")
    pacientes = core.readFile("pacientes.json")
    empleados = core.readFile("empleados.json")

    fechaVenta = datetime.now().strftime("%d/%m/%Y")

    # ==========================
    # BUSCAR PACIENTE
    # ==========================

    nombrePaciente = input("Digite el nombre del paciente: ")

    pacienteEncontrado = None

    for id, paciente in pacientes.items():
        if paciente["nombre"].lower() == nombrePaciente.lower():
            pacienteEncontrado = paciente
            break

    if pacienteEncontrado is None:
        print("Paciente no encontrado")
        functions.pausar()
        return

    # ==========================
    # BUSCAR EMPLEADO
    # ==========================

    nombreEmpleado = input("Digite el nombre del empleado: ")

    empleadoEncontrado = None

    for id, empleado in empleados.items():
        if empleado["nombre"].lower() == nombreEmpleado.lower():
            empleadoEncontrado = empleado
            break

    if empleadoEncontrado is None:
        print("Empleado no encontrado")
        functions.pausar()
        return

    # ==========================
    # REGISTRAR 3 MEDICAMENTOS
    # ==========================

    medicamentosVendidos = []

    for i in range(3):

        print(f"\nMedicamento #{i+1}")

        nombreMedicamento = input("Nombre medicamento: ")

        encontrado = False

        for idMed, medicamento in medicamentos.items():

            if medicamento["nombre"].lower() == nombreMedicamento.lower():

                cantidad = int(input("Cantidad vendida: "))

                if cantidad > medicamento["stock"]:
                    print("Stock insuficiente")
                    functions.pausar()
                    return

                medicamento["stock"] -= cantidad

                ventaMedicamento = {
                    "nombreMedicamento": medicamento["nombre"],
                    "cantidadVendida": cantidad,
                    "precio": medicamento["precio"]
                }

                medicamentosVendidos.append(ventaMedicamento)

                encontrado = True
                break

        if not encontrado:
            print("Medicamento no encontrado")
            functions.pausar()
            return

    # ==========================
    # CREAR VENTA
    # ==========================

    venta = {
        "fechaVenta": fechaVenta,
        "paciente": {
            "nombre": pacienteEncontrado["nombre"],
            "direccion": pacienteEncontrado["direccion"]
        },
        "empleado": {
            "nombre": empleadoEncontrado["nombre"],
            "cargo": empleadoEncontrado["cargo"]
        },
        "medicamentosVendidos": medicamentosVendidos
    }

    nuevoId = str(len(ventas) + 1)

    ventas[nuevoId] = venta

    core.createFile(NAME_FILE, ventas)

    # ACTUALIZAR STOCK
    core.createFile("medicamentos.json", medicamentos)

    print("Venta registrada correctamente")
    functions.pausar()


def viewSales():

    core.checkFile(NAME_FILE, {})

    ventas = core.readFile(NAME_FILE)

    for idVenta, venta in ventas.items():

        print(f"\nVENTA #{idVenta}")
        print(f"Fecha: {venta['fechaVenta']}")

        print("\nPaciente:")
        for key, value in venta["paciente"].items():
            print(f"{key}: {value}")

        print("\nEmpleado:")
        for key, value in venta["empleado"].items():
            print(f"{key}: {value}")

        print("\nMedicamentos:")

        for medicamento in venta["medicamentosVendidos"]:

            print(
                f"{medicamento['nombreMedicamento']} | "
                f"Cantidad: {medicamento['cantidadVendida']} | "
                f"Precio: {medicamento['precio']}"
            )

    functions.pausar()

