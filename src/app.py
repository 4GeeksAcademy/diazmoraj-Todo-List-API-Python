from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

todos = [{"label": "My first task", "done": False}]
# todos = [{"label": "Sample", "done": True}]

@app.route('/todos', methods=['GET'])
def hello_world():
    # return "<h1>Hello!</h1>"
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<position:int>', methods=['DELETE'])
def delete_todo(position):
    if position < 0 or position >= len(todos):
        return jsonify({"error", "Position out of range"})
    
    todos.pop(position)
    print("This is the position to delete:", position)
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)