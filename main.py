from Network_Security.Components.data_ingestion import DataIngestion
from Network_Security.Exeptions_Handle.exeption import NetworkSecurityException
from Network_Security.Logging.logger import logging
from Network_Security.Entity.config_entity import DataIngestionConfig

from Network_Security.Entity.config_entity import TrainingPipelineConfig
import sys
if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)
    except Exception as e:
        NetworkSecurityException(e,sys)