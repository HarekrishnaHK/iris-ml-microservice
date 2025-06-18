# 🧠 ML Pipeline with Flask, Kafka, gRPC, and SQLite

This project demonstrates a Machine Learning pipeline using:
- **Flask API** for receiving prediction input
- **Kafka** for message streaming
- **gRPC microservice** for saving results
- **SQLite** for persistent storage
- **Classification** and **Regression** ML models (Iris dataset)



## 📌 Project Structure



ml\_pipeline/
├── flask\_api.py              # Input validation + Kafka publisher
├── publisher.py              # Standalone Kafka message publisher
├── subscriber1.py            # Kafka subscriber for classification
├── subscriber2.py            # Kafka subscriber for regression
├── models/
│   ├── iris\_logistic\_model.pkl
│   ├── iris\_regression\_model.pkl
│   └── iris\_label\_encoder.pkl
├── grpc/
│   ├── store.proto           # gRPC service definition
│   ├── store\_pb2.py          # Generated gRPC classes
│   ├── store\_pb2\_grpc.py
│   ├── store\_server.py       # gRPC server
│   └── store\_client.py       # Client to send gRPC requests
├── store\_results.db          # SQLite database
└── init\_db.py                # DB setup script



🚀 Setup Instructions

1. 🔧 Install Requirements


pip install flask joblib scikit-learn confluent-kafka grpcio grpcio-tools

2. ⚙️ Start Kafka (using Confluent CLI)


confluent local services start
confluent local kafka topic create manage

3. 📡 Run gRPC Server

```bash
python grpc/store_server.py
```

---

### 4. 🧪 Run Subscribers (in separate terminals)

* **Classification Subscriber**

```bash
python subscriber1.py
```

* **Regression Subscriber**

```bash
python subscriber2.py
```

---

### 5. 🌐 Run Flask API (Publisher)

```bash
python flask_api.py
```

Then send a POST request:

```json
POST http://127.0.0.1:5001/predict

{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}


✅ This triggers Kafka publishing → subscribers → gRPC calls → database insertion.

---

## 🗃️ Database Tables

The SQLite database `store_results.db` has two tables:

### classification

| id | model\_name      | features                | predicted\_label |
| -- | ---------------- | ----------------------- | ---------------- |
| 1  | iris\_classifier | "\[5.1, 3.5, 1.4, 0.2]" | setosa           |

### regression

| id | model\_name     | features           | predicted\_value |
| -- | --------------- | ------------------ | ---------------- |
| 1  | iris\_regressor | "\[5.1, 3.5, 1.4]" | 0.2095           |

---

## 📦 Proto Definition

```proto
// store.proto

service StoreService {
  rpc SaveRegress (RegressRequest) returns (RegressResponse);
  rpc SaveClassify (ClassifyRequest) returns (ClassifyResponse);
}

message RegressRequest {
  string model_name = 1;
  string features = 2;
  float predicted_value = 3;
}

message RegressResponse {
  string status = 1;
}

message ClassifyRequest {
  string model_name = 1;
  string features = 2;
  string predicted_label = 3;
}

message ClassifyResponse {
  string status = 1;
}
```

---

## 💡 Features

* ✅ Real-time classification & regression
* ✅ Kafka for stream-based processing
* ✅ gRPC microservices for clean architecture
* ✅ SQLite for easy result persistence
* ✅ Input validation and preprocessing

---

## 📚 Future Improvements

* Add Docker support for full deployment
* Add authentication to the gRPC service
* Switch to PostgreSQL or MySQL for production use

---

## 👨‍💻 Author

**Harekrishna Adhikary**
B.Tech in CSE (Data Science)
[The Neotia University]







Here's a **beautifully designed and unique** `README.md` using **modern markdown**, emojis, icons, and a visually structured layout to stand out:

---

```markdown
<h1 align="center">🚀 ML Streaming Pipeline</h1>
<h3 align="center">Flask API + Kafka + gRPC + SQLite + Machine Learning</h3>

