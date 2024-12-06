# Network Security Project

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
├── .github/ # GitHub Actions workflows
├── Network_Security/ # Main package
│ ├── Components/ # Core ML pipeline components
│ │ ├── data_ingestion.py # Data collection from MongoDB
│ │ ├── data_validation.py # Data quality checks
│ │ ├── data_transformation.py # Feature engineering
│ │ └── model_trainer.py # Model training and evaluation
│ │
│ ├── Cloud/ # Cloud integration utilities
│ │ └── s3_syncer.py # AWS S3 sync functionality
│ │
│ ├── Constants/ # Project constants and configs
│ ├── Entity/ # Data classes and type definitions
│ ├── Exeptions_Handle/ # Custom exception handling
│ ├── Logging/ # Logging configuration
│ ├── Pipeline/ # Training and prediction pipelines
│ └── Utils/ # Utility functions
│ ├── main_utils/ # General utilities
│ └── ml_utils/ # ML-specific utilities
│
├── logs/ # Application logs
├── tests/ # Unit and integration tests
├── app.py # FastAPI application
├── main.py # Training pipeline entry point
├── Dockerfile # Container configuration
└── requirements.txt # Project dependencie

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
