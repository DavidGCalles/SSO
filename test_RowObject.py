from RowObject import RowObject

def test_instance_mock():
	mockData = {
		"data": ["maria", 18], 
		"headers":["name", "age"]
	}
	rowInstance = RowObject(mockData["data"], mockData["headers"])
	rowInstance.combineHeadersAndData()
	assert rowInstance.info["name"] == "maria"
	assert rowInstance.headers == ["name", "age"]