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

```
Network_Security/
│
├── .github/
│   └── workflows/
│       └── main.yml
│
├── Network_Security/
│   ├── Components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── data_validation.py
│   │   └── model_trainer.py
│   │
│   ├── Constants/
│   ├── Entity/
│   ├── Exeptions_Handle/
│   ├── Logging/
│   ├── Pipeline/
│   └── Utils/
│
├── logs/
│
├── app.py
├── main.py
├── requirements.txt
└── setup.py
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Docker
- AWS CLI (for deployment)
- Git

### Installation

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

- **CI/CD Pipeline**: Modify `.github/workflows/main.yml` to add new steps or change existing ones for the CI/CD process.

## Logging and Monitoring

- **MLflow**: Used for experiment tracking and model management.
- **DagsHub**: Integrated for version control and collaboration.
