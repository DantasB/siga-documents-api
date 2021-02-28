# Siga-Documents-API

A simple API built using python made by Bruno Dantas.

This project was used to learn a little about flask and improve my python skills. The idea is to access the siga page and download a document, returning it in a single object.


## Important 
This API is actually offline, but you can run this project in your machine.


### Setup
Setting up the Siga Documents API is a no-brainer, just follow the guide below:
1. Download all the files.
2. Install all the libraries located at the [requirements.txt](requirements.txt).
4. Run the [main.py](main.py).

### Routes
- *'/':* This route will return every doc_type that can be downloaded using the api.
- *'/[login]/[password]/[document_type]':* This route, you need to pass the siga credentials and the document_type that you want to download.


### Object
The [response object](https://github.com/DantasB/Siga-Documents-API/blob/main/Objects/response_object.py) is the information that the api returns. The information returned by the api are:
- current_date (string)
- error_message (string)
- pdf_document (list)
- status (bool)

If you still need help in how to run this project or doubts about flask and python, fell free to contact me on discord: BDantas#3692
