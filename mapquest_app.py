import requests
 
# Constants for MapQuest API
BASE_URL = "https://www.mapquestapi.com/directions/v2/route"
API_KEY = "YOUR_API_KEY"  # Replace with your MapQuest API key
 
# Function to fetch directions and format the output
def get_directions(start, end):
    params = {
        "key": API_KEY,
        "from": start,
        "to": end,
    }
 
    response = requests.get(BASE_URL, params=params)
    data = response.json()
 
    # TODO: Enhancements - Format the data for user-friendly output
    # Example: Display step-by-step directions in a more readable format
 
    directions = data["route"]["legs"][0]["maneuvers"]
    for step in directions:
        print(step["narrative"])
 
    # TODO: Additional enhancements here
 
# Main function
def main():
    start_location = input("Enter the starting location: ")
    end_location = input("Enter the destination: ")
 
    get_directions(start_location, end_location)
 
if _name_ == "_main_":
    main()
