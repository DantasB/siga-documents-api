# Siga-Documents-API

![demonstration](https://cdn.discordapp.com/attachments/539836407628169237/824487428856217620/unknown.png)

## Table of Contents

<!--ts-->
   * [About](#about)
   * [Requirements](#requirements)
   * [How to use](#how-to-use)
      * [Setting up Program](#program-setup)
      * [Response Object](#object)  
   * [Routes](#routes)  
   * [Technologies](#technologies)
<!--te-->

## About

A simple API built using python made by Bruno Dantas.

This project was used to learn a little about flask and improve my python skills. The idea is to access the siga page and download a document, returning it in a single object.

## Requirements

To run this repository by yourself you will need to install python3 in your machine and them install all the requirements inside the [requirements](requirements.txt) file

## How to use

### Program Setup

```bash
# Clone this repository
$ git clone <https://github.com/DantasB/Siga-Documents-API>

# Access the project page on your terminal
$ cd Siga-Documents-API

# Install all the requirements
$ pip install -r requirements.txt

# Execute the main program
$ python main.py

# The api will start and them you can make your own requests. Check in the terminal what is the url.
```
![demonstration](https://cdn.discordapp.com/attachments/539836407628169237/824485349862277130/unknown.png)

### Object

The [response object](https://github.com/DantasB/Siga-Documents-API/blob/main/Objects/response_object.py) is the information that the api returns. The information returned by the api are:
- current_date (string)
- error_message (string)
- pdf_document (list)
- status (bool)

### Routes

- *'/':* This route will return every doc_type that can be downloaded using the api.
- *'/document?login=your_login&password=your_password&document_type=document_to_be_downloaded':* This route, you need to pass the siga credentials and the document_type that you want to download.

## Technologies

* Python3
* Flask
* validate_docbr
* PyPDF2


If you still need help in how to run this project or doubts about flask and python, fell free to contact me on discord: BDantas#3692
