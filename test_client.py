import requests

# URL de l'API
url = "http://127.0.0.1:8000/predict"

# Les données à envoyer
data = {
    "features": [
    52,1,0,125,212,0,1,168,0,1.0,2,2,3
  ]
}

# Envoyer la requête POST
response = requests.post(url, json=data)

# Récupérer la réponse en JSON
result = response.json()

# Interpréter la prédiction
if result["prediction"] == 1:
    print("La personne est prédite comme ayant une maladie cardiaque.")
else:
    print("La personne est prédite comme n'ayant pas de maladie cardiaque.")
