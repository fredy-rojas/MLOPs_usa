import sys

from us_visa.exception import USvisaException
from us_visa.logger import logging

import os
from us_visa.constants import DATABASE_NAME, MONGODB_URL_KEY
import pymongo
import certifi   # To handle TIME OUT issue with mongoDB

ca = certifi.where()

class MongoDBClient:
    """
    Class Name :   MongoDBClient
    Description :  Design to handle the connection to a MongoDB database by initilizing a
                    client connection to MongoDB and stores a reference to a specific database 
                    within that MongoDB server.
                    Class-level attribute, ensure only one MongoDB client connection has been stablish. 
                     To handle client string url connection and authentications
    
    Output      :   connection to mongodb database
    On Failure  :   raises an exception
    """
    client = None

    def __init__(self, database_name=None) -> None:

        # Pending to improve how to initialize environment Key secrets values. 
        database_name = os.environ.get(DATABASE_NAME)
        
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, 
                                                        #    tlsCAFile=ca
                                                           )
                
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection succesfull")
        except Exception as e:
            raise USvisaException(e,sys)