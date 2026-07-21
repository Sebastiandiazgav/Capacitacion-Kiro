# ============================================
# 1.2code.py — Código de DEMOSTRACIÓN
# Este archivo será analizado por un agente
# custom de Kiro que generará un reporte
# de calidad de código.
# ============================================

import os
import sys
import json
import random  # No se usa en ninguna parte

# Variable global sin documentación
data = []

def get_users(db_connection, type, limit):
    """Obtiene usuarios de la base de datos."""
    # Problema: parámetro 'type' es palabra reservada de Python
    # Problema: sin validación de inputs
    # Problema: SQL inyectable
    query = "SELECT * FROM users WHERE type = '" + type + "' LIMIT " + str(limit)
    result = db_connection.execute(query)
    users = []
    for row in result:
        users.append(row)
    return users


def process(d):
    """Procesa datos."""
    # Problema: nombre de función y parámetro no descriptivos
    # Problema: no hay manejo de errores
    # Problema: lógica duplicada
    output = []
    for item in d:
        if item["status"] == "active":
            output.append({"name": item["name"], "email": item["email"], "active": True})
        if item["status"] == "active":
            print("User " + item["name"] + " is active")
    return output


def calc(a, b, c):
    # Problema: sin docstring
    # Problema: nombres de variables no descriptivos
    # Problema: division por cero no manejada
    result = (a + b) / c
    temp = result * 2
    final = temp - 1
    return final


class userManager:
    # Problema: nombre de clase no sigue PascalCase
    # Problema: sin __init__ documentado

    def __init__(self):
        self.users = []
        self.active = []
        self.deleted = []

    def add(self, name, email, age, role, department):
        # Problema: demasiados parámetros, debería usar un objeto
        # Problema: sin validación
        user = {
            "name": name,
            "email": email,
            "age": age,
            "role": role,
            "department": department,
            "status": "active"
        }
        self.users.append(user)
        return True

    def delete_user(self, email):
        # Problema: inconsistencia en naming (add vs delete_user)
        # Problema: no retorna si el usuario no existe
        for user in self.users:
            if user["email"] == email:
                self.users.remove(user)
                self.deleted.append(user)

    def get_all(self):
        # Problema: expone referencia interna mutable
        return self.users


def send_notification(user_email, subject, body, cc=None, bcc=None, priority="normal"):
    """Envía notificación por email."""
    # Problema: función que no hace nada real (placeholder sin implementar)
    # Problema: no levanta NotImplementedError
    pass


# Código suelto al final del archivo sin protección __main__
print("Cargando módulo de gestión de usuarios...")
manager = userManager()
manager.add("Juan", "juan@test.com", 25, "dev", "engineering")
manager.add("María", "maria@test.com", 30, "lead", "engineering")
result = manager.get_all()
print(f"Usuarios cargados: {len(result)}")
