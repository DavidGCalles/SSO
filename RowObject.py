class RowObject:
	def __init__(self, rawData, rowHeaders):
		self.rawData = rawData
		self.headers = rowHeaders
		self.info = {}
	def combineHeadersAndData(self):
		infoDict = {}
		for ind,val in enumerate(self.headers):
			value = self.rawData[ind]
			infoDict[val] = value
		self.info = infoDict
		return infoDict