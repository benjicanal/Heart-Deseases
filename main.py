from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Charger le modèle
model = joblib.load('heart_disease_model.pkl')

# Initialiser FastAPI
app = FastAPI()

# Créer une classe pour le modèle de données d'entrée
class HeartData(BaseModel):
    features: list

# Définir une route pour les prédictions
@app.post('/predict')
def predict(data: HeartData):
    # Convertir les données en tableau numpy
    input_data = np.array([data.features])
    
    # Faire la prédiction
    prediction = model.predict(input_data)
    
    # Retourner la prédiction
    return {"prediction": int(prediction[0])}
