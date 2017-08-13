import os
from datetime import datetime
from flask import Flask
from flask import Response
from pymongo import MongoClient
from bson import json_util
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
CORS(app, resources={r"/api/*": {"origins": "*"}})
mongo_client = MongoClient(app.config.get("MONGO_DATABASE_URI"))
mongo_database = app.config.get("MONGO_DATABASE")
db = mongo_client[mongo_database]


@app.route('/api/v1/current')
def get_current_deals():
    now = datetime.now()
    query = {
        "date_from": {"$lte": now},
        "date_to": {"$gte": now}
    }

    return Response(
        json_util.dumps(
            [offer for offer in db['offers'].find(query)],
            json_options=json_util.STRICT_JSON_OPTIONS
        ),
        mimetype='application/json'
    )
