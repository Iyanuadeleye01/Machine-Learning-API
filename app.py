import fastapi
from pydantic import BaseModel
import uvicorn
import joblib
import pandas as pd

# Create an instance of fastapi
app = fastapi.FastAPI()


class SepsisInput(BaseModel):
    Plasma_glucose: float
    Blood_Work_Result1: float
    Blood_Pressure: float
    Blood_Work_Result2: float 
    Blood_Work_Result3: float 
    Body_mass_index: float
    Blood_Work_Result4: float 
    Age: float 
    Insurance: float

# Load the models
gradient_boosting = joblib.load("./models/gradientboosting_model.joblib")
encoder = joblib.load("./models/label_encoder.joblib")
naive_bayes = joblib.load("./models/naive_bayes_model.joblib")  
xgboost = joblib.load("./models/xgboost_model.joblib")

@app.get('/')
def home():
    return {'status': 'ok'}

# API endpoint for Gradient Boosting model
@app.post('/gradient_boosting_predict')  
async def gradient_boosting_predict(data: SepsisInput):
    try:
        # Convert data into a DataFrame
        df = pd.DataFrame([data.dict()])

        # Make prediction with the Gradient Boosting model
        gradient_prediction = gradient_boosting.predict(df)

        # Decode the prediction
        gradient_prediction = encoder.inverse_transform([gradient_prediction])[0]

        # Predict the probability 
        gradient_probability = gradient_boosting.predict_proba(df)

        # Convert probability array to a list
        gradient_probabilities = gradient_probability.tolist()

        return {'gradient_prediction': gradient_prediction, 'gradient_probabilities': gradient_probabilities}
    
    except Exception as e:
        return {'error': str(e)}

# API endpoint for Naive Bayes model
@app.post('/naive_bayes_predict')
async def naive_bayes_predict(data: SepsisInput):
    try:
        # Convert data into a DataFrame
        df = pd.DataFrame([data.dict()])

        # Make prediction with the Naive Bayes model
        naive_prediction = naive_bayes.predict(df)

        # Decode the prediction
        naive_prediction = encoder.inverse_transform([naive_prediction])[0]

        # Predict the probability for Naive Bayes model
        naive_probability = naive_bayes.predict_proba(df)

        # Convert the probability array to a list
        naive_probabilities = naive_probability.tolist()

        return {'naive_prediction': naive_prediction, 'naive_probabilities': naive_probabilities}
    
    except Exception as e:
        return {'error': str(e)}
    
# API endpoint for XGBoost model
@app.post('/xgboost_predict')
async def xgboost_predict(data:SepsisInput):
    try:
        # Convert the data into a dataframe
        df = pd.DataFrame([data.dict()])

        # Make prediction with the df
        xgboost_prediction = xgboost.predict(df)

        # Decode with encoder
        xgboost_prediction = encoder.inverse_transform([xgboost_prediction])[0]

        # Probability prediction
        xgboost_probability = xgboost.predict_proba(df)

        # Convert the prob numpy array to a list
        xgboost_probabilities = xgboost_probability.tolist()

        return {'xgboost_prediction':xgboost_prediction, 'xgboost_probabilities':xgboost_probabilities}
    
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8001, debug=True)





# @app.get('/')
# def home():
#     return{'status': 'ok'}

# # Create API endpoint for Gradientboosting model

# @app.post('/gradient_boosting_predict')
# async def gradient_boosting_predict(data:Sepsisinput):
#     try:

#         # Convert the data into a dataframe and a dictionary
#         df = pd.DataFrame([data.model_dump()])

#         # Make a prediction with the gradient boosting model
#         prediction = gradient_boosting.predict(df)

#         # Convert the prediction into an integer instead of an array and take the first index value
#         prediction = int(prediction[0])

#         # Use encoder to decode the data
#         prediction = encoder.inverse_transform([prediction])[0]

#         # Predict the probability 

#         probability = gradient_boosting.predict_proba(df)

#         # Covert the probability numpy array to a list
#         probabilities = probability.tolist()

#         return {'prediction':prediction, 'probabilities':probabilities}
#     except Exception as e:
#         return {'error': str(e)}

# # Create API endpoint for Naive Bayes model

# @app.post('/naive_bayes_predict')
# async def naive_bayes_predict(data:Sepsisinput):
#     try:
#         df = pd.DataFrame([data.model_dump()])

#         naive_prediction = naive_bayes.predict(df)

#         naive_prediction = int(naive_prediction[0])

#         # Decode the data
#         naive_prediction = encoder.inverse_transform(df)

#         # Predict the probability for naive bayes model
#         naive_probability = naive_bayes.predict_proba(df)

#         # Convert the probability in an array to a list
#         naive_probabilities = naive_probability.tolist()

#         return {'naive_prediction':naive_prediction, 'naive_probabilities':naive_probabilities}
    
#     except Exception as e:
#         return {'error':str(e)}






# if __file__ == '__main__':
#     uvicorn(app, host="0.0.0", port="8001", debug=True)


