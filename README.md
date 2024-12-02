# Network Security Project

## Project Overview

This project is focused on **network security**, leveraging tools and frameworks to build secure, efficient, and scalable applications. It includes modules for cloud integration, logging, exception handling, pipelines, and utilities to ensure comprehensive security and functionality.

---

## File Structure

```
Network_Security/
├── .git
├── .github
├── network
├── Network_Data
├── Network_Security
│   ├── Cloud
│   ├── Components
│   ├── Constants
│   ├── Entity
│   ├── Exceptions_Handle
│   ├── Logging
│   ├── Pipeline
│   ├── Utils
│   ├── __init__.py
├── Notebooks
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt
├── setup.py
```

### Key Directories and Files:

- **Network_Security/**: Core module containing submodules for various functionalities like cloud, logging, and pipeline integration.
- **requirements.txt**: Contains the list of dependencies required to run this project.
- **setup.py**: Script to configure the Python package and manage dependencies.
  - Uses the `get_requirements` function to dynamically read and install dependencies from `requirements.txt`.
  - Automatically finds all packages within the project using `find_packages()`.
- **Dockerfile**: Used for containerizing the application.
- **Notebooks/**: Placeholder for Jupyter Notebooks or similar documents.

---

## Installation

### Prerequisites

- Python 3.10+
- pip

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/Prahaladha-Reddy/Network_Security
   cd Network_Security
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate    # For Windows
   ```

3. Install the package and its dependencies:
   ```bash
   python setup.py install
   ```

---

## Dependencies

The project uses the following Python libraries:

- **python-dotenv**: For environment variable management.
- **pandas, numpy**: Data manipulation and analysis.
- **pymongo**: MongoDB driver for Python.
- **certifi**: SSL certificate validation.
- **scikit-learn**: Machine learning algorithms.
- **mlflow**: MLOps tracking and model management.
- **pyyaml**: YAML file handling.
- **dagshub**: Integration with DagsHub for data versioning.
- **python-multipart**: Handling file uploads.

---
