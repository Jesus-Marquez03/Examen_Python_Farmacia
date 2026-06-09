import utils.coreFiles as core
import utils.functions as functions


def menuReportes():

    while True:

        functions.eliminar()

        print("""
==============================
        MENU REPORTES
==============================

1. Medicamentos con menos de 50 unidades
2. Proveedores y contactos
3. Medicamentos comprados a Proveedor A
4. Total ventas Paracetamol
5. Medicamentos que caducan antes de 2024
6. Total medicamentos vendidos por proveedor
7. Dinero total recaudado
8. Medicamentos no vendidos
9. Medicamento más caro
10. Número de medicamentos por proveedor
11. Pacientes que compraron Paracetamol
12. Proveedores sin ventas
13. Total medicamentos vendidos en marzo 2023
14. Medicamento menos vendido
15. Ganancia por proveedor
16. Promedio medicamentos por venta
17. Ventas realizadas por empleado
18. Medicamentos que expiran en 2024
19. Empleados con más de 5 ventas
20. Paciente que más gastó
21. Empleados sin ventas
22. Proveedor que más suministró
23. Pacientes que compraron Paracetamol en 2023

0. Volver
""")

        opcion = int(input("Seleccione una opción: "))

        match opcion:

            case 1:
                medicamentosMenor50()

            case 2:
                proveedoresContactos()

            case 3:
                medicamentosProveedorA()

            case 4:
                totalVentasParacetamol()

            case 5:
                medicamentosCaducan2024()

            case 6:
                totalMedicamentosVendidosProveedor()

            case 7:
                dineroTotalRecaudado()

            case 8:
                medicamentosNoVendidos()

            case 9:
                medicamentoMasCaro()

            case 10:
                numeroMedicamentosProveedor()

            case 11:
                pacientesCompraronParacetamol()

            case 12:
                proveedoresSinVentas()

            case 13:
                vendidosMarzo2023()

            case 14:
                medicamentoMenosVendido2023()

            case 15:
                gananciaProveedor()

            case 16:
                promedioMedicamentosVenta()

            case 17:
                ventasEmpleado2023()

            case 18:
                expiran2024()

            case 19:
                empleadosMas5Ventas()

            case 20:
                pacienteMasGasto()

            case 21:
                empleadosSinVentas()

            case 22:
                proveedorMasSuministro()

            case 23:
                pacientesParacetamol2023()

            case 0:
                break

            case _:
                print("Opción inválida")

        functions.pausar()

def stockBajo():

    medicamentos = core.readFile("medicamentos.json")

    print("\nMEDICAMENTOS CON STOCK MENOR A 50\n")

    for _, medicamento in medicamentos.items():

        if medicamento["stock"] < 50:

            print(
                f"{medicamento['nombre']} "
                f"-> Stock: {medicamento['stock']}"
            )

    functions.pausar()

def medicamentoMasCaro():

    medicamentos = core.readFile("medicamentos.json")

    mayor = None

    for _, medicamento in medicamentos.items():

        if mayor is None:

            mayor = medicamento

        elif medicamento["precio"] > mayor["precio"]:

            mayor = medicamento

    print("\nMEDICAMENTO MAS CARO\n")

    print(
        f"{mayor['nombre']} "
        f"${mayor['precio']}"
    )

    functions.pausar()

def medicamentosPorProveedor():

    medicamentos = core.readFile("medicamentos.json")

    conteo = {}

    for _, medicamento in medicamentos.items():

        proveedor = medicamento["proveedor"]["nombre"]

        conteo[proveedor] = conteo.get(
            proveedor,
            0
        ) + 1

    print()

    for proveedor, cantidad in conteo.items():

        print(
            f"{proveedor}: "
            f"{cantidad} medicamentos"
        )

    functions.pausar()

def dineroRecaudado():

    ventas = core.readFile("ventas.json")

    total = 0

    for _, venta in ventas.items():

        for medicamento in venta["medicamentosVendidos"]:

            total += (
                medicamento["cantidadVendida"]
                * medicamento["precio"]
            )

    print(
        f"\nDINERO RECAUDADO: ${total}"
    )

    functions.pausar()

