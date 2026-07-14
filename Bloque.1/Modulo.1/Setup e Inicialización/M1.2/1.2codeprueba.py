# ============================================
# 1.2codeprueba.py — Código para PRÁCTICA
# El equipo debe crear su propio agente y
# ejecutarlo sobre este archivo para generar
# un reporte de calidad de código.
# ============================================

import datetime
import math
import re
import subprocess  # No se usa

# Constantes mal definidas
MAX = 100
min = 0  # Problema: no sigue UPPER_CASE para constantes

def get_data(url, timeout, retries, verbose, format):
    """Descarga datos de una URL."""
    # Problema: 'format' es built-in de Python
    # Problema: sin manejo de excepciones de red
    # Problema: sin type hints
    # Problema: demasiados parámetros
    import requests  # Problema: import dentro de función
    response = requests.get(url, timeout=timeout)
    data = response.json()
    return data


def validate(x):
    """Valida entrada."""
    # Problema: nombre no descriptivo
    # Problema: docstring inútil
    # Problema: múltiples returns sin claridad
    if x == None:  # Problema: debería usar 'is None'
        return False
    if type(x) == str:  # Problema: debería usar isinstance()
        if len(x) > 0:
            return True
        else:
            return False
    if type(x) == int:
        if x > 0:
            return True
    return False


class order_processor:
    # Problema: nombre no sigue PascalCase
    # Problema: clase con responsabilidades mezcladas

    def __init__(self):
        self.orders = []
        self.processed = []
        self.failed = []
        self.log = []

    def add_order(self, id, product, qty, price, customer, address, phone):
        # Problema: demasiados parámetros
        # Problema: 'id' es built-in de Python
        # Problema: sin validaciones
        order = {
            "id": id,
            "product": product,
            "qty": qty,
            "price": price,
            "customer": customer,
            "address": address,
            "phone": phone,
            "date": str(datetime.datetime.now()),
            "status": "pending"
        }
        self.orders.append(order)

    def process_order(self, order_id):
        # Problema: lógica repetida del bucle de búsqueda
        # Problema: sin manejo de orden no encontrada
        for order in self.orders:
            if order["id"] == order_id:
                order["status"] = "processed"
                self.processed.append(order)
                self.log.append("Processed: " + str(order_id))

    def cancel_order(self, order_id):
        # Problema: misma lógica de búsqueda duplicada
        for order in self.orders:
            if order["id"] == order_id:
                order["status"] = "cancelled"
                self.failed.append(order)
                self.log.append("Cancelled: " + str(order_id))

    def get_total(self):
        # Problema: no maneja qty o price None/inválidos
        total = 0
        for order in self.processed:
            total = total + (order["qty"] * order["price"])
        return total

    def export_report(self, filename):
        # Problema: no usa 'with' para manejo de archivo
        # Problema: no maneja errores de escritura
        f = open(filename, "w")
        for order in self.orders:
            f.write(str(order) + "\n")
        f.close()


def calculate_discount(price, customer_type, is_holiday, coupon_code, loyalty_points):
    """Calcula descuento."""
    # Problema: demasiada complejidad ciclomática
    # Problema: números mágicos
    discount = 0
    if customer_type == "vip":
        discount = discount + 20
    if customer_type == "regular":
        discount = discount + 5
    if is_holiday == True:  # Problema: comparación innecesaria con True
        discount = discount + 10
    if coupon_code == "SAVE50":
        discount = discount + 50
    if coupon_code == "SAVE20":
        discount = discount + 20
    if loyalty_points > 1000:
        discount = discount + 15
    if discount > 70:
        discount = 70
    final_price = price - (price * discount / 100)
    return final_price


# Código suelto sin __main__
print("Iniciando procesador de órdenes...")
proc = order_processor()
proc.add_order(1, "Laptop", 2, 999.99, "Carlos", "Calle 123", "555-0001")
proc.add_order(2, "Mouse", 5, 29.99, "Ana", "Av. Principal 456", "555-0002")
proc.process_order(1)
print(f"Total procesado: ${proc.get_total()}")
