"""Crear un servicio de prueba para ver si los vemos en el mail"""
from services import service01prueba

print("Soy un main")

texto = service01prueba.getSaludo()
print(texto)