def medicamentosNoVendidos():

    medicamentos = core.readFile(
        "medicamentos.json"
    )

    ventas = core.readFile(
        "ventas.json"
    )

    vendidos = set()

    for _, venta in ventas.items():

        for medicamento in venta[
            "medicamentosVendidos"
        ]:

            vendidos.add(
                medicamento[
                    "nombreMedicamento"
                ].lower()
            )

    print(
        "\nMEDICAMENTOS NO VENDIDOS\n"
    )

    for _, medicamento in medicamentos.items():

        if medicamento[
            "nombre"
        ].lower() not in vendidos:

            print(medicamento["nombre"])

    functions.pausar()

def empleadosMas5Ventas():

    ventas = core.readFile(
        "ventas.json"
    )

    conteo = {}

    for _, venta in ventas.items():

        empleado = venta[
            "empleado"
        ]["nombre"]

        conteo[empleado] = (
            conteo.get(
                empleado,
                0
            ) + 1
        )

    print(
        "\nEMPLEADOS CON MAS DE 5 VENTAS\n"
    )

    for empleado, cantidad in conteo.items():

        if cantidad > 5:

            print(
                f"{empleado}: "
                f"{cantidad}"
            )

    functions.pausar()

def totalMedicamentosVendidosProveedor():

    ventas = core.readFile("ventas.json")
    medicamentos = core.readFile("medicamentos.json")

    resultado = {}

    for venta in ventas.values():

        for medicamentoVendido in venta["medicamentosVendidos"]:

            nombreMedicamento = medicamentoVendido["nombreMedicamento"]
            cantidad = medicamentoVendido["cantidadVendida"]

            for medicamento in medicamentos.values():

                if medicamento["nombre"].lower() == nombreMedicamento.lower():

                    proveedor = medicamento["proveedor"]["nombre"]

                    resultado[proveedor] = resultado.get(proveedor, 0) + cantidad

    for proveedor, total in resultado.items():
        print(f"{proveedor}: {total}")

def dineroTotalRecaudado():

    ventas = core.readFile("ventas.json")

    total = 0

    for venta in ventas.values():

        for medicamento in venta["medicamentosVendidos"]:

            total += (
                medicamento["cantidadVendida"]
                * medicamento["precio"]
            )

    print(f"Total recaudado: ${total}")

def medicamentosNoVendidos():

    medicamentos = core.readFile("medicamentos.json")
    ventas = core.readFile("ventas.json")

    vendidos = []

    for venta in ventas.values():

        for medicamento in venta["medicamentosVendidos"]:

            vendidos.append(
                medicamento["nombreMedicamento"].lower()
            )

    for medicamento in medicamentos.values():

        if medicamento["nombre"].lower() not in vendidos:

            print(medicamento["nombre"])

def medicamentoMasCaro():

    medicamentos = core.readFile("medicamentos.json")

    masCaro = max(
        medicamentos.values(),
        key=lambda x: x["precio"]
    )

    print(masCaro["nombre"])
    print(masCaro["precio"])

def numeroMedicamentosProveedor():

    medicamentos = core.readFile("medicamentos.json")

    resultado = {}

    for medicamento in medicamentos.values():

        proveedor = medicamento["proveedor"]["nombre"]

        resultado[proveedor] = resultado.get(proveedor, 0) + 1

    for proveedor, cantidad in resultado.items():

        print(f"{proveedor}: {cantidad}")

def pacientesCompraronParacetamol():

    ventas = core.readFile("ventas.json")

    pacientes = set()

    for venta in ventas.values():

        for medicamento in venta["medicamentosVendidos"]:

            if medicamento["nombreMedicamento"].lower() == "paracetamol":

                pacientes.add(
                    venta["paciente"]["nombre"]
                )

    for paciente in pacientes:

        print(paciente)

def proveedoresSinVentas():

    medicamentos = core.readFile("medicamentos.json")
    ventas = core.readFile("ventas.json")

    proveedoresConVentas = set()

    for venta in ventas.values():

        for medVenta in venta["medicamentosVendidos"]:

            for medicamento in medicamentos.values():

                if medicamento["nombre"].lower() == medVenta["nombreMedicamento"].lower():

                    proveedoresConVentas.add(
                        medicamento["proveedor"]["nombre"]
                    )

    for medicamento in medicamentos.values():

        proveedor = medicamento["proveedor"]["nombre"]

        if proveedor not in proveedoresConVentas:

            print(proveedor)

from datetime import datetime

