

"""
MAPQUEST Docs: https://developer.mapquest.com/documentation/open/geocoding-api/reverse/get/
OPENNOTIFY Docs: http://open-notify.org/Open-Notify-API/ISS-Location-Now/


"""
# Requests is the library we use to connect to HTTP (the internet)
import requests

OPEN_NOTIFY_URL = "http://api.open-notify.org/"
OPEN_GEOCODE_URL = "http://open.mapquestapi.com/geocoding/v1/reverse"
MAPQUEST_KEY = "k8VfHQEvKkczv77dQnMG9nJq4QJAoir5"
MAPQUEST_SECRET = "8gqkaAlfkArzB41X"

def call_api(url, params):
	# construct full URL from base and endpoint
	# url = BASE_URL + endpoint
	# API requests can return Errors, so we must handle them
	try:
		response = requests.get(url, params).json()
	# Sometimes, the repsonse is returned as bytes, not text
	except ValueError:
		response = requests.get(url, params).content.decode('utf-8')
	# Handle other errors
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

def get_status(endpoint):
	return call_api(endpoint, params=None).status_code

def get_iss_pass(lon=38.9, lat=-77.0):
	"""
	location defaults to DC
	"""
	url = OPEN_NOTIFY_URL + "iss-pass.json"
	location = {"lat": lat, "lon": lon}
	return call_api(url, params=location)

def get_iss_pos():
	"""
	return current ISS location
	"""
	url = OPEN_NOTIFY_URL + "iss-now.json"
	return call_api(url, params=None)

def get_astronauts():
	endpoint = OPEN_NOTIFY_URL + "astros.json"
	return call_api(endpoint, params=None)

def get_location(lon, lat):
	"""
	Use MapQuest's API in combination with OpenNotify
	to return a text address given a longitude and latitude
	"""
	url = OPEN_GEOCODE_URL 
	#url += f"?key={MAPQUEST_KEY}&location={lat},{lon}"
	location = str(lat) + "," + str(lon)
	params = {
		"key": MAPQUEST_KEY,
		"location": location
	}
	return call_api(url, params=params)
	#return call_api(url, params=None)

def find_location_of_iss():
	data = get_iss_pos()
	longitude = data["iss_position"]["longitude"]
	latitude = data["iss_position"]["latitude"]
	time = data["timestamp"]
	# pass location to MapQuest API
	map_data = get_location(longitude, latitude)
	# to make things simpler, zoom in
	loc_data = map_data["results"][0]["locations"][0]
	print(loc_data)
	# Fill all areas, but if they are blank, fill with NA
	street = loc_data["street"] if loc_data["street"] else "Street: NA"
	city = loc_data["adminArea5"] if loc_data["adminArea5"] else "City: NA"
	country = loc_data["adminArea1"] if loc_data["adminArea3"] else "Country: NA" 
	zipcode = loc_data["postalCode"] if loc_data["postalCode"] else "Zip: NA" 
	res = f"Time: {time}\nAddress:\n{street}\n{city}, {country} {zipcode}"
	return res
	

if __name__ == "__main__":
	#print(get_status("iss-pass.json"))
	data = find_location_of_iss()
	print(data)