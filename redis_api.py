from crypt import methods
from flask import Flask
from redis_service import Redis_service
from flask import request, jsonify

app = Flask(__name__)

def get_redis_obj(index):
    config = {
        'persist': True,
        'load_file': True,
        'expiry': 20
    }

    redis_obj = Redis_service(index=index, config = config)
    return redis_obj

@app.route("/<index>/get/<key>", methods=["GET"])
def redis_api_get(index, key):
    redis_obj = get_redis_obj(index=index)
    value = redis_obj.get(key)
    return {'value': value}

@app.route("/<index>/", methods=["POST"])
def redis_api(index):
    redis_obj = get_redis_obj(index=index)

    data = request.get_json()
    key = data.get('key')
    value = data.get('value')
    status = redis_obj.set(key=key, value=value)
    return {'status': status}

@app.route("/<index>/remove/<key>", methods=["GET"])
def redis_api_remove(index, key):
    redis_obj = get_redis_obj(index=index)

    # if request.method == 'GET':
    value = redis_obj.remove(key)
    return {'value': value}

@app.route("/<index>/get_all", methods=["GET"])
def redis_api_get_all(index):
    redis_obj = get_redis_obj(index=index)

    # if request.method == 'GET':
    value = redis_obj.get_all()
    return {'value': value}

