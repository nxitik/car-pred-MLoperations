from carPred.config.configuration import ConfigurationManager
from carPred.components.model_evaluation import ModelEvaluation
from carPred import logger
from pathlib import Path

STAGE_NAME ="Model Evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config)
        model_evaluation.log_into_mlflow()
    
if __name__ =="__main__":
    try:
        logger.info(f"Starting {STAGE_NAME}.... started")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f"Completed {STAGE_NAME}.... completed")
    except Exception as e:
        logger.exception(e)
        raise e