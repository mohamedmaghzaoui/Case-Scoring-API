from fastapi import FastAPI,HTTPException
from model import DisasterFolder
app = FastAPI()

folders_list = []

def calculate_score(folder: DisasterFolder):
 
    type_sinistre=folder.type_sinistre
    if type_sinistre=="Automobile":
        T=10
    elif type_sinistre=="Habitation":
        T=15
    else:
        T=20


    montant = folder.montant_estime_euros
    if montant < 500:
        M = 0
    elif montan< 2000:
        M = 10
    elif montant < 5000:
        M = 20
    else:
        M = 35

    anciennete = folder.anciennete_contrat_mois
    if anciennete < 6:
        A = 20
    elif anciennete < 24:
        A = 10
    else:
        A = 0

    S = {0:0, 1:10, 2:20}.get(folder.nombre_sinistres_anterieurs, 30)

    age = folder.age_assure
    if age < 25:
        G = 10
    elif age <= 70:
        G = 0
    else:
        G = 5

    score = max(0, min(100, T + M + A + S + G))

    if score < 35:
        decision = "Accepté"
    elif score < 70:
        decision = "Analyse requise"
    else:
        decision = "Bloqué"

    return {"score": score, "decision": decision}

@app.post("/folders/")
def evaluer_folder(folder: DisasterFolder):
   
   if(folder.type_sinistre not in ["Automobile", "Habitation", "Responsabilité"]):
        raise HTTPException(status_code=404, detail="invalid disaster type")
   
   result = calculate_score(folder) 
   folder.score = result["score"]
   folder.decision = result["decision"]
   folders_list.append(folder)  
   return {"identifiant_sinistre": folder.identifiant_sinistre, "score": folder.score, "decision":  folder.decision}


@app.get("/folders/{identifiant}")
def consult_folder(identifiant: str):
    for folder in folders_list:
        if folder.identifiant_sinistre == identifiant:
            return {"identifiant_sinistre": folder.identifiant_sinistre , "decision": folder.decision, "score": folder.score}
    raise HTTPException(status_code=404, detail="Dossier non trouvé")



@app.get("/health")
def health():
    return "l'applciation fonctionne"