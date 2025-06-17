from flask import Flask

from tracking.interfaces.services import gps_api
from shared.infrastructure.database import init_db

app = Flask(__name__)
app.register_blueprint(gps_api)

first_request = True

@app.before_request
def setup():
    global first_request
    if first_request:
        first_request = False
        init_db()


if __name__ == '__main__':
    app.run(debug=True)