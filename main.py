from fastapi import FastAPI
from SqliteDB import SqliteDB

app = FastAPI()
@app.get("/", status_code=403)
async def root():
	return {"message": "No hay nada que ver aqui"}

@app.get("/{dbName}/{tablename}")
async def readTable(dbName:str,tableName:str):
	dbInstance = SqliteDB(f"{dbName}.db")
	data = dbInstance.basicSelectQuery(tableName)
	return data