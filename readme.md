# 🧠 ML Classification App – Deployed with CI/CD, Docker, Kubernetes & GCP 🚀

This is a simple yet powerful machine learning classification project built with **scikit-learn** and served via **Streamlit**. It comes with an automated deployment pipeline using **GitHub Actions**, containerized with **Docker**, orchestrated with **Kubernetes**, and deployed to **Google Cloud Platform (GKE)**. Yeah, it’s basically a full-stack DevOps beast in disguise.

---

## ⚙️ Tech Stack

- **Frontend**: Streamlit (Python)
- **ML Backend**: scikit-learn
- **DevOps**: GitHub Actions, Docker, Kubernetes
- **Cloud**: Google Cloud Platform (GKE + Artifact Registry)
- **Model Tracking**: MLflow (locally tested)

---

## 📂 Folder Structure

```
.
├── app/
│   └── app.py                  # Streamlit frontend
├── data/
│   └── processed/train.csv     # Preprocessed data
├── models/
│   └── model.pkl               # Trained ML model
├── scripts/
│   └── training.py             # Model training script
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Container config
├── deployment.yaml            # K8s deployment
├── service.yaml               # K8s service (LoadBalancer)
├── .github/
│   └── workflows/cicd.yml     # GitHub Actions pipeline
└── README.md                  # This file
```

---

## 🚀 Deployment Flow

1. **Code pushed to `main` branch**
2. **GitHub Actions** kicks in:
   - Authenticates with GCP via service account key
   - Builds Docker image
   - Pushes to **GCP Artifact Registry**
   - Deploys to **GKE cluster**
3. App becomes available publicly through a **LoadBalancer** IP

---

## 🐳 Docker Build

```bash
docker build -t streamlit-ml-app .
docker run -p 8080:8080 streamlit-ml-app
```

---

## ☸️ Kubernetes Deploy

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

To get external IP:
```bash
kubectl get service
```

---

## 🔬 Model Training

Training is done via `scripts/training.py`. Preprocessed data is saved under `data/processed/`, and trained model is saved as `models/model.pkl`.

---

## 🔥 GitHub Actions Workflow (`cicd.yml`)

Handles the build and deploy automatically on each push to `main`.

---

## 📦 Requirements

```txt
scikit-learn
pandas
streamlit
joblib
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 🎯 Future Improvements

- Add MLflow tracking in production
- Add automated tests in CI
- Hook up retraining triggers for new data
- Add proper error handling in Streamlit

---

## 🤖 Credits

Built by Yash Suthar, a guy who trained, deployed, and DevOps'd a full ML pipeline in one day — and still had time for sarcasm and paneer 🍽️.
