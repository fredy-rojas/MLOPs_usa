


# #_______________________________________
# # Testing MongoClient
# from us_visa.data_access.usvisa_data import USvisaData
# from us_visa.entity.config_entity import DataIngestionConfig

# data_ingestion_config = DataIngestionConfig()
# print(data_ingestion_config.collection_name)

# obj = USvisaData()
# df = obj.export_collection_as_dataframe(collection_name=data_ingestion_config.collection_name)
# print(df.shape)

#_________________________________
# Testing trainpipeline
from us_visa.pipline.training_pipeline import TrainPipeline

obj = TrainPipeline() # instantiation
obj.run_pipeline() # running method