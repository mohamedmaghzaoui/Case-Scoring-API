from pydantic import BaseModel


class DisasterFolder(BaseModel):
    identifiant_sinistre: str
    type_sinistre: str
    montant_estime_euros: float
    anciennete_contrat_mois: int
    nombre_sinistres_anterieurs: int
    age_assure: int

