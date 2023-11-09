import requests
from math import radians, sin, cos, sqrt, atan2

# Constants for MapQuest API
BASE_URL = "https://www.mapquestapi.com/directions/v2/route"
API_KEY = "zVYkcjdkV1Pykfr32gAyOsj3FsMujdUe"  # Replace with your MapQuest API key

# Function to fetch directions and format the output
def get_directions(start, end):
    params = {
        "key": API_KEY,
        "from": start,
        "to": end,
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    # Check if the request was successful
    if response.status_code != 200 or data["info"]["statuscode"] != 0:
        print("Error fetching directions. Please check your input.")
        return

    # Extract and display step-by-step directions
    directions = data["route"]["legs"][0]["maneuvers"]
    for idx, step in enumerate(directions, start=1):
        print(f"Step {idx}: {step['narrative']}")

    # Calculate distance using the Haversine formula
    start_coordinates = data["route"]["locations"][0]["displayLatLng"]
    end_coordinates = data["route"]["locations"][-1]["displayLatLng"]
    distance_km = haversine_distance(
        start_coordinates["lat"], start_coordinates["lng"],
        end_coordinates["lat"], end_coordinates["lng"]
    )

    print(f"\nThe straight-line distance between {start} and {end} is {distance_km:.2f} kilometers.")

    # TODO: Additional enhancements here

# Haversine formula function
def haversine_distance(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Calculate the distance
    distance = R * c

    return distance

# Main function
def main():
    start_location = input("Enter the starting location: ")
    end_location = input("Enter the destination: ")

    get_directions(start_location, end_location)

if __name__ == "__main__":
    main()