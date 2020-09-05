import requests
BASE_URL = "http://api.open-notify.org/"

def call_api(url):
	try:
		response = requests.get(url).json()
	except ValueError:
		response = requests.get(url).content.decode('utf-8')
	except Exception as e:
		response = e
	return handle_response(response)

def handle_response(response):
	# if Error, print the error
	if isinstance(response, Exception):
		print(response)
		return response
	# if response is not an error, it is good data
	else:
		return response

def get_astronauts():
	endpoint = BASE_URL + "astros.json"
	return call_api(endpoint)

if __name__ == "__main__":	
	pass
	
	