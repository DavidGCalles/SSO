class RowObject:
	def __init__(self, rawData:list, rowHeaders:list):
		self.rawData = rawData
		self.headers = rowHeaders
		self.info = {}
	def combineHeadersAndData(self) -> dict:
		infoDict = {}
		for ind,val in enumerate(self.headers):
			value = self.rawData[ind]
			infoDict[val] = value
		self.info = infoDict
		return infoDict