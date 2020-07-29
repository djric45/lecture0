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
	def select_user(self, id):
		sql ='Select * from usuarios where id = {}'.format(id)
		
		print("primer usuario")
		try:
			self.cursor.execute(sql)
			user = self.cursor.fetchone() #un solo registro

			print("Id:", user[0])
			print("Nombre:", user[1])
			print("Apellido:", user[2])

		except Exception as e:
			raise

	def select_all_users(self):
		sql='Select * from usuarios'
		print ("todos los usuarios")

		try:
			self.cursor.execute(sql)

			users = self.cursor.fetchall() #mas de un solo registro

			for user in users:
				print("Id:", user[0])
				print("Nombre:", user[1])
				print("Apellido:", user[2])
				print("________\n")
		except Exception as e:
			raise

	def update_user(self, id, nombre):
		sql= "UPDATE usuarios set nombre= '{}' where id={}".format(nombre, id)
		try:
			self.cursor.execute(sql)
			self.connection.commit()
		except Exception as e:
			raise

	def close(self):
		self.connection.close()
database =DataBase()
database.select_user(1)
database.select_all_users()
database.update_user(1, 'Richard')
database.select_user(1)
database.close()