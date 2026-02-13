"""Crear un servicio de prueba para ver si los vemos en el mail"""
from services import service01prueba

print("Soy un main")

texto = service01prueba.getSaludo()
pez = service01prueba.getMascota
leona = service01prueba.getMascota2

print(texto)

print(f"{pez.nombre}, Raza: {pez.raza}")

print (leona.nombre)
