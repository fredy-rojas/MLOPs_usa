import os
import sys

def error_message_detail(error, error_detail:sys):
    """
    Description:
    -----------


    Parameters:
    -----------
        error: The error or exception that occurred.
        error_detail: Typically passed as sys, which provides access to the exception details via sys.exc_info().

    Explanation:
    -----------
        error_detail.exc_info() retrieves information about the most recent exception caught by an except block.
                             It returns a tuple (type, value, traceback), but here only the traceback (exc_tb) is used.
                            ref: https://docs.python.org/3/library/traceback.html
                                to go inside of the exc_tb object and extract its elements information. 

        

    
    """
    
    _type, _value, exc_tb = error_detail.exc_info() # only traceback 'exc_tb' is used here


    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class USvisaException(Exception):
    def __init__(self, error_message, error_detail):
        """
        :param error_message: error message in string format
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message