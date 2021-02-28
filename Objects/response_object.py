from datetime import datetime

class Response():
    """ The object to be returned in the api. It contains the request status and the pdf document.
        
        Args:
            pdf_document (list, optional): the bytes list of the downloaded document. Defaults to None.
            status (bool, optional): true if the capture was correct. Defaults to False.
            error_message (str, optional): if there's any error. Defaults to "".
    """
    def __init__(self, pdf_document=None, status=False, error_message=""):

        self.pdf_document  = pdf_document
        self.status        = status
        self.error_message = error_message
        self.current_date  = datetime.today()

    def serialize(self):
        """ We need to serialize the object before send it through the api

        Returns:
            dictionary: the response object serialized
        """
        return { "PDF": self.pdf_document,
                "Status": self.status,
                "ErrorMessage": self.error_message,
                "CurrentDate": self.current_date}
