from SqliteDB import SqliteDB

def test_createTable():
	dbInstance = SqliteDB("dbPrueba.db")
	newTable = {
		"tableName": "prueba",
		"fields": [
			{"fieldName": "id", "fieldType": "INTEGER", "fieldKeys": "PRIMARY KEY"},
			{"fieldName": "nombre", "fieldType": "TEXT", "fieldKeys": "NOT NULL"},
			{"fieldName": "edad", "fieldType": "INTEGER"}
		]
	}
	assert dbInstance.createTable(newTable) == True

def test_deleteTable():
	dbInstance = SqliteDB("dbPrueba.db")
	assert dbInstance.deleteTable("prueba") == True

def test_updateTable():
	dbInstance = SqliteDB("dbPrueba.db")
	tableName = "alterTable"
	dbInstance.deleteTable(tableName)
	assert dbInstance.updateTable(tableName,"add", {"column_name": 'email', 'datatype':'TEXT'}) == False
	dbInstance.createTable({"tableName":tableName, "fields":[{"fieldName": "id", "fieldType": "INTEGER", "fieldKeys": "PRIMARY KEY"}]})
	assert dbInstance.updateTable(tableName,"add", {"column_name": 'email', 'datatype':'TEXT'}) == True
	assert dbInstance.updateTable(tableName,"rename_column", {"column_name": 'email', 'new_column_name': "nuevomail"}) == True
	assert dbInstance.updateTable(tableName, "drop",{"column_name": "nuevomail"})

def test_readTable():
	dbInstance = SqliteDB("dbPrueba.db")
	headers = dbInstance.readTable("alterTable")
	assert  len(headers) > 0
	fakeHeaders = dbInstance.readTable("inexistente")
	assert len(fakeHeaders) == 0