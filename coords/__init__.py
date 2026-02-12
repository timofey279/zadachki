import requests
def __findCoodrs__(search_api_server, search_params):
    response = requests.get(search_api_server, params=search_params)
    json_response = response.json()
    organization = json_response["features"][0]

    bounds = organization["properties"]["boundedBy"]
    lower = bounds[0]
    upper = bounds[1]

    delta_lon = abs(upper[0] - lower[0])
    delta_lat = abs(upper[1] - lower[1])

    return delta_lon, delta_lat