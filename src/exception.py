import sys
from src.logger import logging

def exception_details(error:Exception, error_details:sys) -> str:
    _,_, exc = error_details.exc_info()
    filename = exc.tb_frame.f_code.co_filename

    error_message = f"Error occurred in {filename} in line no. {exc.tb_lineno}: {str(error)}"

    logging.info(error_message)

    return error_message


class CustomException(Exception):
    def __init__(self, error:Exception, error_details:sys):
        super().__init__(error)
        self.error_message = exception_details(error, error_details)

    def __str__(self):
        return self.error_message