def vendidosMarzo2023():

    ventas = core.readFile("ventas.json")

    total = 0

    for venta in ventas.values():

        try:

            fecha = datetime.strptime(
                venta["fechaVenta"][:10],
                "%Y-%m-%d"
            )

        except:

            continue

        if fecha.month == 3 and fecha.year == 2023:

            for medicamento in venta["medicamentosVendidos"]:

                total += medicamento["cantidadVendida"]

    print(total)

def medicamentoMenosVendido2023():

    ventas = core.readFile("ventas.json")

    conteo = {}

    for venta in ventas.values():

        for medicamento in venta["medicamentosVendidos"]:

            nombre = medicamento["nombreMedicamento"]

            conteo[nombre] = conteo.get(nombre, 0) + medicamento["cantidadVendida"]

    menor = min(conteo, key=conteo.get)

    print(menor)

def gananciaProveedor():

    compras = core.readFile("compras.json")
    medicamentos = core.readFile("medicamentos.json")

    ganancias = {}

    for compra in compras.values():

        proveedor = compra["proveedor"]["nombre"]

        for medicamentoCompra in compra["medicamentosComprados"]:

            nombre = medicamentoCompra["nombreMedicamento"]

            for medicamento in medicamentos.values():

                if medicamento["nombre"].lower() == nombre.lower():

                    venta = medicamento["precio"]
                    compraPrecio = medicamentoCompra["precioCompra"]

                    ganancias[proveedor] = ganancias.get(
                        proveedor,
                        0
                    ) + (venta - compraPrecio)

    print(ganancias)

def promedioMedicamentosVenta():

    ventas = core.readFile("ventas.json")

    total = 0

    for venta in ventas.values():

        total += len(
            venta["medicamentosVendidos"]
        )

    promedio = total / len(ventas)

    print(promedio)

def ventasEmpleado2023():

    ventas = core.readFile("ventas.json")

    resultado = {}

    for venta in ventas.values():

        empleado = venta["empleado"]["nombre"]

        resultado[empleado] = resultado.get(
            empleado,
            0
        ) + 1

    print(resultado)

from datetime import datetime

def expiran2024():

    medicamentos = core.readFile(
        "medicamentos.json"
    )

    for medicamento in medicamentos.values():

        fecha = datetime.strptime(
            medicamento["fechaExpiracion"],
            "%d/%m/%Y"
        )

        if fecha.year == 2024:

            print(medicamento["nombre"])

def empleadosMas5Ventas():

    ventas = core.readFile("ventas.json")

    contador = {}

    for venta in ventas.values():

        empleado = venta["empleado"]["nombre"]

        contador[empleado] = contador.get(
            empleado,
            0
        ) + 1

    for empleado, cantidad in contador.items():

        if cantidad > 5:

            print(empleado)

def pacienteMasGasto():

    ventas = core.readFile("ventas.json")

    gastos = {}

    for venta in ventas.values():

        paciente = venta["paciente"]["nombre"]

        totalVenta = 0

        for medicamento in venta["medicamentosVendidos"]:

            totalVenta += (
                medicamento["cantidadVendida"]
                * medicamento["precio"]
            )

        gastos[paciente] = gastos.get(
            paciente,
            0
        ) + totalVenta

    mayor = max(gastos, key=gastos.get)

    print(mayor)

def empleadosSinVentas():

    empleados = core.readFile("empleados.json")
    ventas = core.readFile("ventas.json")

    empleadosConVentas = set()

    for venta in ventas.values():

        empleadosConVentas.add(
            venta["empleado"]["nombre"]
        )

    for empleado in empleados.values():

        if empleado["nombre"] not in empleadosConVentas:

            print(empleado["nombre"])

def proveedorMasSuministro():

    compras = core.readFile("compras.json")

    resultado = {}

    for compra in compras.values():

        proveedor = compra["proveedor"]["nombre"]

        for medicamento in compra["medicamentosComprados"]:

            resultado[proveedor] = resultado.get(
                proveedor,
                0
            ) + medicamento["cantidadComprada"]

    mayor = max(resultado, key=resultado.get)

    print(mayor)

def pacientesParacetamol2023():

    ventas = core.readFile("ventas.json")

    pacientes = set()

    for venta in ventas.values():

        if "2023" not in venta["fechaVenta"]:
            continue

        for medicamento in venta["medicamentosVendidos"]:

            if medicamento["nombreMedicamento"].lower() == "paracetamol":

                pacientes.add(
                    venta["paciente"]["nombre"]
                )

    for paciente in pacientes:

        print(paciente)
