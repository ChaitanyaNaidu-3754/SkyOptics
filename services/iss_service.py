import requests
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

class ISSService:
    def __init__(self):
        self.api_url = "http://api.open-notify.org/iss-now.json"
        # Initialize geolocator with a unique user_agent
        self.geolocator = Nominatim(user_agent="cosmos_ai_app")

    def get_iss_location(self):
        """
        Fetch live ISS location.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            data = response.json()
            position = data['iss_position']
            return {
                "latitude": float(position['latitude']),
                "longitude": float(position['longitude'])
            }
        except Exception as e:
            print(f"Error fetching ISS location: {e}")
            return None

    def check_visibility(self, user_city, radius_km=1500):
        """
        Check if ISS is visible from user's city within a certain radius.
        """
        try:
            # Get user coordinates
            location = self.geolocator.geocode(user_city)
            if not location:
                return {"error": "City not found."}
            
            user_coords = (location.latitude, location.longitude)
            
            # Get ISS coordinates
            iss_data = self.get_iss_location()
            if not iss_data:
                return {"error": "Could not fetch ISS data."}
            
            iss_coords = (iss_data['latitude'], iss_data['longitude'])
            
            # Calculate distance
            distance = geodesic(user_coords, iss_coords).km
            
            is_visible = distance <= radius_km
            
            return {
                "visible": is_visible,
                "distance_km": round(distance, 1),
                "iss_coords": iss_data,
                "user_coords": {"lat": location.latitude, "lon": location.longitude},
                "status_text": "VISIBLE NOW" if is_visible else "NOT VISIBLE"
            }
        except Exception as e:
            return {"error": str(e)}
