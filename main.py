import asyncio
from flask import Flask, jsonify, request
from SharedLibrary.pdf_utils import *
from SharedLibrary.siga_utils import *
from Objects.response_object import *
from Program.siga_core import *

app = Flask(__name__)

loop = asyncio.get_event_loop()

@app.route('/')
def get_disponible_document_type():
    return jsonify(list(list_of_documents.keys()))

@app.route('/document')
def get_document():
    login = request.args.get('login')
    password = request.args.get('password')
    document_type = request.args.get('doctype')

    response = Response()

    if login is None or password is None or document_type is None:
        response.error_message = "PLEASE SET YOUR PARAMETERS LIKE: url?login=something&password=8888&doctype=crid"
        response.status        = False
        return jsonify(response.serialize())

    if treat_login(login) == "":
        response.error_message = "LOGIN IS NOT A VALID CPF. CHECK YOUR CREDENTIALS."
        response.status        = False
        return jsonify(response.serialize())
    
    if document_type not in list_of_documents:
        response.error_message = "DOCUMENT TYPE NOT VALID. CHECK YOUR CREDENTIALS."
        response.status        = False
        return jsonify(response.serialize())
    
    pdf_path, pdf = loop.run_until_complete(get_document_from_siga(login, password, document_type))
    if not is_valid_file_path(pdf_path):
        response.error_message = "PDF NOT VALID. CHECK IF YOU HAVE THIS DOCUMENT, YOUR CREDENTIALS ARE CORRECT OR IF SIGA IS NOT ONLINE."
        response.status        = False
        return jsonify(response.serialize())
    
    delete_document(pdf_path.split('/',2)[0])
    
    response.pdf_document = list(pdf)
    response.status       = True
    return jsonify(response.serialize())

if __name__ == "__main__":
    app.run(debug=True)