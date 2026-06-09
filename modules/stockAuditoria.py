import utils.coreFiles as core
import utils.functions as functions
from datetime import datetime

import json

def auditoriaInventario():
    core.checkFile(NAME_FILE, {})

    compras = core.readFile("compras.json")
    medicamentos = core.readFile("medicamentos.json")
    ventas = core.readFile("ventas.json")

    fechaCompra = datetime.now().strftime("%d/%m/%Y")

print("===== AUDITORIA INVENTARIO =====")
for producto, cantidad_sistema in inventario.items():
    print(f"\nProducto: {producto}")
    cantidad_fisica = int(input("Ingrese la cantidad fisica encontrada: "))

    diferencia = cantidad_fisica - cantidad_sistema

    print(f"Cantidad en sistema: {cantidad_sistema}")
    print(f"Cantidad fisica: {cantidad_fisica}")

    if diferencia > 0:
        print(f"Sobrante: {diferencia} unidades")
    elif diferencia < 0:
        print(f"Faltante: {abs(diferencia)} unidades")
    else:
        print("Inventario correcto")
print("\nAuditoria finalizada")

#Leer archivos JSON

with open("medicamentos.json", "r", encoding="utf-8") as archivo:
    medicamentos = json.load(archivo)

with open("compras.json", "r", encoding="utf-8") as archivo:
    compras = json.load(archivo)

with open("ventas.json", "r", encoding="utf-8") as archivo:
    ventas = json.load(archivo)

reporte_auditoria = []

for medicamento in medicamentos:
    nombre = medicamento["nombre"]
    stock_registrado = medicamento["stock"]

    #CALCULAR TOTAL COMPRADO
    total_comprado = sum(
        compra["cantidad"]
        for compra in compras
        if compra["medicamento"] == nombre
    )

    #CALCULAR TOTAL VENDIDO
    total_vendido = sum(
        venta["cantidad"]
        for venta in ventas
        if venta["medicamento"] == nombre
    )

    #STOCK TEORICO
    stock_teorico = total_comprado - total_vendido

    #DIFERENCIA
    diferencia = stock_teorico - stock_registrado

    reporte_auditoria.append({
        "nombre": nombre,
        "stock_registrado": stock_registrado,
        "stock_teorico": stock_teorico,
        "diferencia": diferencia
    })

#GUARDAR REPORTE
with open("reporte_auditoria_inventario.json", "w", encoding="utf-8") as archivo:
    json.dump(reporte_auditoria, archivo, indent=4, ensure_ascii=False)
print("Reporte de auditoria generado correctamente")
