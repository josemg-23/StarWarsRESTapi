from flask import Flask, jsonify, request
import json

app = Flask(__name__)

todos = [
    {"label": "Wash dishes", "done": False },
   ]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route ("/todos", methods = ["POST"])
def add_new_todo():
    request_body =json.loads(request.data) 
    #print ("Peticion recibida con el body", request_body)
    todos.append(request_body)
    return jsonify(todos), 201

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if (position >= len(todos)):
        return "Posicion no existe", 404
    if (position < 0):
        return "La posicion no puede ser menor a cero", 404    
    todos.pop(position)
    return jsonify (todos)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=3245, debug=True)

