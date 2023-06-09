import flask
from flask import request, jsonify

books = [
     {'id': 0,
 'title': 'A Fire Upon the Deep',
 'author': 'Vernor Vinge',
 'first_sentence': 'The coldsleep itself was dreamless.',
 'year_published': '1992'},
 {'id': 1,
 'title': 'The Ones Who Walk Away From Omelas',
 'author': 'Ursula K. Le Guin',
 'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
 'published': '1973'},
 {'id': 2,
 'title': 'Dhalgren',
 'author': 'Samuel R. Delany',
 'first_sentence': 'to wound the autumnal city.',
 'published': '1975'}
]

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
 return jsonify(books)



@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/api/v1/resources/book', methods=['GET'])
def api_id():
    if 'id' in request.args:
        print(request.args)
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []
    for book in books:
        if book['id'] == id:
            results.append(book)
    return jsonify(results)

@app.route('/api/v1/resources/muchosbooks', methods=['GET'])
def api_id_muchos():
    results = []
    if 'id' in request.args:
        print(request.args)
        #id = int(request.args['id'])
        for combinacion in dict(request.args.lists()).items():
            print("aquí",combinacion)
            if combinacion[0] == "id":
                mis_ids = combinacion[1]
                for mi_id in mis_ids:
                    for book in books:
                        if book['id'] == int(mi_id):
                            results.append(book)
    else:
        return "Error: No id field provided. Please specify an id."

    return jsonify(results)





@app.route('/api/v1/resources/book/<string:title>', methods=['GET'])
def get_by_title(title):
    for book in books:
      if book['title'] == title:
         return jsonify(book)
    return jsonify({'message': "Book not found"})



@app.route('/api/v2/resources/book', methods=['GET'])
def get_by_id():
    id = int(request.get_json()['id'])
    for book in books:
        if book['id'] == id:
            return jsonify(book)
    return jsonify({'message': "Book not found"})

@app.route('/api/v1/resources/book', methods=['POST'])
def post_book():
    data = request.get_json()
    books.append(data)
    return data



app.run()