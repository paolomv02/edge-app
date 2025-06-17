from peewee import SqliteDatabase

db = SqliteDatabase('edugo.db')

def init_db() -> None:
    db.connect()
    from tracking.infrastructure.models import GPSLocation
    db.create_tables([GPSLocation], safe=True)
    print("Database initialized and tables created.")