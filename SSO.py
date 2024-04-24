'''The simpliest of the simpliest ORM.
Also called SSO (Sorry Single Sign On.)'''

'''El proposito de este insanity es practicar python, buenas practicas y desestresarme.'''

import sqlite3
from typing import Any

class SqliteDB:
	"""
	Una clase simple para interactuar con una base de datos SQLite.

	Proporciona funcionalidades básicas para crear y eliminar tablas en una base de datos SQLite.

	Attributes:
		connection (sqlite3.Connection): Conexión a la base de datos SQLite.
		cursor (sqlite3.Cursor): Cursor para ejecutar consultas en la base de datos.
	"""
	def __init__(self, dbPath:str):
		"""
		Inicializa una nueva instancia de la clase SqliteDB, abriendo una conexión a la base de datos SQLite.

		Args:
			dbPath (str): Ruta al archivo de la base de datos SQLite.
		"""
		self.connection = sqlite3.connect(dbPath)
		self.cursor = self.connection.cursor()
	def createTable(self, params:dict) -> bool:
		"""
		Crea una nueva tabla en la base de datos SQLite según los parámetros especificados.

		Args:
			params (dict): Un diccionario que contiene la especificación de la tabla a crear. Debe tener
						una clave 'tableName' que indique el nombre de la tabla y una clave 'fields'
						que sea una lista de diccionarios, cada uno representando un campo de la tabla.

		Returns:
			bool: True si la tabla fue creada con éxito, False si ocurrió un error.
		
		Ejemplo de uso:
			params = {
				"tableName": "usuarios",
				"fields": [
					{"fieldName": "id", "fieldType": "INTEGER", "fieldKeys": "PRIMARY KEY"},
					{"fieldName": "nombre", "fieldType": "TEXT", "fieldKeys": "NOT NULL"},
					{"fieldName": "edad", "fieldType": "INTEGER"}
				]
			}
			db.createTable(params)
		"""
		# Comenzamos la sentencia SQL con el nombre de la tabla
		sqlStatement = f"CREATE TABLE IF NOT EXISTS {params['tableName']} ("

		if 'tableName' not in params or 'fields' not in params:
			print("Error: Missing 'tableName' or 'fields' in parameters.")
			return False
		
		# Preparamos la lista de definiciones de los campos
		field_definitions = []
		for field in params['fields']:
			# Crear la definición de cada campo, incluyendo tipo y claves adicionales si existen
			field_definition = f"{field['fieldName']} {field['fieldType']}"
			if 'fieldKeys' in field:
				field_definition += f" {field['fieldKeys']}"
			field_definitions.append(field_definition)
		
		# Unimos todas las definiciones con comas y cerramos la sentencia
		sqlStatement += ", ".join(field_definitions) + ")"
		
		# Imprimir la sentencia para verificar
		print(sqlStatement)
		try:
			self.cursor.execute(sqlStatement)
			return True
		except:
			return False
	def deleteTable(self, tableName:str)-> bool:
		"""
		Elimina una tabla específica de la base de datos si existe.

		Intenta eliminar la tabla especificada en la base de datos SQLite. Si la tabla no existe,
		la operación se ignorará sin causar un error. El método devuelve True si la operación es
		exitosa, y False si se produce una excepción durante la ejecución del comando SQL.

		Args:
			tableName (str): El nombre de la tabla a eliminar.

		Returns:
			bool: True si la tabla se eliminó con éxito, False si ocurrió un error al intentar
				eliminar la tabla.
		"""
		try:
			sqlStatement = f"DROP TABLE IF EXISTS {tableName}"
			self.cursor.execute(sqlStatement)
			return True
		except:
			return False
	def updateTable(self, tableName:str, operation:str, options:dict) -> bool:
		"""
		Modify a database table structure using a dictionary of options.

		Args:
			table_name (str): The name of the table to modify.
			operation (str): The type of operation to perform. Supported values:
								'add' - Add a new column.
								'drop' - Drop an existing column.
								'modify' - Modify the datatype of an existing column.
								'rename_column' - Rename an existing column.
								'add_constraint' - Add a new constraint.
			options (dict): A dictionary containing the parameters for the operation. Expected keys:
				'column_name' (str): The name of the column to modify (required for 'add', 'drop', 'modify', 'rename_column').
				'new_column_name' (str): The new name for the column (required for 'rename_column').
				'datatype' (str): The datatype for the column (required for 'add', 'modify').
				'constraint_name' (str): The name of the new constraint (required for 'add_constraint').
				'constraint_type' (str): The type of constraint to add (required for 'add_constraint').
				'constraint_columns' (str): The columns involved in the constraint (required for 'add_constraint').

		Example Usage:
			updateTable(conn, 'employees', 'add', {'column_name': 'email', 'datatype': 'VARCHAR(255)'})
			updateTable(conn, 'employees', 'add_constraint', {
				'constraint_name': 'unique_email',
				'constraint_type': 'UNIQUE',
				'constraint_columns': 'email'
			})
		"""
		sql = f"ALTER TABLE {tableName} "
		try:
			if operation == "add":
				sql += f"ADD {options['column_name']} {options['datatype']};"
			elif operation == "drop":
				sql += f"DROP COLUMN {options['column_name']};"
			#elif operation == "modify": MODIFY NO SE PUEDE DAR EN SQLITE3
				#sql += f"MODIFY COLUMN {options['column_name']} {options['datatype']};"
			elif operation == "rename_column":
				sql += f"RENAME COLUMN {options['column_name']} TO {options['new_column_name']};"
			#elif operation == "add_constraint":
				#sql += f"ADD CONSTRAINT {options['constraint_name']} {options['constraint_type']} ({options['constraint_columns']});"
			print(f"Alterando la estructura de la tabla con el statement: {sql}")
			self.cursor.execute(sql)
			return True
		except Exception as e:
			print(e)
			return False
	def readTable(self, tableName:str)-> list:
		"""
		Retrieves the structure of a specified table in an SQLite database.

		Args:
			tableName (str): The name of the table whose structure is to be retrieved.

		Returns:
			list of dict: A list where each dictionary contains details of a column in the table
						such as the column's name, type, and other constraints.
		"""
		try:
			self.cursor.execute(f"PRAGMA table_info({tableName});")
		except Exception as e:
			print(e)
			return []

		# Fetching all results
		columns_info = self.cursor.fetchall()

		# Prepare the structure to return
		table_structure = []
		for column in columns_info:
			# Column info is returned as (cid, name, type, notnull, dflt_value, pk)
			column_dict = {
				'name': column[1],
				'type': column[2],
				'not_null': bool(column[3]),  # Converts 0/1 to False/True
				'default_value': column[4],
				'is_primary_key': bool(column[5])  # Converts 0/1 to False/True
			}
			table_structure.append(column_dict)
		print(table_structure)
		return table_structure

