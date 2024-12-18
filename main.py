import os
from Network_Security.Components.data_ingestion import DataIngestion
from Network_Security.Exeptions_Handle.exeption import NetworkSecurityException
from Network_Security.Logging.logger import logging
from Network_Security.Entity.config_entity import *
import sys
from Network_Security.Components.data_transformation import DataTransformation
from Network_Security.Components.model_trainer import *
from Network_Security.Components.data_validation import DataValidation
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
            data_validation_config=DataValidationConfig(trainingpipelineconfig)
            data_validation=DataValidation(dataingestionartifact,data_validation_config)
            logging.info("Initiate the data Validation")
            data_validation_artifact=data_validation.initiate_data_validation()
            logging.info("data Validation Completed")
            print(data_validation_artifact)
            data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
            logging.info("data Transformation started")
            data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
            data_transformation_artifact=data_transformation.initiate_data_transformation()
            print(data_transformation_artifact)
            logging.info("data Transformation completed")
            logging.info("Model Training stared")
            model_trainer_config=ModelTrainerConfig(trainingpipelineconfig)
            model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
            model_trainer_artifact=model_trainer.initiate_model_trainer()

            logging.info("Model Training artifact created")
        
    except Exception as e:
           raise NetworkSecurityException(e,sys)