from tracking.domain.entities import GPSLocation
from tracking.domain.services import GPSLocationService
from tracking.infrastructure.repositories import GPSLocationRepository

class GPSLocationApplicationService:
    def __init__(self):
        self.gps_location_repository = GPSLocationRepository()
        self.gps_location_service = GPSLocationService()

    def create_location(self, device_id: str, latitude: float, longitude: float, created_at: str) -> GPSLocation:
        location = self.gps_location_service.create_location(device_id, latitude, longitude, created_at)
        return self.gps_location_repository.save(location)
    
    def get_all_locations(self) -> list[GPSLocation]:
        return self.gps_location_repository.get_all()