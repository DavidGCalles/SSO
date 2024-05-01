from SqliteDB import SqliteDB

class UnsupportedDatabaseTypeError(Exception):
	"""
	Exception raised when an unsupported database type is specified.

	Attributes:
		dbType (str): The database type that triggered the exception.

	Args:
		dbType (str): The database type that is not supported.
	"""
	def __init__(self, dbType):
		self.message = f"Unsupported database type: {dbType}"
		super().__init__(self.message)

class DbManager:
	"""
    Manages database operations through a unified interface that supports multiple database types.

    Attributes:
        type (str): The type of database to manage.
        db (SqliteDB | SQLDB): The database instance.

    Args:
        dbType (str): The type of database, e.g., "SQLite" or "SQL".
        dbOptions (dict): Configuration options for the database. Typically includes paths and connection details.

    Raises:
        UnsupportedDatabaseTypeError: If the specified database type is not supported.
    """
	def __init__(self, dbType, dbOptions):
		self.type = dbType
		self.db = None
		if self.type == "SQLite":
			self.db = SqliteDB(dbOptions["dbPath"])
		elif self.type == "SQL":
			print("WIP")
			raise UnsupportedDatabaseTypeError(self.type)
		else:
			raise UnsupportedDatabaseTypeError(self.type)
	
	def createTable(self, params: dict) -> bool:
		"""
		Creates a table in the database.

		Args:
			params (dict): Parameters and specifications for the table creation.

		Returns:
			bool: True if the table was created successfully, False otherwise.
		"""
		return self.db.createTable(params)

	def deleteTable(self, tableName: str) -> bool:
		"""
		Deletes a table from the database.

		Args:
			tableName (str): The name of the table to be deleted.

		Returns:
			bool: True if the table was deleted successfully, False otherwise.
		"""
		return self.db.deleteTable(tableName)

	def updateTable(self, tableName: str, operation: str, options: dict) -> bool:
		"""
		Updates a table in the database based on the specified operation.

		Args:
			tableName (str): The name of the table to update.
			operation (str): The type of operation to perform.
			options (dict): Additional options relevant to the update operation.

		Returns:
			bool: True if the table was updated successfully, False otherwise.
		"""
		return self.db.updateTable(tableName, operation, options)

	def readTable(self, tableName: str) -> list:
		"""
		Reads data from a table.

		Args:
			tableName (str): The name of the table from which to read data.

		Returns:
			list: The data retrieved from the table.
		"""
		return self.db.readTable(tableName)

	def executeQuery(self, query: str):
		"""
		Executes a custom SQL query on the database.

		Args:
			query (str): The SQL query to execute.

		Returns:
			The result of the query execution.
		"""
		return self.db.executeQuery(query)

	def basicSelectQuery(self, tableName: str) -> list:
		"""
		Performs a basic SELECT query on the specified table.

		Args:
			tableName (str): The name of the table to query.

		Returns:
			list: The results of the query.
		"""
		return self.db.basicSelectQuery(tableName)

	def basicInsertQuery(self, params: dict) -> bool:
		"""
		Performs a basic INSERT operation into a table.

		Args:
			params (dict): The data to insert into the table.

		Returns:
			bool: True if the insert operation was successful, False otherwise.
		"""
		return self.db.basicInsertQuery(params)