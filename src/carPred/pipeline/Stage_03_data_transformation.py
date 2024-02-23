from carPred.config.configuration import ConfigurationManager
from carPred.components.data_transformation import DataTransformation
from carPred import logger
from pathlib import Path

STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.json"),"r") as f:
                status = f.read().split(" ")[-1]
            if status =="True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()

            else:
                raise Exception("Data Validation failed")
            
        except Exception as e:
            print(e)

if __name__ =="__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}.... started")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f"Completed {STAGE_NAME}.... completed")
    except Exception as e:
        logger.exception(e)
        raise e