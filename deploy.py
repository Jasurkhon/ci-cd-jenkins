from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import numpy as np

app = FastAPI(title="My ML Model API", description="My ML Model API", version="1.0")

class InputDataModel(BaseModel):
    sepal_length: float = Field(default=5.1, description="Sepal length in cm")
    sepal_width: float = Field(default=3.5, description="Sepal width in cm")
    petal_length: float = Field(default=3.4, description="Petal length in cm")
    petal_width: float = Field(default=2.2, description="Petal width in cm")

class OutputDataModel(BaseModel):
    species: str
    probabilities: dict

@app.on_event("startup")
async def load_model():
    app.model = joblib.load("/app/model/model.joblib")
    app.species_mapping = {0: "setosa", 1: "versicolor", 2: "virginica"}

@app.get("/", status_code=200)
async def root():
    return {"message": "ML prediction API up & running."}

@app.post("/predict/", response_model=OutputDataModel)
async def predict_species(input: InputDataModel):
    features = np.array([[
        input.sepal_length,
        input.sepal_width,
        input.petal_length,
        input.petal_width
    ]])
    
    prediction_probs = app.model.predict_proba(features)[0]
    predicted_species = app.species_mapping[np.argmax(prediction_probs)]
    
    response_probs = {app.species_mapping[i]: round(prob, 2) for i, prob in enumerate(prediction_probs)}
    
    return {"species": predicted_species, "probabilities": response_probs}

