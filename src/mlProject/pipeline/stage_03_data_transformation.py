from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTrnsformation
from mlProject import logger
from pathlib import Path

STAGE_NAME="Data Transformation stage"
class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            with open(Path('artifacts/data_validation/status.txt'),"r") as f:
                status=f.read().split(" ")[-1]
                logger.info(f"the data validation status is {status}")
                if status=="True":
                    config=ConfigurationManager()
                    data_transformation_config=config.get_data_transformation()
                    data_transformation=DataTrnsformation(config=data_transformation_config)
                    data_transformation.train_test_split()
                else:
                    raise Exception("your data schema is not valid")
        except Exception as e:
            print(e)
