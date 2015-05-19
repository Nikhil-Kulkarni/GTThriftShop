from flask import Flask
from flask import jsonify
from flask import abort
from flask import request
from flask import make_response

app = Flask(__name__)

items = [
	{
		'id':1,
		'name':'Dell XPS 15', 
		'price':'700',
		'description':'2011 Dell XPS 15 inch laptop, i7, 12GB RAM'
	}
]

@app.route('/getItems', methods=['GET'])
def get_items():
	return jsonify({'items':items})

@app.route('/postItem', methods=['POST'])
def post_item():
	if not request.json:
		abort(400)
	item = {
		'id': items[-1]['id'] + 1,
		'name': request.json['name'],
		'price': request.json['price'],
		'description': request.json['description']
	}
	items.append(item)
	return jsonify({'item':item}), 201

@app.route('/deleteItem/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
	item = [item for item in items if item['id'] == item_id]
	if len(item) == 0:
		abort(404)
	items.remove(item[0])
	return jsonify({'result':True})

if __name__ == '__main__':
	app.run(debug=True)
