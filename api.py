from flask import Flask, request
from flask_restful import Resource, Api
import db

app = Flask(__name__)
api = Api(app)

class User(Resource):
    def get(self):
        userList = db.User.getAll()
        length = len(userList)
        if length == 0:
            return 204
        
        return {'user-list': userList, 'length': length}, 200
    
    def post(self):
        json = request.get_json(force=True)
        userId = json.get('user-id')
        userName = json.get('user-name')
        nfcId = json.get('nfc-id')

        # 無効な形式ならエラーを返す
        if type(userId) != int:
            return {'message': '"user-id" must be int.'}, 400
        
        if type(userName) != str:
            return {'message': '"user-name" must be str.'}, 400
        
        if type(nfcId) != int and type(nfcId) != type(None):
            return {'message': '"nfc-id" must be int or null.'}, 400
        
        # ユーザIDが重複していたらエラーを返す
        #userList = db.User.getAll()
        if False:
            return {'message': 'duplicate user ID.'}, 409

        # 新しくユーザを作成する
        #user = db.User.add(userId, userName)
        #return {'user-id': user.id, 'user-name': user.name}
        return 201

class VariableUser(Resource):
    def get(self, id: int):
        return 200
    
    def put(self, id: int):
        return 400
    
    def delete(self, id: int):
        return 204

class Door(Resource):
    def get(self):
        return 200
    
    def put(self):
        json = request.get_json(force=True)
        isLocked = json.get('is-locked')

        if type(isLocked) != bool:
            return {'message': '"is-locked" must be boolean.'}, 400

        #door = db.Door.set(isLocked)
        #return {'is-locked': door.isLocked}, 200
        return 200

api.add_resource(User, '/users')
api.add_resource(VariableUser, '/users/<int:id>')
api.add_resource(Door, '/door')

app.run(debug=True)
