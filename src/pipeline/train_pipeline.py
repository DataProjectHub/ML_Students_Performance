# all the code for training pipeline and trigger/call all the components.
#Run your entire ML pipeline (ingestion → transformation → training) from a single script
import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.exception import CustomException

if __name__ == "__main__":
    try:
        print("Starting Training Pipeline...")

        # 1. Data Ingestion
        ingestion = DataIngestion()
        train_path, test_path = ingestion.initiate_data_ingestion()
        print("Data Ingestion Completed")

        # 2. Data Transformation
        transformer = DataTransformation()
        train_arr, test_arr, _ = transformer.initiate_data_transformation(train_path, test_path)
        print("Data Transformation Completed")

        # 3. Model Training
        trainer = ModelTrainer()
        score = trainer.initiate_model_trainer(train_arr, test_arr)
        print(f"Model Training Completed. R² Score: {score:.4f}")

    except Exception as e:
        raise CustomException(e, sys)
