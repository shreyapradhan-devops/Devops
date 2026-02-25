DevOps Dashboard is a cloud-native full-stack application deployed on AWS EC2 using Docker and Kubernetes.

This project demonstrates:

Containerization of frontend and backend services

Kubernetes orchestration (Deployments & Services)

Public exposure via NodePort

Docker Hub image management

Cloud networking & security configuration

Cross-origin communication handling (CORS)

The system is deployed on an AWS Free Tier EC2 instance and is accessible publicly via NodePort services.

🏗 System Architecture
                        ┌────────────────────┐
                        │     Web Browser    │
                        └──────────┬─────────┘
                                   │
                                   ▼
                     ┌─────────────────────────┐
                     │ Frontend Service        │
                     │ NodePort :30007         │
                     └──────────┬──────────────┘
                                │
                                ▼
                     ┌─────────────────────────┐
                     │ Frontend Pod (Nginx)    │
                     └──────────┬──────────────┘
                                │ HTTP Request
                                ▼
                     ┌─────────────────────────┐
                     │ Backend Service         │
                     │ NodePort :30008         │
                     └──────────┬──────────────┘
                                │
                                ▼
                     ┌─────────────────────────┐
                     │ Backend Pod (Flask API) │
                     └─────────────────────────┘
🧰 Tech Stack
Layer	Technology
Cloud	AWS EC2 (Free Tier)
Container	Docker
Registry	Docker Hub
Orchestration	Kubernetes
Backend	Python (Flask)
Frontend	HTML, JavaScript, Nginx
Networking	NodePort Services
OS	Amazon Linux
📁 Repository Structure
devops-dashboard/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── index.html
│   └── Dockerfile
│
├── k8s/
│   ├── deployments.yaml
│   ├── frontend-service.yaml
│   └── backend-service.yaml
│
└── README.md
🐳 Containerization
Backend

Python Flask REST API

Exposes /api/info

Runs on port 5000

CORS enabled for cross-origin access

Example response:

{
  "app": "DevOps Dashboard",
  "hostname": "backend-pod-name",
  "status": "Running in Kubernetes"
}
Frontend

Static HTML + JavaScript

Served via Nginx

Fetches backend API from NodePort endpoint

Displays dynamic JSON response

☸ Kubernetes Configuration
Deployments

backend Deployment (1 replica)

frontend Deployment (1 replica)

Label-based selector matching

Container ports exposed properly

Services
Service	Type	Port	Purpose
frontend-service	NodePort	30007	Public access
backend-service	NodePort	30008	API access
🌐 Accessing the Application

Frontend:

http://<EC2-PUBLIC-IP>:30007

Backend API:

http://<EC2-PUBLIC-IP>:30008/api/info
🔐 AWS Configuration

Security Group Inbound Rules:

Port	Purpose
22	SSH
30007	Frontend
30008	Backend
🚀 Deployment Steps (High-Level)

Build Docker images

Push images to Docker Hub

Apply Kubernetes YAML files

Configure AWS Security Groups

Access via NodePort

🧠 Engineering Challenges & Solutions
1️⃣ Service Selector Mismatch

Resolved label-selector mismatch between Deployment and Service definitions.

2️⃣ Internal vs External DNS

Understood difference between Kubernetes internal DNS (backend-service) and public NodePort access via EC2 IP.

3️⃣ CORS Issue

Enabled Flask CORS to allow cross-origin requests between frontend (port 30007) and backend (port 30008).

4️⃣ NodePort Networking

Configured NodePort exposure and AWS Security Group rules for external accessibility.

📊 Key DevOps Concepts Demonstrated

Docker image lifecycle management

Kubernetes Deployments & Services

Label & Selector architecture

Pod-to-Pod vs Browser-to-Service networking

NodePort exposure strategy

Cloud firewall configuration

Runtime debugging using kubectl logs

Rollout restarts & image updates



Cloud infrastructure understanding

Production-style deployment thinking

Strong DevOps fundamentals
