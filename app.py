from flask import Flask, jsonify, request


app = Flask(__name__)
tasks = [{
    'task_id': 0,
    'task_title': 'Clean Laundry',
    'task_description': 'Clean The Dirt Laundary In The Washing Machine',
    'is_done': False,
}, {
    'task_id': 1,
    'task_title': 'Clean Dishes',
    'task_description': 'Clean The Dirt Laundary In The Dish Washer',
    'is_done': True,
}, {
    'task_id': 2,
    'task_title': 'Clean Room',
    'task_description': 'Clean Your Room',
    'is_done': False,
}]

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/addData', methods=['POST'])
def add_data():
    print(request.json)
    if not request.json:
        return jsonify({
            'status': 'Error',
            'message': 'No Request Found To Post Data'
        }, 400)
  
    task = {
        'task_id': tasks[-1]['task_id'] + 1,
        'task_title': request.json['task_title'],
        'task_description': request.json['task_description'],
        'is_done':  request.json['is_done']
    }
    tasks.append(task)
    return jsonify({
            'status': 'Success',
            'message': 'Task Successfully Posted'
        })

@app.route('/getData')
def get_task():
    return jsonify({
        'data': tasks
    })

if __name__ == '__main__':
    app.run(debug=True)