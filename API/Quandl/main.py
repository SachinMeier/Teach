import requests as r
import xlsxwriter as excel
from datetime import datetime


"""
GET https://www.quandl.com/api/v3/datasets/{database_code}/{dataset_code}/data.{return_format}
return 
{
  "dataset_data":{
     "limit":null,
     "transform":null,
     "column_index":null,
     "column_names":[
        "Date",
        "Open",
        "High",
        "Low"
     ],
     "start_date":"2015-05-24",
     "end_date":"2015-05-28",
     "frequency":"daily",
     "data":[
        [
           "2015-05-28",
           9.58,
           10.17,
           12.96
        ],
        [
           "2015-05-27",
           9.53,
           10.13,
           12.97
        ],
        [
           "2015-05-26",
           9.53,
           10.11,
           12.98
        ]
     ],
     "collapse":null,
     "order":"desc"
  }
}
"""



class Quandl:
	BASE_URL = "https://www.quandl.com/api/v3/datasets"
	DEFAULT_FORMAT = "json" # XML 
	def __init__(self, output_format=None):
		self.key = self.get_key("key.pem")
		self.format = output_format if output_format is not None else self.DEFAULT_FORMAT

	def call_api(self, url, params=None):
		if params is None:
			params = {
				"api_key": self.key
			}
		else:
			params["api_key"] = self.key
		try:
			response = r.get(url, params=params).json()
		except ValueError:
			response = r.get(url, params=params).content.decode('utf-8')
		except Exception as e:
			response = e
		return self.handle_response(response)

	@staticmethod
	def handle_response(response):
		# if Error, print the error
		if isinstance(response, Exception):
			print(response)
			return response
		# if response is not an error, it is good data
		else:
			return response


	def search(self, query):
		endpoint = BASE_URL + DEFAULT_FORMAT
		params = {
			"query": query.replace(" ", "+")
		}
		return self.call_api(endpoint, params=params)

	def get_timeseries(self, database_code, dataset_code, params=None, return_format=DEFAULT_FORMAT):
		endpoint = self.BASE_URL
		endpoint += f"/{database_code}/{dataset_code}/data.{return_format}"
		return self.call_api(endpoint, params=params)
<<<<<<< HEAD
	
	def avg_price(self, data):
		aSum = 0
		count = 0
		for obj in data["dataset_data"]["data"]:
			aSum += obj[1]
			count += 1
		return aSum/count

	def avg_change(self, data):
		aSum = 0
		count = len(data["dataset_data"]["data"])-1
		for idx in range(count):
			d = data["dataset_data"]["data"][idx+1][1] - data["dataset_data"]["data"][idx][1]
			aSum += d
		return aSum/count
		# for idx, obj in enumerate(data["dataset_data"]["data"]): # 	obj[1]
		# 	data["dataset_data"]["data"][idx+1][1]

	def get_volatility(self, data):
		''' data is result of get_timeseries '''
		change = self.avg_change(data)
		price = self.avg_price(data)
		return change / price

=======
>>>>>>> a4f35b8092968a42e5b3b51268ef2de01afe69a6

	def write_to_sheet(self, database_code, dataset_code, sheet, row, col, params=None):
		data = Q.get_timeseries(database_code, dataset_code, return_format=self.DEFAULT_FORMAT, params=params)
		sheet.write(row,col,f"{database_code}/{dataset_code}")
		row += 1
		sheet.write(row, col, "Date")
		sheet.write(row, col+1, "Price")
		row += 1
		for d, p in data["dataset_data"]["data"]:
			sheet.write(row, col, d)
			sheet.write(row,col+1, p)
			row += 1
		return row

if __name__ == "__main__":
	'''
	Facebook weekly close prices from 2016-2018
	date   price

	chart. 
	'''
	Q = Quandl()
	p = {
		"column_index": 4,
		"collapse": "weekly",
		"start_date": "2014-01-01",
		"end_date": "2015-01-01"
	}
<<<<<<< HEAD
	gold = Q.get_timeseries("LBMA", "GOLD", params=p)
	silv = Q.get_timeseries("LBMA", "SILVER", params=p)
	#print(data["dataset_data"]["data"][0][1])
	
	print(Q.get_volatility(gold))
	print(Q.get_volatility(silv))
=======
	#data = Q.get_timeseries("FRBP", "GDPPLUS", params=None)
	#print(data["dataset_data"]["data"])
	dt = datetime.strptime('1998-09-30', "%Y-%m-%d")
	print(dt.timestamp())
>>>>>>> a4f35b8092968a42e5b3b51268ef2de01afe69a6










	# params = {
	# 	"start_date": "2015-01-01",
	# 	"end_date": "2016-01-01",
	# 	"column_index": 4,
	# 	"collapse": "weekly"
	# }
	# #print(Q.get_timeseries("FRED", "EMRATIO"))
	# workbook = excel.Workbook("APIData.xlsx")
	# stocks = workbook.add_worksheet()
	# r = 0
	# c = 0
	# Q.write_to_sheet("WIKI", "FB", stocks, r, c, params=params)
	# c += 2
	# Q.write_to_sheet("WIKI", "TSLA", stocks, r, c, params=params)
	# c += 2
	# Q.write_to_sheet("BITSTAMP", "USD", stocks, r, c, params=params)
	# c += 2
	# fred = workbook.add_worksheet()
	# Q.write_to_sheet("FRED", "EMRATIO", fred, r, c)
	# workbook.close()
	
