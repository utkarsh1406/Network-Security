import os 
import sys
import json
import certifi
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exceptions.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


from dotenv import load_dotenv
load_dotenv()
MongoDBUrl = os.getenv("MONGO_DB_URL_KEY")
# Certify is used to cerate Trust certificate for HTTP request 
# CA is certificate Authority
ca = certifi.where()  # retreives the path from bundle of trusted certificate Authorities

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_converter(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def insert_data_to_Mongodb(self,records,database,collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records
            self.mongo_client = pymongo.MongoClient(MongoDBUrl)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
        
if __name__ == '__main__':
    File_Path = r'networkdata/phisingData.csv'
    DataBase = 'Network_DataBase'
    Collection = 'NetworkData'
    networkObj = NetworkDataExtract()
    records = networkObj.csv_to_json_converter(file_path=File_Path)
    no_of_records = networkObj.insert_data_to_Mongodb(records=records, database=DataBase, collection=Collection)