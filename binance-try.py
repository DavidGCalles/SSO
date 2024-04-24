from binance.spot import Spot
from datetime import datetime

class Kline:
	def __init__(self, dataArray):
		#print(f"Convirtiendo {dataArray} en Kline Instance")
		self.rawData = dataArray
		self.data = self.parseData()
	def parseData(self):
		return {
			"timestamp": datetime.fromtimestamp(self.rawData[0]/1000),
			"openPrice": self.rawData[1],
			"highPrice": self.rawData[2],
			"lowPrice": self.rawData[3],
			"closePrice": self.rawData[4]
		}

class DataMiner:
	def __init__(self, clientInstance, pair):
		self.pair = pair
		self.client = clientInstance
		#print(f"Se va a minar el par {pair}")
	def getKlines(self ):
		rawKlines = self.client.klines(self.pair, "1m", limit = 10)
		return list(map(Kline, rawKlines))
	

def main():
	client = Spot()
	miner = DataMiner(client, "BTCEUR")
	for kline in miner.getKlines():
		print(kline.data["timestamp"])

if __name__ == "__main__":
	#print(datetime.fromtimestamp(1713434280000/1000))
	
	main()