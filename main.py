import os
from Network_Security.Components.data_ingestion import DataIngestion
from Network_Security.Exeptions_Handle.exeption import NetworkSecurityException
from Network_Security.Logging.logger import logging
from Network_Security.Entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
import sys

if __name__ == '__main__':
    try:
        training_pipeline_config = TrainingPipelineConfig()
        
        # Ensure the artifact directory is created
        if not os.path.exists(training_pipeline_config.artifact_dir):
            os.makedirs(training_pipeline_config.artifact_dir)
            logging.info(f"Created artifact directory at {training_pipeline_config.artifact_dir}")
        
            trainingpipelineconfig=TrainingPipelineConfig()
            dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
            data_ingestion=DataIngestion(dataingestionconfig)
            logging.info("Initiate the data ingestion")
            dataingestionartifact=data_ingestion.initiate_data_ingestion()
            logging.info("Data Initiation Completed")
            print(dataingestionartifact)
    except Exception as e:
           raise NetworkSecurityException(e,sys)