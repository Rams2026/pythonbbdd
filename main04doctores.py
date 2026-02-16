from services import service04oracledoctores as services

#Creamos nuestro servicio de Oracle
service = services.ServiceDoctores()
print("")
print("------CRUD Doctores------")
print("1.- Mostrar todos lo doctores")
print("2.- Insertar doctor")
print("3.- Modificar doctor")
print("4.- Eliminar doctor")
print("Seleccione una opción")

opcion = int(input())

if (opcion == 1):
    print("Consulta de todos los doctores")
    lista = service.getDoctores()
    for h in lista:
        print(f"Id: {h.idHospital} - doctor: {h.doctorno} - apellido: {h.apellido} - esp: {h.especialidad} - salario: {h.salario} ")
elif (opcion == 2):
    id = int(input("Id para el alta del nuevo doctor: "))
    doctor = input("Doctor No: ")
    apellido = input("Apellido: ")
    esp = input("Especialidad: ")
    sal = int(input("Salario: "))
    service.insertarDoctor(id, doctor, apellido, esp, sal)
    print("Insertado OK")
elif (opcion == 3):
    id = int(input("Doctor a modificar : "))
    docno = input("Doctor No: ")
    ape = input("Apellido: ")
    esp = input("Especialidad: ")
    sal = int(input("Salario: "))
    service.updateDoctor(id, docno, ape, esp, sal)
    print("Doctor actualizado OK")
elif (opcion == 4):
    id = int(input("Doctor a eliminar : "))
    service.deleteDoctor(id)
    print("Doctor eliminado OK")
print("Fin de programa")