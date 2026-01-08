# telco-churn-pipeline

Pipeline voor een Telco Customer Churn **Machine Learning** casus (Data Engineering – LU2).

Doel: een reproduceerbare flow van **data → training/evaluatie → model serving (API) → UI/prototype**.

Repo: https://github.com/simonklaren/telco-churn-pipeline

---

## Repo-structuur

- `data/`  
  Input data (raw/processed) en/of voorbeelden.
- `notebooks/`  
  Training, EDA, feature engineering, modelvergelijking, evaluatie, export van het model.
- `ml_service/`  
  Model serving laag (API). Hier laad je het getrainde model/pipeline en expose je endpoints voor predict/health.
- `deploy.sh`  
  Helper script voor deployment/updates (lokaal of op device/server).

---

## Quickstart (lokaal)

### 1) Repo clonen
`git clone https://github.com/simonklaren/telco-churn-pipeline.git`

`cd telco-churn-pipeline`

2) Notebook draaien
Open notebooks/ in Jupyter / VSCode en run de training flow.
Zorg dat het model artifact dat de API gebruikt gegenereerd is (bijv. een .pkl/.joblib/pipeline bestand).
(Er staat al een getrained model in ml_service/models)

4) API starten
Ga naar ml_service/ en start de service (hoe precies hangt af van je setup: venv/Docker).
Doel: een endpoint waar je een predict-call tegenaan kunt doen.

Voorbeeld request (JSON):

`
{
  "tenure": 12,
  "Contract": "Month-to-month",
  "MonthlyCharges": 79.85,
  "TotalCharges": 958.2,
  "...": "..."
}
`

Voorbeeld response (concept):

`
{
  "churn": true,
  "probability": 0.73,
  "model_version": "v1"
}
`

## Deployment notes

  - deploy.sh is bedoeld om het uitrollen simpeler te maken (pull + build/restart).


## License
MIT (zie LICENSE).
