from flask import Flask
from SQLAdapter import executeQuery, createTable

app = Flask(__name__)

@app.route('/', methods=['GET'])
def simple_response():
    return { 'message': 'All is good' }

if __name__ == '__main__':
    createTable()
    app.run(host='0.0.0.0', port=80)
