#Tenemos la posibilidad de poner un Alias
#a esto namespace
from services import service02oracledepartamentos as serv
print("Bienvenido a mi Servicio Departamentos")
print("")
#Creamos la clase del servicio
servicio = serv.ServiceDepartamentos()
print("Insertar departamento")
numero = int(input("Id departamento: "))
nombre = input("Nombre departamento: ")
localidad = input("Localidad: ")
reg = servicio.insertarDepartamento(numero, nombre, localidad)
print(f"Insertados: {reg}")

#eliminacion
print("Dime un departamento a eliminar")
id = int(input())
reg = servicio.eliminarDepartamento(id)
print(f"Eliminados: {reg}")

#actualizacion
print("Dime un departamento a actualizar")
numero = int(input("Id departamento modificado : "))
nombre = input("Nombre departamento modificado : ")
localidad = input("Localidad modificada : ")
reg = servicio.updateDepartamento(numero, nombre, localidad)
print(f"Actualizacion: {reg}")

#Consultamos
print("Buscar un departamento")
numero = int(input("Id departamento a buscar : "))
dato = servicio.getNombreDepartamento(numero)

print(f"Nombre departamento es: {dato.nombre} ")
print(f"Nombre localidad es: {dato.localidad} ")

print("Fin de programa")




