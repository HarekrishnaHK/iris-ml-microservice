
```markdown
# 🧠 ML Pipeline with Flask, Kafka, gRPC, and SQLite

This project demonstrates a Machine Learning pipeline using:
- Flask API for receiving prediction input
- Kafka for message streaming
- gRPC microservice for saving results
- SQLite for persistent storage
- Classification and Regression ML models (Iris dataset)

## 📌 Project Structure

```

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

```

---

## 🚀 Setup Instructions
```
## 1. 🔧 Install Requirements

```bash
pip install flask joblib scikit-learn confluent-kafka grpcio grpcio-tools
````
```
### 2. ⚙️ Start Kafka (using Confluent CLI)

```bash
confluent local kafka start
confluent local kafka topic create manage
```

---

### 3. 📡 Run gRPC Server

```bash
python store_server.py
```

---

### 4. 🧪 Run Subscribers (in separate terminals)

 **Classification Subscriber**

```bash
python subscriber1.py
```

 **Regression Subscriber**

```bash
python subscriber2.py
```

---

### 5. 🌐 Run Flask API (Publisher)

```bash
python server.py
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
```

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
🎓 B.Tech CSE (Data Science) | The Neotia University
🧠 Focus: ML, Deep Learning, Microservices
📫 *Drop a message if you'd like to collaborate!*
---