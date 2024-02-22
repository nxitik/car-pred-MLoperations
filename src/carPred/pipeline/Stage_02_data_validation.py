from carPred.config.configuration import ConfigurationManager
from carPred.components.data_validation import DataValidation
from carPred import logger

STAGE_NAME = "Data Validation stage"
class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()



if __name__ =="__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}.... started")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f"Completed {STAGE_NAME}.... completed")
    except Exception as e:
        logger.exception(e)
        raise e