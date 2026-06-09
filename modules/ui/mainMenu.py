import utils.functions as functions
import modules.proveedores as prov
import modules.empleados as emp
import modules.pacientes as paci
import modules.medicamentos as medi
import modules.ventas as vent
import modules.compras as comp
import modules.informes as info
import modules.reportes as rep
from modules.stockAuditoria import auditoriaInventario





def mainMenu():
    while True:
        functions.eliminar()
        menuPrincipal = "1.Gestion de medicamentos\n2.Gestion de proveedores\n3.Gestion de empleados\n4.Gestion de pacientes\n5.Gestion de ventas\n6.Gestion de compras\n7.Informes\n8.Reportes\n9.Auditoria\n0.Salir"
        print("--------------------------------------\nBienvenido a la Farmacia EL MARQUEZ\n--------------------------------------")
        print(menuPrincipal)
        eleccion = int(input("Digite el numero de la opcion: "))
        match eleccion:
            case 1:
                functions.eliminar()
                menuMedicamentos = "1.Registrar medicamento\n2.Ver medicamentos\n0.Salir"
                print(menuMedicamentos)
                eleccion = int(input("Digite el numero de la opcion: "))
                match eleccion:
                    case 1:
                        medi.registerMedicine()
                    case 2:
                        medi.viewMedicine()
                    case 0:
                        break
                    case _:
                        print("Digitaste una opcion invalida, vuelve a digitar")
                        functions.pausar()
            case 2:
                while True:
                    functions.eliminar()
                    gestionProveedores = "1.Registrar proveedores\n2.Ver proovedores\n0.Volver"
                    print(gestionProveedores)
                    eleccion = int(input("Digite el numero de la opcion: "))
                    match eleccion:
                        case 1:
                            prov.registerProv()
                        case 2:
                            prov.viewProv()
                        case 0:
                            break
                        case _:
                            print("Digitaste una opcion invalida, vuelve a intentar")
                            functions.pausar
            case 3:
                while True:
                    functions.eliminar()
                    gestionEmpleados = "1.Registrar empleados\n2.Ver empleados\n0.Volver"
                    print(gestionEmpleados)
                    eleccion = int(input("Digite el numero de la opcion: "))
                    match eleccion:
                        case 1:
                            emp.registerEmploys()
                        case 2:
                            emp.viewEmploys()
                        case 0:
                            break
                        case _:
                            print("Digitaste una opcion invalida, vuelve a intentar")
                            functions.pausar
            case 4:
                while True:
                    functions.eliminar()
                    gestionPacientes = "1.Registrar pacientes\n2.Ver pacientes\n0.Volver"
                    print(gestionPacientes)
                    eleccion = int(input("Digite el numero de la opcion: "))
                    match eleccion:
                        case 1:
                            paci.registerPatients()
                        case 2:
                            paci.viewPatients()
                        case 0:
                            break
                        case _:
                            print("Digitaste una opcion invalida, vuelve a intentar")
                            functions.pausar
            case 5:
                functions.eliminar()
                gestionVentas = "1.Registrar venta\n2.Ver ventas\n0.Salir"
                print(gestionVentas)
                seleccion = int(input("Digite el numero de la opcion: "))
                match seleccion:
                    case 1:
                        vent.registerSale()
                    case 2:
                        vent.viewSales()
                    case 0:
                        break
                    case _:
                        print("Digistaste una opcion invalida")
                        functions.pausar()
            case 6:
                while True:

                    functions.eliminar()

                    menuCompras = (
                        "1.Registrar compra\n"
                        "2.Ver compras\n"
                    "0.Volver"
                    )

                    print(menuCompras)

                    opcion = int(input("Digite una opcion: "))

                    match opcion:

                        case 1:
                            comp.registerPurchase()

                        case 2:
                            comp.viewPurchases()

                        case 0:
                            break

                        case _:
                            print("Opcion invalida")
                            functions.pausar()
            case 7:
                while True:

                    functions.eliminar()

                    print("""
            1. Informe de ventas
            2. Informe de compras
            3. Informe de caducidad
            0. Volver
            """)

                    opcion = int(input("Digite una opcion: "))

                    match opcion:

                        case 1:
                            info.informeVentas()

                        case 2:
                            info.informeCompras()

                        case 3:
                            info.informeCaducidad()

                        case 0:
                            break

                        case _:
                            print("Opcion invalida")
                            functions.pausar()
            case 8:
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
                            rep.medicamentosMenor50()

                        case 2:
                            rep.proveedoresContactos()

                        case 3:
                            rep.medicamentosProveedorA()

                        case 4:
                            rep.totalVentasParacetamol()

                        case 5:
                            rep.medicamentosCaducan2024()

                        case 6:
                            rep.totalMedicamentosVendidosProveedor()

                        case 7:
                            rep.dineroTotalRecaudado()

                        case 8:
                            rep.medicamentosNoVendidos()

                        case 9:
                            rep.medicamentoMasCaro()

                        case 10:
                            rep.numeroMedicamentosProveedor()

                        case 11:
                            rep.pacientesCompraronParacetamol()

                        case 12:
                            rep.proveedoresSinVentas()

                        case 13:
                            rep.vendidosMarzo2023()

                        case 14:
                            rep.medicamentoMenosVendido2023()

                        case 15:
                            rep.gananciaProveedor()

                        case 16:
                            rep.promedioMedicamentosVenta()

                        case 17:
                            rep.ventasEmpleado2023()

                        case 18:
                            rep.expiran2024()

                        case 19:
                            rep.empleadosMas5Ventas()

                        case 20:
                            rep.pacienteMasGasto()

                        case 21:
                            rep.empleadosSinVentas()

                        case 22:
                            rep.proveedorMasSuministro()

                        case 23:
                            rep.pacientesParacetamol2023()

                        case 0:
                            break

                        case _:
                            print("Opción inválida")

                    functions.pausar()

            case 9:
                while True:
                    print("""
                          ===== AUDITORIA =====)
                          1. Auditoria inventario
                          2. Salir
                          """)
                    opcion = int(input("Seleccione una opcion: "))

                    match opcion:

                        case 1:
                            auditoriaInventario()

                        case 0:
                            break
                        case _:
                            print("Opcion invalida")
                            
                    functions.pausar()
                    