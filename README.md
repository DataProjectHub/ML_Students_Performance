
# END TO END ML PROJECT -Student Performance Prediction – ML Web App

This project is a complete end-to-end machine learning pipeline designed to predict a student's math score based on various inputs such as gender, ethnicity, parental education level, lunch type, test preparation course, reading score, and writing score. The project is deployed as a web application using Flask and hosted on Render.

## Project Overview

The application takes input through a web form and returns the predicted math score using a trained regression model. It covers data ingestion, preprocessing, model training, and inference.

## Features

- Clean modular structure (components separated logically)
- Data ingestion and train/test split
- Data transformation using pipelines with handling of categorical and numerical features
- Model training using multiple regressors (Random Forest, XGBoost, CatBoost, etc.)
- Automatic model selection based on best R² score
- Persisted preprocessor and model using `dill`
- Flask-based web interface for real-time prediction
- Deployed on Render

## Project Structure
ML_PROJECTS/
├── artifacts/    # Holds model.pkl, preprocessor.pkl, etc.
├── logs/        # Stores log files
├── notebook/      # Likely has your data CSV
├── src/       # Source files (components, pipeline, utils)
    ├── components/ # Data ingestion, transformation, training 
    ├── pipeline/ # train_pipeline.py for full pipeline run
    ├── utils.py # Helper functions (save/load object, evaluation)
    ├── logger.py # Logging
    ├── exception.py # Custom exceptions
├── templates/     # HTML files for Flask
├── venv/        # Virtual environment (should be ignored)
├── application.py     # Flask app
├── requirements.txt   # contain all python dependencies
├── Procfile      # For Render deployment,specifies how to run the Flask app using Gunicorn
├── .gitignore
├── README.md
├── setup.py      # Can be used if you're packaging this as a module


## How It Works

1. **Data Ingestion**: Loads CSV data from `notebook/data/stud.csv` and splits it into train/test sets.
2. **Data Transformation**: Applies preprocessing pipeline including `SimpleImputer`, `StandardScaler`, and `OneHotEncoder` with `handle_unknown='ignore'`.
3. **Model Training**: Trains multiple models, performs hyperparameter tuning, selects the best model, and saves it.
4. **Prediction**: Loads the model and preprocessor, transforms incoming form data, and returns the predicted math score.

## How to Run Locally

1. Clone the repository:
git clone https://github.com/DataProjectHub/ML_Students_Performance.git 

2. Create a virtual environment:
python -m venv venv venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Run training pipeline (optional)
python src/pipeline/train_pipeline.py

5. Start the Flask server
python application.py

Visit `http://localhost:5000/predictdata` to use the form.

## Deployment

The app is deployed on Render. You can access it here:  
https://student-performance-deployment.onrender.com/predictdata

## Tech Stack

- Python
- Scikit-learn
- XGBoost
- CatBoost
- Flask
- HTML/CSS (Bootstrap)
- Render (for deployment)

## Credits

Project built and deployed by **Pooja Anilkumar** as part of learning full-cycle machine learning implementation and deployment.

Connect with me on [LinkedIn](https://www.linkedin.com/in/pooja-a-8b678637/)  
GitHub: [DataProjectHub](https://github.com/DataProjectHub/Student_Performance_Predictor)





