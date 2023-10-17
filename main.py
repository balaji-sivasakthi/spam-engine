from fastapi import FastAPI
from pydantic import BaseModel
from service.mail_spam_checker import model, feature_extraction
import numpy as np
import pickle
from langdetect import detect
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
app = FastAPI()


# import sys
model_file = 'service/model.pkl'
pickled_model = pickle.load(open(model_file, 'rb'))

class RequestModel(BaseModel):
    raw_data:str


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/detect")
async def detectRoute(req:RequestModel):
    test = detect(req.raw_data)
    print(req.raw_data)
    if test == 'en' or test == 'ta':
        input_mail = [req.raw_data]
        # Convert Text to feature vectors
        input_data_feature = feature_extraction.transform(input_mail)
        prediction = pickled_model.predict(input_data_feature)
    
        # Making Prediction
        return {"result": prediction.tolist()[0]}
    else:
        return {"result":0}





