from flask import Flask, jsonify, request
import json

app = Flask(__name__)

people = [
    {"id": 1,
     "name": "Luke" },
    {
        "id" : 2,
        "name" : "Dark vader"
    } 
   ]
users = [
    {"id" : 1, "email" :"juanjo@mail.com","favorites" : "Luke" , "is_active" : False}
]   

@app.route('/people', methods=['GET'])
def getpeople():
    json_text = jsonify(people)
    return json_text, 201

@app.route('/people/<int:people.id>', methods=['GET'])
def getperson():
    json_text = jsonify(people.id)
    return json_text, 201

@app.route('/users', methods=['GET'])
def getusers():
    json_text = jsonify(users)
    return json_text, 201

@app.route('/users/<int:users.id>', methods=['GET'])
def getfavorites():
    json_text = jsonify(users.favorites)
    return json_text, 201


@app.route ("/favorite/people/<int:people.id>", methods = ["POST"])
def add_new_favorite():
    request_body =json.loads(request.data) 
    #print ("Peticion recibida con el body", request_body)
    users.favorites.append(request_body)
    return jsonify(users.favorites), 201

@app.route('/favorite/people/<int:people.id>', methods=['DELETE'])
def delete_favorite(position):
    if (position >= len(todos)):
        return "Posicion no existe", 404
    if (position < 0):
        return "La posicion no puede ser menor a cero", 404    
    todos.pop(users.favorites.people.id)
    return jsonify (users.favorites)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=3245, debug=True)

