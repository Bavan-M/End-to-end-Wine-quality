from mlProject.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH,SCHEMA_FILE_PATH
from mlProject.utils.common import read_yaml,crate_directories
from mlProject.entity.config_entity import (DataIngestionConfig,DataValidationCofig,DataTransformationConfig,ModelTrainerConfig,ModelEvaluationConfig)

class ConfigurationManager:
    def __init__(
            self,
            config_filepath=CONFIG_FILE_PATH,
            params_filepath=PARAMS_FILE_PATH,
            schema_filepath=SCHEMA_FILE_PATH):
        
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)
        self.schema=read_yaml(schema_filepath)

        crate_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config=self.config.data_ingestion
        crate_directories([config.root_dir])
        data_ingestion_config=DataIngestionConfig(root_dir=config.root_dir,source_URL=config.source_URL,local_data_file=config.local_data_file,unzip_dir=config.unzip_dir)
        return data_ingestion_config
    
    def get_data_validation_config(self)->DataValidationCofig:
        config=self.config.data_validation
        schema=self.schema.COLUMNS
        crate_directories([config.root_dir])
        data_validation_config=DataValidationCofig(root_dir=config.root_dir,STATUS_FILE=config.STATUS_FILE,unzip_data_dir=config.unzip_data_dir,all_schema=schema)
        return data_validation_config
    
    def get_data_transformation(self)->DataTransformationConfig:
        config=self.config.data_transformation
        crate_directories([config.root_dir])
        data_transformation=DataTransformationConfig(root_dir=config.root_dir,data_path=config.data_path)
        return data_transformation
    
    def get_model_trainer_config(self)->ModelTrainerConfig:
        config=self.config.model_trianer
        params=self.params.ElasticNet
        schema=self.schema.TARGET_COLUMN
        crate_directories([config.root_dir])
        model_trainer_config=ModelTrainerConfig(root_dir=config.root_dir,train_data_path=config.train_data_path,test_data_path=config.test_data_path,
                                                model_name=config.model_name,alpha=params.alpha,l1_ratio=params.l1_ratio,target_column=schema.name)
        return model_trainer_config
    
    def get_model_evaluation_config(self)->ModelEvaluationConfig:
        config=self.config.model_evaluation
        params=self.params.ElasticNet
        schema=self.schema.TARGET_COLUMN
        crate_directories([config.root_dir])
        model_evaluation=ModelEvaluationConfig(root_dir=config.root_dir,test_data_path=config.test_data_path,model_path=config.model_path,
                                               all_params=params,metric_file_name=config.matric_file_name,target_column=schema.name)
        return model_evaluation