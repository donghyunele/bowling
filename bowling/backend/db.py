from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import objectid
from flask_cors import CORS

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'bowling'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/bowling'

mongo = PyMongo(app)

CORS(app)

@app.route('/api/task', methods=['POST'])
def add_task():
    tasks = mongo.db.tasks
    title = request.get_json()['title']

    task_id = tasks.insert({'title': title})
    new_task = tasks.find_one({'_id': task_id})

    result = {'title' : new_task['title']}

    return jsonify({'result': result})
    
@app.route('/api/tasks', methods=['GET'])
def get_all_tasks():
    tasks = mongo.db.tasks

    result = []

    for field in tasks.find():
        result.append({'_id': str(field['_id']), 'title': field['title']})
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)