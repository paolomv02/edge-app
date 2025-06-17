from tracking.domain.entities import GPSLocation
from tracking.infrastructure.models import GPSLocation as GPSLocationModel
from datetime import datetime

class GPSLocationRepository:
    @staticmethod
    def save(gps_location) -> GPSLocation:
        location = GPSLocationModel.create(
            device_id=gps_location.device_id,
            latitude=gps_location.latitude,
            longitude=gps_location.longitude,
            created_at=gps_location.created_at
        )
        return GPSLocation(
            gps_location.device_id,
            gps_location.latitude,
            gps_location.longitude,
            gps_location.created_at,
            location.id
        )
    
    @staticmethod
    def get_all() -> list[GPSLocation]:
        locations = GPSLocationModel.select()
        result = []
        for loc in locations:
            # Asegúrate de que created_at es datetime
            created_at = loc.created_at
            if isinstance(created_at, str):
                created_at = datetime.fromisoformat(created_at.replace("Z", ""))
            result.append(GPSLocation(
                loc.device_id,
                loc.latitude,
                loc.longitude,
                created_at,
                loc.id
            ))
        return result
