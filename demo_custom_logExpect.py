from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

# logging.info("This is a test of logging level INFO")


try: 
    a = 10/0

except Exception as e:
    logging.exception(USvisaException(e, sys))