<p align="center">
  <img src="https://img.shields.io/badge/ML-Classification%20%26%20Regression-brightgreen" />
  <img src="https://img.shields.io/badge/Streaming-Kafka-blue" />
  <img src="https://img.shields.io/badge/API-Flask-orange" />
  <img src="https://img.shields.io/badge/gRPC-Service-lightgrey" />
  <img src="https://img.shields.io/badge/Database-SQLite-purple" />
</p>

---

## 🧩 Overview

A modular Machine Learning microservice system featuring:

✨ **Flask** for input API  
📡 **Kafka** for real-time message passing  
🔌 **gRPC** service for storing results  
📈 **ML Models** (Classification & Regression)  
🛢️ **SQLite DB** for persistent storage

---

## 📂 Project Layout

```

ml\_pipeline/
│
├── flask\_api.py               → Input validation & Kafka publisher
├── subscriber1.py             → Classification consumer
├── subscriber2.py             → Regression consumer
├── publisher.py               → Sample Kafka publisher
│
├── models/
│   ├── iris\_logistic\_model.pkl
│   ├── iris\_regression\_model.pkl
│   └── iris\_label\_encoder.pkl
│
├── grpc/
│   ├── store.proto
│   ├── store\_pb2.py
│   ├── store\_pb2\_grpc.py
│   ├── store\_server.py        → gRPC server
│   └── store\_client.py        → gRPC client
│
├── init\_db.py                 → SQLite DB table setup
└── store\_results.db           → Local database

````

---

## 🔧 Setup Guide

### 🐍 Install Dependencies
```bash
pip install flask joblib scikit-learn confluent-kafka grpcio grpcio-tools
````

### 🧱 Start Kafka Broker (Confluent CLI)

```bash
confluent local services start
confluent local kafka topic create manage
```

---

## ▶️ Run The Services

> Open **separate terminals** for each step below 👇

### 1️⃣ gRPC Server

```bash
python grpc/store_server.py
```

### 2️⃣ Subscribers

* **Classification**

  ```bash
  python subscriber1.py
  ```

* **Regression**

  ```bash
  python subscriber2.py
  ```

### 3️⃣ Flask API

```bash
python flask_api.py
```

Then, send a POST request using Postman or `curl`:

```json
POST http://127.0.0.1:5001/predict

{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

---

## 🧠 ML Model Info

| Type           | Model               | Features Used                   | Output                   |
| -------------- | ------------------- | ------------------------------- | ------------------------ |
| Classification | Logistic Regression | All 4 features                  | Iris species (label)     |
| Regression     | Linear Regression   | 3 features (sepal/petal length) | Predicted numeric target |

---

## 🗃️ Database Schema

> SQLite database `store_results.db` will be automatically populated.

**Table: `classification`**

| id | model\_name      | features                | predicted\_label |
| -- | ---------------- | ----------------------- | ---------------- |
| 1  | iris\_classifier | "\[5.1, 3.5, 1.4, 0.2]" | setosa           |

**Table: `regression`**

| id | model\_name     | features           | predicted\_value |
| -- | --------------- | ------------------ | ---------------- |
| 1  | iris\_regressor | "\[5.1, 3.5, 1.4]" | 0.2095           |

---

## 📡 gRPC Proto File

```proto
service StoreService {
  rpc SaveRegress (RegressRequest) returns (RegressResponse);
  rpc SaveClassify (ClassifyRequest) returns (ClassifyResponse);
}

message RegressRequest {
  string model_name = 1;
  string features = 2;
  float predicted_value = 3;
}

message ClassifyRequest {
  string model_name = 1;
  string features = 2;
  string predicted_label = 3;
}
```

---

## 🧪 Sample Kafka Publisher (Optional)

```bash
python publisher.py
```

---

## 💡 Future Ideas

* 🐳 Dockerize all components
* 🛡 Add gRPC authentication
* 📊 Add Grafana + Prometheus monitoring
* 🧪 Integrate unit testing and logging

---

## 👨‍💻 Author

**Harekrishna Adhikary**
🎓 B.Tech CSE (Data Science) | The Neotia University
🧠 Focus: ML, Deep Learning, Microservices
📫 *Drop a message if you'd like to collaborate!*

---

> Made with ❤️ and Python
