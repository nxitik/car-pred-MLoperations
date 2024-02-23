from carPred import logger
from carPred.pipeline.Stage_01_data_ingestion import DataIngestionTrainingPipeline
from carPred.pipeline.Stage_02_data_validation import DataValidationTrainingPipeline
from carPred.pipeline.Stage_03_data_transformation import DataTransformationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f"Starting {STAGE_NAME}.... started")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"Completed {STAGE_NAME}.... completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f"Starting {STAGE_NAME}.... started")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f"Completed {STAGE_NAME}.... completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f"Starting {STAGE_NAME}.... started")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f"Completed {STAGE_NAME}.... completed")
except Exception as e:
    logger.exception(e)
    raise e