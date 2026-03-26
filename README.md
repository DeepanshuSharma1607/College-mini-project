# 🎓 AI-Based Student Performance Analyzer

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.132.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Latest-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-Deployed-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)

**An end-to-end Machine Learning system that predicts student CGPA and identifies at-risk students before it's too late.**

[Features](#-features) • [Demo](#-api-demo) • [Installation](#-installation) • [Usage](#-usage) • [API Docs](#-api-reference) • [Model Performance](#-model-performance) • [Project Structure](#-project-structure)

</div>

---

## 📌 Overview

Schools and universities often detect underperforming students only at the end of a semester — when it's already too late for effective intervention. This project solves that problem.

The **AI-Based Student Performance Analyzer** uses Ridge Regression Machine Learning models trained on 3,046 real student academic records to **predict a student's CGPA for Year 2, Year 3, or Year 4** based on their current academic data. The system automatically classifies each student into a **risk tier** and returns a real-time **advisory suggestion** — giving faculty the insights they need to intervene early.

The solution is fully productionized: trained models are served via a **FastAPI REST API**, containerized with **Docker**, and was deployed on **Amazon Web Services (AWS)**.

---

## ✨ Features

- 🔮 **Year-wise CGPA Prediction** — Three independent models for Year 2, Year 3, and Year 4
- ⚠️ **Risk Classification** — Automatically classifies students as High Risk, Low Risk, or No Risk
- 💬 **Actionable Suggestions** — Returns faculty advisory messages alongside every prediction
- ✅ **Strict Input Validation** — Pydantic v2 rejects invalid inputs before they reach the model
- 🚀 **Production-Ready API** — FastAPI with auto-generated Swagger UI at `/docs`
- 🐳 **Dockerized** — Single command to run anywhere
- ☁️ **Cloud Deployed** — AWS-ready containerized deployment

---

## 🧠 How It Works

The system operates in two phases:

**Offline — Training Phase**
```
CSV Dataset → EDA & Preprocessing → Feature Engineering (by year) → RidgeCV Pipeline → .pkl Model Files
```

**Online — Inference Phase**
```
API Request → Pydantic Validation → Load Model → Predict CGPA → Compute Risk → Return JSON Response
```

### Risk Classification Logic

| SGPA Range | Risk Level | Advisory Message |
|---|---|---|
| < 1.5 | 🔴 High Risk | Increase study time and attendance — you are at high risk |
| 1.5 – 3.5 | 🟡 Low Risk | You are doing OK but need more focus — you are at low risk |
| > 3.5 | 🟢 No Risk | You are doing well — no risk |

> **SGPA** is automatically computed from the submitted CGPA values — no extra input needed.

---

## 📊 Model Performance

Three separate **Ridge Regression (RidgeCV)** models were trained — one per academic year. Features grow progressively as students advance through their degree.

| Model | Target | R² Score | MAE | RMSE |
|---|---|---|---|---|
| Year 2 | CGPA200 | 0.6556 | 0.3701 | 0.4586 |
| Year 3 | CGPA300 | 0.7411 | 0.3611 | 0.4524 |
| Year 4 | CGPA400 | **0.7424** | **0.3474** | **0.4246** |

**Feature sets used per model:**

| Year | Input Features | Target |
|---|---|---|
| Year 2 | Gender, CGPA100, attendance, study_hours | CGPA200 |
| Year 3 | Gender, CGPA100, CGPA200, attendance, study_hours | CGPA300 |
| Year 4 | Gender, CGPA100, CGPA200, CGPA300, attendance, study_hours | CGPA400 |

### Why Ridge Regression?
- Target variable (CGPA) is **continuous** → regression is the right approach
- **L2 regularization** prevents overfitting when year-wise CGPAs are naturally correlated
- **RidgeCV** auto-selects optimal alpha from `[0.01, 0.1, 1, 10, 100]` via cross-validation
- Fast, interpretable, and generalizes well on this dataset size

---

## 📂 Project Structure

```
College-mini-project/
│
├── 📁 api_folder/                              # Production API — Dockerized FastAPI service
│   ├── 📁 model/                               # Trained .pkl model files served by the API
│   │   ├── model_year_2.pkl                    # Ridge Regression model — Year 2 prediction
│   │   ├── model_year_3.pkl                    # Ridge Regression model — Year 3 prediction
│   │   └── model_year_4.pkl                    # Ridge Regression model — Year 4 prediction
│   ├── 📁 Schema/                              # Pydantic schema modules
│   │   ├── user_input.py                       # Student input model (validation + computed fields)
│   │   └── predicted_response.py               # API response schema
│   ├── api.py                                  # FastAPI app — routes, CORS, prediction endpoint
│   ├── Dockerfile                              # Container definition (Python 3.13 + Uvicorn)
│   └── requirements.txt                        # API dependencies
│
├── 📁 student_prediction/                      # ML training — notebook + dataset + models
│   ├── project_1.ipynb                         # Full EDA, preprocessing, training & evaluation
│   ├── updated_dataset.csv                     # Raw academic dataset (3,046 student records)
│   ├── model_year_2.pkl                        # Saved trained model — Year 2
│   ├── model_year_3.pkl                        # Saved trained model — Year 3
│   ├── model_year_4.pkl                        # Saved trained model — Year 4
│   └── api.py                                  # Standalone prediction script (dev/testing)
│
├── 📁 student_prediction_frontend/             # Streamlit frontend UI
│   ├── frontend.py                             # Streamlit app (connects to FastAPI backend)
│   └── requirements.txt                        # Frontend dependencies (streamlit, requests...)
│
└── README.md
```

### Folder Responsibilities

| Folder | Purpose |
|---|---|
| `api_folder/` | The production-ready Dockerized FastAPI service — this is what gets deployed to AWS |
| `student_prediction/` | All ML work — EDA, model training, evaluation notebook and the trained `.pkl` files |
| `student_prediction_frontend/` | Streamlit UI that connects to the API and provides an interface for faculty |

---

## ⚙️ Installation

### Prerequisites
- Python 3.10+
- Docker (optional, for containerized run)
- Trained model `.pkl` files in the `model/` directory

### Option 1 — Run the API Locally

```bash
# 1. Clone the repository
git clone https://github.com/DeepanshuSharma1607/College-mini-project.git
cd College-mini-project/api_folder

# 2. Install API dependencies
pip install -r requirements.txt

# 3. Start the API server
uvicorn api:app --host 0.0.0.0 --port 8000 --reload
```

### Option 2 — Run the Frontend Locally

```bash
# In a separate terminal
cd College-mini-project/student_prediction_frontend

# Install frontend dependencies
pip install -r requirements.txt

# Start the Streamlit UI
streamlit run frontend.py
```

> Make sure the API server (Option 1) is running before launching the frontend.

### Option 3 — Run the API with Docker

```bash
# Navigate to the api_folder
cd College-mini-project/api_folder

# Build the Docker image
docker build -t student-predictor .

# Run the container
docker run -p 8000:8000 student-predictor
```

The API will be live at **`http://localhost:8000`**

Interactive docs available at **`http://localhost:8000/docs`**

---

## 🚀 Usage

### Quick Test with curl

**Predict Year 4 CGPA:**
```bash
curl -X POST "http://localhost:8000/predict?year=4" \
  -H "Content-Type: application/json" \
  -d '{
    "Gender": "Female",
    "CGPA100": 3.85,
    "CGPA200": 3.60,
    "CGPA300": 3.72,
    "attendance": 88.5,
    "study_hours": 5.5
  }'
```

**Response:**
```json
{
  "predicted_cgpa": 3.74,
  "current_avg_cgpa": 3.72,
  "status": "YOU ARE DOING WELL NO RISK",
  "model_loaded": "1.0.0"
}
```

**Predict Year 2 CGPA (only first year data needed):**
```bash
curl -X POST "http://localhost:8000/predict?year=2" \
  -H "Content-Type: application/json" \
  -d '{
    "Gender": "Male",
    "CGPA100": 2.40,
    "attendance": 63.0,
    "study_hours": 1.5
  }'
```

**Response:**
```json
{
  "predicted_cgpa": 2.15,
  "current_avg_cgpa": 2.40,
  "status": "YOU ARE DOING OK BUT NEED MORE FOCUS YOU ARE AT LOW RISK",
  "model_loaded": "1.0.0"
}
```

---

## 📡 API Reference

### `POST /predict`

Predict a student's upcoming year CGPA and receive a risk classification.

**Query Parameter**

| Parameter | Type | Required | Description |
|---|---|---|---|
| `year` | `int` | ✅ | Academic year to predict for. Must be `2`, `3`, or `4` |

**Request Body**

| Field | Type | Required | Constraints |
|---|---|---|---|
| `Gender` | `string` | ✅ | `"Male"`, `"Female"`, or `"Other"` |
| `CGPA100` | `float` | ✅ | `0 < value < 5` |
| `CGPA200` | `float` | For year 3 & 4 | `0 < value < 5` |
| `CGPA300` | `float` | For year 4 only | `0 < value < 5` |
| `attendance` | `float` | ✅ | `0 < value < 100` |
| `study_hours` | `float` | ✅ | `0 < value < 12` |

**Response Body**

| Field | Type | Description |
|---|---|---|
| `predicted_cgpa` | `float` | Model's predicted CGPA for the target year |
| `current_avg_cgpa` | `float` | Student's running average CGPA from submitted data |
| `status` | `string` | Risk level and advisory message |
| `model_loaded` | `string` | Model version used for prediction |

**Error Responses**

| Status | Reason |
|---|---|
| `400` | Invalid year (not 2, 3, or 4) or model file not found |
| `422` | Input validation failed (invalid field values) |
| `500` | Internal prediction error |

---

## 🏗️ Training Your Own Models

To retrain the models from scratch using your own dataset:

```bash
# Navigate to the training folder
cd College-mini-project/student_prediction

# Run the training notebook
jupyter notebook project_1.ipynb
```

Or run the training script directly — the key pipeline steps are:

```python
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import RidgeCV
import joblib

# Preprocessing pipeline
preprocessing = make_column_transformer(
    (OneHotEncoder(sparse_output=False, handle_unknown='ignore'), ['Gender']),
    (StandardScaler(), numeric_features),
    remainder='drop'
)

# Model pipeline
pipe = make_pipeline(
    preprocessing,
    RidgeCV(alphas=[0.01, 0.1, 1, 10, 100])
)

# Train and save
pipe.fit(X_train, y_train)
joblib.dump(pipe, f"model_year_{year}.pkl")  # saved in student_prediction/
```

---

## 🐳 Docker Details

**Dockerfile overview:**
```dockerfile
FROM python:3.13
WORKDIR /api
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Useful Docker commands:**
```bash
# Build
docker build -t student-predictor .

# Run in background
docker run -d -p 8000:8000 --name sp-api student-predictor

# View logs
docker logs sp-api

# Stop
docker stop sp-api
```

---

## ☁️ AWS Deployment

The application was deployed on AWS using the following workflow:

```bash
# 1. Build and tag image
docker build -t student-predictor .
docker tag student-predictor:latest <aws-account-id>.dkr.ecr.<region>.amazonaws.com/student-predictor:latest

# 2. Push to AWS ECR
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <ecr-uri>
docker push <ecr-uri>/student-predictor:latest

# 3. Deploy on EC2 / ECS
# Pull the image and run with docker run -p 8000:8000
```

> **Note:** The AWS deployment is currently offline. It was used for live demonstration purposes.

---

## 📦 Dependencies

```txt
fastapi==0.132.0
uvicorn[standard]
joblib==1.5.2
scikit-learn
pandas==3.0.1
pydantic==2.12.5
```

---

## 🗂️ Dataset

The model was trained on a structured academic dataset (`updated_dataset.csv`) with the following characteristics:

| Property | Value |
|---|---|
| Total Records | 3,046 student entries |
| Features | Gender, CGPA100–400, SGPA, attendance, study_hours |
| Year of Graduation | 2010 – 2014 |
| Programs | Multiple (BCH, ICE, EEE, CHM, CEN, PHYE, PHYG, ...) |
| Missing Values | None |
| Mean CGPA | 3.49 / 5.0 |
| Mean Attendance | 84.66% |
| Mean Study Hours | 4.59 hrs/day |

> The dataset is not included in this repository. Place `updated_dataset.csv` in the root directory before running the training notebook.

---

## 🔭 Future Improvements

- [ ] Frontend dashboard (React / Flutter) for faculty visualization
- [ ] SHAP explainability for per-student feature importance
- [ ] Automated model retraining pipeline (MLflow / Airflow)
- [ ] AWS SNS alerts when students cross into High Risk
- [ ] LMS integration (Moodle, Canvas)
- [ ] Support for behavioral and psychological input factors
- [ ] Multi-institutional multi-tenancy support

---
>
