from flask import Blueprint, request, jsonify
from tracking.application.services import GPSLocationApplicationService

gps_api = Blueprint('gps_api', __name__)

gps_location_service = GPSLocationApplicationService()

@gps_api.route('/api/v1/gps/locations', methods=['POST'])
def create_location():
    data = request.json
    try:
        device_id = data['device_id']
        latitude = data['latitude']
        longitude = data['longitude']
        created_at = data.get('created_at')
        location = gps_location_service.create_location(device_id, latitude, longitude, created_at)
        return jsonify({
            'id': location.id,
            'device_id': location.device_id,
            'latitude': location.latitude,
            'longitude': location.longitude,
            'created_at': location.created_at.isoformat() + "Z"
        }), 201
    except KeyError:
        return jsonify({'error': 'Missing required fields'}), 400
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
@gps_api.route('/api/v1/gps/locations', methods=['GET'])
def get_locations():
    locations = gps_location_service.get_all_locations()
    return jsonify([
        {
            'id': loc.id,
            'device_id': loc.device_id,
            'latitude': loc.latitude,
            'longitude': loc.longitude,
            'created_at': loc.created_at.isoformat() + "Z" if loc.created_at else None
        }
        for loc in locations
    ])