import oracledb
from models import doctores as models

class ServiceDoctores:
    def __init__(self):
        self.connection = oracledb.connect(user="system"
                                    , password="oracle"
                                    , dsn="localhost/freepdb1")
                
    #Metodo para recuperar todos los docltores
    def getDoctores(self):
        cursor = self.connection.cursor()
        sql = "select * from DOCTOR"
        cursor.execute(sql)
        listaDoctores = []
        for row in cursor:
            doctores = models.Doctores()
            doctores.idHospital = row[0]
            doctores.doctorno = row[1]
            doctores.apellido = row[2]
            doctores.especialidad = row[3]
            doctores.salario = row[4]
            listaDoctores.append(doctores)
        cursor.close()
        return listaDoctores
    
    def insertaDoctor
        cursor = self.connection.cursor()
        sql = "select max(DOCTOR_NO) + 1 as MAXIMO from DOCTOR"
        cursor.execute(sql)
        row = cursor.fethone()
        id = row[0]
        sql"insert into DOCTOR values (:hos, :id, :ape, :esp, :sal)"

        self.connection.commit()
        cursor.close()

 """  
    def insertarDoctor(self, id, docno, apell, esp, sal):
        cursor = self.connection.cursor()
        sql = "insert into DOCTOR values (:id,:docno, :apell, :esp, :sal)"
        cursor.execute
        self.connection.commit()
        cursor.close()
"""
    def updateDoctor(self, id, docno, ape, esp, sal):
        cursor = self.connection.cursor()
        sql = "update DOCTOR set HOSPITAL_COD=:id, DOCTOR_NO=:docno," \
              "APELLIDO=:ape, ESPECIALIDAD=:esp, SALARIO=:sal" \
            " where HOSPITAL_COD=:id"
        cursor.execute(sql, (docno, ape, esp, sal, id,))
        self.connection.commit()
        cursor.close()

    def deleteDoctor(self, id):
        cursor = self.connection.cursor()
        sql = "delete from DOCTOR where HOSPITAL_COD=:id"
        cursor.execute(sql, (id,))
        self.connection.commit()
        cursor.close()    


