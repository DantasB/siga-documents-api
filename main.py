import asyncio
from flask import Flask, Response, jsonify
from SharedLibrary.pdf_utils import *
from SharedLibrary.siga_utils import *
from Program.siga_core import *

app = Flask(__name__)

loop = asyncio.get_event_loop()

@app.route('/')
def get_disponible_document_type():
    return jsonify(list(list_of_documents.keys()))

@app.route('/<login>/<password>/<document_type>')
def get_document(login, password, document_type):
    pass


if __name__ == "__main__":
    app.run(debug=True)