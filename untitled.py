from flask import Flask
from flask_restful import Api, abort, reqparse, Resource

app = Flask(__name__)
api = Api(app)

FOODS = {
    'foodid1': {'name': 'food 1', 'price': 24},
    'foodid2': {'name': 'food 2', 'price': 25},
    'foodid3': {'name': 'food 3', 'price': 26},
}

def abort_if_food_doesnt_exist(food_id):
    if food_id not in FOODS:
        abort(404,message="food {} doesn't exist".format(food_id))

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('price')

#Food
#shows a single food item and lets you delete a food item
class Food(Resource):
    def get(self,food_id):
        abort_if_food_doesnt_exist(food_id)
        return FOODS[food_id]

    def delete(self,food_id):
        abort_if_food_doesnt_exist(food_id)
        del FOODS[food_id]
        return  '',204

    def put(self,food_id):
        args = parser.parse_args()
        task = {'name':args['name'],'price':args['price']}
        FOODS[food_id] = task
        return task, 201

#FoodList
# shows a list of all foods, and lets you POST to add new foods
class TodoList(Resource):
    def get(self):
        return FOODS

    def post(self):
        args = parser.parse_args()
        food_id = int(max(FOODS.keys()).lstrip('food')) + 1
        food_id = 'food%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201