# API de Scoring de Dossiers de Sinistre

## Présentation
Cette API permet d'évaluer le risque d'un dossier de sinistre et retourne un **score** ainsi qu'une **décision** (Accepté / Analyse requise / Bloqué).

## Prérequis
- Python 3.10+
- Docker (si utilisation de Docker)
- Uvicorn (si lancement sans Docker)

## Lancer le projet pour tester


# Lancer le projet avec docker
```
docker build -t folder-api .
docker run -p 8000:8000 folder-api
```

# Lancer le projet sans docker
```
$ uvicorn backend:app --reload --port 8000
```
# Jeux de données de test

```
[
  {
    "identifiant_sinistre": "SIN-001",
    "type_sinistre": "Automobile",
    "montant_estime_euros": 300,
    "anciennete_contrat_mois": 36,
    "nombre_sinistres_anterieurs": 0,
    "age_assure": 45
  },
  {
    "identifiant_sinistre": "SIN-002",
    "type_sinistre": "Habitation",
    "montant_estime_euros": 1200,
    "anciennete_contrat_mois": 18,
    "nombre_sinistres_anterieurs": 1,
    "age_assure": 52
  },
  {
    "identifiant_sinistre": "SIN-003",
    "type_sinistre": "Responsabilité",
    "montant_estime_euros": 6500,
    "anciennete_contrat_mois": 4,
    "nombre_sinistres_anterieurs": 0,
    "age_assure": 33
  },
  {
    "identifiant_sinistre": "SIN-004",
    "type_sinistre": "Automobile",
    "montant_estime_euros": 2400,
    "anciennete_contrat_mois": 8,
    "nombre_sinistres_anterieurs": 2,
    "age_assure": 22
  },
  {
    "identifiant_sinistre": "SIN-005",
    "type_sinistre": "Habitation",
    "montant_estime_euros": 480,
    "anciennete_contrat_mois": 2,
    "nombre_sinistres_anterieurs": 3,
    "age_assure": 41
  },
  {
    "identifiant_sinistre": "SIN-006",
    "type_sinistre": "Responsabilité",
    "montant_estime_euros": 1800,
    "anciennete_contrat_mois": 60,
    "nombre_sinistres_anterieurs": 1,
    "age_assure": 74
  },
  {
    "identifiant_sinistre": "SIN-007",
    "type_sinistre": "Automobile",
    "montant_estime_euros": 5200,
    "anciennete_contrat_mois": 14,
    "nombre_sinistres_anterieurs": 0,
    "age_assure": 28
  },
  {
    "identifiant_sinistre": "SIN-008",
    "type_sinistre": "Habitation",
    "montant_estime_euros": 3200,
    "anciennete_contrat_mois": 5,
    "nombre_sinistres_anterieurs": 2,
    "age_assure": 67
  },
  {
    "identifiant_sinistre": "SIN-009",
    "type_sinistre": "Automobile",
    "montant_estime_euros": 800,
    "anciennete_contrat_mois": 3,
    "nombre_sinistres_anterieurs": 1,
    "age_assure": 19
  },
  {
    "identifiant_sinistre": "SIN-010",
    "type_sinistre": "Responsabilité",
    "montant_estime_euros": 400,
    "anciennete_contrat_mois": 30,
    "nombre_sinistres_anterieurs": 0,
    "age_assure": 38
  }
]

```