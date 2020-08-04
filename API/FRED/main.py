import requests
import xlsxwriter as excel
import xml.etree.ElementTree as ET
import json

class Client:
	BASE_URL = "https://api.stlouisfed.org/fred/"
	DEFAULT_FORMAT = "json"
	def __init__(self, output_format=None):
		self.key = self.get_key("key.pem")
		self.format = self.DEFAULT_FORMAT if output_format is None else output_format

	def call_api(self, url, params=None):
		if params is None:
			params = {
				"api_key": self.key,
				"file_type": "json"
			}
		else:
			params["api_key"] = self.key
			params["file_type"] = self.format 
		try:
			response = requests.get(url, params=params).json()
		except ValueError:
			response = requests.get(url, params=params).content.decode('utf-8')
		except Exception as e:
			response = e
		return self.handle_response(response)

	@staticmethod
	def handle_response(response):
		# if Error, print the error
		if isinstance(response, Exception):
			print(response)
			print(response.status_code)
			return response
		# if response is not an error, it is good data
		else:
			return response

	@staticmethod
	def get_key(filename):
		with open(filename, "r") as fp:
			return fp.readline()

	def get_series_categories(self, code):
		endpoint = self.BASE_URL + "series/categories"
		params = {"series_id": code}
		return self.call_api(endpoint, params=params)

	def get_series_by_code(self, code):
		endpoint = self.BASE_URL + f"series/{code}"
		return self.call_api(endpoint)

	def get_category(self, code):
		

if __name__ == "__main__":
	FRED = Client()
	print(FRED.get_series_categories("EMRATIO"))