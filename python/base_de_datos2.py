import pymysql

class DataBase:
	def __init__(self):
		self.connection = pymysql.connect(
			host='localhost',
			user ='rich',
			password='root',
			db='neoguias'
		)

		self.cursor = self.connection.cursor()
		print ("Conexion exitosa")
	def insertar(self, id, nombre, apellido):
		sql ='insert into usuarios(id, nombre, apellido) values ({},"{}","{}")'.format(id,nombre,apellido)
		print("agregado a la base")
		print(sql)
		try:
			self.cursor.execute(sql)
			self.connection.commit()

			#datos=(4,"Laura","Hernandez")
			#self.cursor.execute(sql,datos)

		except Exception as e:
			raise


	def close(self):
		self.connection.close()
database =DataBase()
database.insertar(6,"Maria","Megia")
database.close()