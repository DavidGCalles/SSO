from pytest import raises
from DbManager import DbManager

def test_DbManager_Instance():
	dbManagerTrue = DbManager("SQLite",{"dbPath": "dbPrueba.db"})
	print(type(dbManagerTrue))
	assert isinstance(dbManagerTrue,DbManager) == True
	with raises(Exception) as e_info: #Testeamos para la excepcion de base de datos no soportada
		DbManager("Postgre",{})