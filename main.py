from flask import Flask,request,jsonify
from functools import wraps
from dotenv import load_dotenv
import os
from flask_cors import CORS


# Load .env variables
load_dotenv()

app = Flask(__name__)

CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": ["https://razinco-procurement.web.app", "http://localhost:4200"]}})


# Read the token from the environment
API_TOKEN = os.getenv("API_TOKEN")

store = {}

def authenticate(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        expected_token = f"Bearer {API_TOKEN}"
        if token != expected_token:
            return jsonify({"message": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated


@app.route('/api/set', methods=['POST'])
@authenticate
def set_value():
    data = request.json
    key = data.get('key')
    value = data.get('value')
    
    if not key or value is None:
        return jsonify({'error':'Key or Value is empty.'}),400
    
    store[key] = value
    return jsonify({'message':f' Key :{key} set successfully.'}),200


@app.route('/api/get',methods=['POST'])
@authenticate
def get_value():
    data = request.json
    key = data.get('key')
    if key is None:
        return jsonify({'error':f'Key is empty'}),400
    
    value = store.get(key)
    
    if value is None:
        return jsonify({'error':f'Value is empty for key: {key}'}), 404
    
    return jsonify({'key':key,'value':value}),200


if __name__ == '__main__':
    app.run(debug=True)