# AWS CICD Deployment with Github Actions
## 1.Login to AWS console
## 2. Create IAM instance for deployement

    # with specifc access
    1.EC2 access: it is virtual machine
    2.ECR: Elastic Containerregistry to save your docker image in AWS.

    #Description:About the deployement
    1.Build docker image of the source code.
    2.Push the docker image to ECR.
    3.Launch your EC2.
    4.Pull your image from ECR to EC2.
    5.Launch your docker image to EC2.

    # Policy:
    1.AmazonEC2ContainerRegistryFullAccess
    2.AmazonEC2FullAccess
## 3.Create ECR repo to store/save docker image
    Save the URI: 
## 4.Create EC2 machine (Ubantu)

## 5. Open EC2 and install docker in thr EC2 Machine:
    ##optional
    sudo apt-get update -y
    sudo apt-get upgrade

    #required
    curl -fsSL https://get.docker.com/ -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker ubuntu
    newgrp docker

## 6.Configure EC2 as self-hosted runner
    seting>actions>runner>new self hosted runner> choose os> then run command one by one

## 7. Setup github secrets:
    AWS_ACCESS_KEY_ID =
    AWS_SECRET_ACCESS_KEY =
    AWS_REGION =
    AWS_ECR_LOGIN_URI =
    ECR_REPOSITORY_NAME = simple-app

    

# End-to-end-Wine-quality

## Workflows
1.Update config.yaml
    Purpose: Centralizes project configurations (e.g., file paths, model settings, environment variables).
    Why:Avoids hardcoding paths/settings.Makes the project environment-agnostic (e.g., works locally, on cloud, or in containers).
2.Update schema.
    Purpose: Defines the expected structure of input data (column names, data types, validation rules).
    Why:Ensures data consistency (e.g., during preprocessing or API inputs).Catches data drift early.
3.Update params.yaml
    Purpose: Stores hyperparameters and training settings (e.g., learning rate, epochs).
    Why:Separates tunable parameters from code for easy experimentation.Facilitates reproducibility (e.g., logging exact params for each run).
4.Update the entity
    Purpose: Defines data classes (e.g., using dataclass or Pydantic) to enforce type safety.
    Why:Validates data flow between components (e.g., ensures model_name is always a string).Improves code readability and debugging.
5.Update the configuration manager in src config
    Purpose: Reads YAML files (config.yaml, params.yaml) and converts them into Python objects (e.g., ConfigBox).
    Why:Centralizes configuration loading.Provides dot-notation access (e.g., config.data_path).
6.Update the components
    Purpose: Modularizes ML steps (e.g., data ingestion, preprocessing, training).
    Why:Encourages reusability (e.g., reuse preprocessing in training/inference).Isolates failures (e.g., a bug in training won’t break data ingestion).
7.Update the pipeline
    Purpose: Chains components into a workflow (e.g., ingest → preprocess → train).
    Why:Automates end-to-end execution.Supports orchestration tools (e.g., Airflow, Kubeflow).
8.Update the main.py
    Purpose: Entry point for running the pipeline (e.g., CLI or script execution).
    Why:Standardizes how the project is executed (e.g., python main.py --stage train).Integrates with logging/metrics tracking.
9.Update the app.py
    Purpose: Serves the model (e.g., as a REST API using FastAPI/Flask).
    Why:Enables real-time predictions (e.g., for production deployments).Validates inputs  schema.yaml                                                                                        
### STEPS:
Clone the repository 
```bash
https://github.com/Bavan-M/End-to-end-Wine-quality
```
### STEP-01 Create a conda environment after opening the repository

```bash
python -m venv mlproj
```

```bash
.\mlproj\Scripts\activate
```
### STEP-02 Install the Requirments
```bash
pip install -r requirements.txt








