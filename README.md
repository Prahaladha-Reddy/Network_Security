﻿# Network Security Project

## Overview

The Network Security project is designed to provide a comprehensive solution for monitoring and securing network traffic. It leverages machine learning models to detect anomalies and potential threats in network data. The project is structured to facilitate data ingestion, validation, transformation, model training, and deployment.

## Features

- **Data Ingestion**: Collects and processes network data for analysis.
- **Data Validation**: Ensures the integrity and quality of the data.
- **Data Transformation**: Prepares data for model training by applying necessary transformations.
- **Model Training**: Trains machine learning models to detect network anomalies.
- **Model Deployment**: Deploys trained models for real-time network monitoring.

## Project Structure

Network_Security/
├── .git/                           # Git version control directory
├── .github/                        # GitHub Actions workflows
│   └── workflows/                  # CI/CD pipelines
│       └── workflow.yml            # GitHub Actions configuration file
├── Network_Data/                   # Directory for storing network-related data files
├── Network_Security/               # Main project directory
│   ├── __init__.py                 # Initialization file for the package
│   ├── Cloud/                      # Cloud integration utilities
│   │   └── s3_syncer.py            # AWS S3 sync functionality
│   ├── Components/                 # Core components of the ML pipeline
│   │   ├── __init__.py             # Initialization file for components
│   │   ├── data_ingestion.py       # Data ingestion from MongoDB
│   │   ├── data_validation.py      # Data quality checks
│   │   ├── data_transformation.py  # Feature engineering and preprocessing
│   │   ├── model_trainer.py        # Model training and evaluation
│   │   ├── inference.py            # Inference script for making predictions
│   │   └── deployment.py           # Deployment-related utilities
│   ├── Constants/                  # Project constants and configurations
│   │   ├── __init__.py             # Initialization file for constants
│   │   └── training_pipeline.py    # Training pipeline constants
│   ├── Entity/                     # Entity classes and type definitions
│   │   ├── __init__.py             # Initialization file for entities
│   │   ├── config_entity.py        # Configuration entity definitions
│   │   └── artifact_entity.py      # Artifact entity definitions
│   ├── Exceptions_Handle/          # Custom exception handling
│   │   ├── __init__.py             # Initialization file for exceptions
│   │   └── exception.py            # Custom exception class
│   ├── Logging/                    # Logging utilities and configuration
│   │   ├── __init__.py             # Initialization file for logging
│   │   ├── logger.py               # Logger setup and configuration
│   ├── Pipeline/                   # Orchestration and training pipeline
│   │   ├── __init__.py             # Initialization file for pipeline
│   │   └── training_pipeline.py    # Training pipeline orchestration
│   ├── Utils/                      # General utility functions
│       ├── __init__.py             # Initialization file for utils
│       ├── file_handler.py         # Utilities for file operations
│       └── ml_utils.py             # ML-specific utility functions
├── logs/                           # Directory for application logs
│   └── example.log                 # Example log file (for demonstration purposes)
├── Artifacts/                      # Directory for storing pipeline artifacts
│   ├── <timestamp>/                # Timestamped directory for each pipeline run
│   │   ├── data_ingestion/         # Data ingestion artifacts
│   │   │   ├── feature_store/      # Feature store files
│   │   │   └── ingested/           # Ingested data files
│   │   ├── data_validation/        # Data validation artifacts
│   │   │   ├── validated/          # Validated data files
│   │   │   └── drift_report/       # Data drift reports
│   │   ├── data_transformation/    # Data transformation artifacts
│   │   │   ├── transformed_data/   # Transformed data files
│   │   │   └── preprocessor.pkl    # Saved preprocessor objects
│   │   ├── model_trainer/          # Model training artifacts
│   │   │   └── trained_model.pkl   # Trained ML model
│   │   └── final_model/            # Final model directory
├── tests/                          # Unit and integration tests
│   ├── __init__.py                 # Initialization file for tests
│   ├── test_data_ingestion.py      # Unit tests for data ingestion
│   ├── test_data_validation.py     # Unit tests for data validation
│   └── test_model_trainer.py       # Unit tests for model training
├── app.py                          # FastAPI or Flask application entry point
├── Dockerfile                      # Dockerfile for containerizing the application
├── requirements.txt                # Project dependencies
├── setup.py                        # Project packaging and installation script
├── README.md                       # Project documentation and overview
└── push_data.py                    # Script for pushing data to MongoDB

