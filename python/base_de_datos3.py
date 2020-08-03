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
	def borrar(self, id):
		sql ='delete from usuarios where id={}'.format(id)
		print(sql)
		try:
			self.cursor.execute(sql)
			self.connection.commit()

		except Exception as e:
			raise


	def close(self):
		self.connection.close()
database =DataBase()
database.borrar(6)
database.close()