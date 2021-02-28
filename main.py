import asyncio
from flask import Flask, Response, jsonify
from SharedLibrary.pdf_utils import *
from SharedLibrary.siga_utils import *
from Program.siga_core import *

app = Flask(__name__)

loop = asyncio.get_event_loop()


@app.route('/<document_type>')
def get_document_(document_type):
    pass


if __name__ == "__main__":
    app.run(debug=True)