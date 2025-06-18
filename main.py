from flask import Flask,request,jsonify

app = Flask(__name__)

store = {}

@app.route('/api/set', methods=['POST'])
def set_value():
    data = request.json
    key = data.get('key')
    value = data.get('value')
    
    if not key or value is None:
        return jsonify({'error':'Key or Value is empty.'}),400
    
    store[key] = value
    return jsonify({'message':f' Key :{key} set successfully.'}),200


@app.route('/api/get',methods=['POST'])
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