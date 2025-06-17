from peewee import Model, AutoField, FloatField, CharField, DateTimeField
from shared.infrastructure.database import db

class GPSLocation(Model):
    id = AutoField()
    device_id = CharField()
    latitude = FloatField()
    longitude = FloatField()
    created_at = DateTimeField()
    

    class Meta:
        database = db
        table_name = 'gps_locations'