## 🚀 Features

### ML Pipeline Components

- **Data Ingestion**: MongoDB integration for data collection
- **Data Validation**: Schema validation and data quality checks
- **Data Transformation**: Feature engineering and preprocessing
- **Model Training**: Multiple classifier support with hyperparameter tuning
- **Model Registry**: MLflow integration for experiment tracking

### Infrastructure

- **CI/CD Pipeline**: Automated testing and deployment with GitHub Actions
- **Cloud Integration**: AWS ECR and S3 for model artifacts
- **API Service**: FastAPI endpoints for predictions
- **Containerization**: Docker support for consistent deployment

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- Docker
- AWS CLI
- Git

### Local Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Prahaladha-Reddy/Network_Security.git
   cd Network_Security
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables**

   Create a `.env` file in the root directory and add the following:

   ```plaintext
   MLFLOW_TRACKING_URI=<your_mlflow_tracking_uri>
   MLFLOW_TRACKING_USERNAME=<your_mlflow_username>
   MLFLOW_TRACKING_PASSWORD=<your_mlflow_password>
   MONGO_DB_URL=<your_mongo_db_url>
   ```

### Running the Application

1. **Start the Training Pipeline**

   ```bash
   python main.py
   ```

2. **Run the FastAPI Server**

   ```bash
   uvicorn app:app --reload
   ```

   Access the API documentation at `http://localhost:8000/docs`.

## Usage

- **Training**: Initiate the training pipeline using the `/train` endpoint.
- **Prediction**: Upload a CSV file with network data to the `/predict` endpoint to get predictions.

## Continuous Integration and Deployment

The project uses GitHub Actions for CI/CD. The workflow is defined in `.github/workflows/main.yml` and includes:

- **Continuous Integration**: Linting and unit tests.
- **Continuous Delivery**: Builds and pushes Docker images to Amazon ECR.
- **Continuous Deployment**: Deploys the Docker container to a self-hosted runner.

## Making Changes

### Configuration Changes

- **AWS Credentials**: Update the AWS credentials in the GitHub repository secrets for deployment.
- **Model Parameters**: Modify model parameters in `model_trainer.py` to experiment with different algorithms and hyperparameters.

### Code Changes

- **Data Ingestion**: Modify `data_ingestion.py` to change the data source or preprocessing steps.
- **Model Training**: Update `model_trainer.py` to add new models or change existing ones.

### Workflow Changes

3. **API Endpoints**

- Add new endpoints in `app.py`
- Update prediction logic in `predict_route()`

### CI/CD Pipeline

1. **GitHub Actions Configuration**

- Workflow file: `.github/workflows/main.yml`
- Modify stages:
  - Continuous Integration (tests)
  - Continuous Delivery (Docker build)
  - Continuous Deployment (AWS deployment)

2. **AWS Configuration**

- Update ECR repository in GitHub Secrets
- Configure S3 bucket for artifacts
- Set up IAM roles and permissions

## 📊 Monitoring

### MLflow Tracking

- Access experiments at your MLflow tracking server
- Monitor metrics: F1 Score, Precision, Recall
- Compare model versions

### Logging

- Application logs in `logs/` directory
- Format: `[timestamp] [level] [module] - message`

## 📧 Contact

Prahaladha Reddy - prahaladreddy80@gmail.com

Project Link: [https://github.com/Prahaladha-Reddy/Network_Security](https://github.com/Prahaladha-Reddy/Network_Security)
