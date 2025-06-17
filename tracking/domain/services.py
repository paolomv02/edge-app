from datetime import datetime, timezone
from dateutil.parser import parse
from tracking.domain.entities import GPSLocation
from tracking.infrastructure.repositories import GPSLocationRepository

class GPSLocationService:
    def __init__(self):
     """Initialize the GPSLocationService.
     """

    @staticmethod    
    def create_location(device_id: str, latitude: float, longitude: float, created_at: str | None) -> GPSLocation:
        try:
            latitude = float(latitude)
            longitude = float(longitude)
            if created_at:
                parsed_created_at = parse(created_at).astimezone(timezone.utc)
            else:
                parsed_created_at = datetime.now(timezone.utc)
        except (ValueError, TypeError):
            raise ValueError("Invalid GPS location data provided.")
        return GPSLocation(device_id, latitude, longitude, parsed_created_at)  
    
    @staticmethod
    def get_all_locations() -> list[GPSLocation]:
        return GPSLocationRepository.get_all()
