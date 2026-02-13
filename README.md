
# 🚀 CI/CD Pipeline for Kubernetes Deployment

![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestrated-blue)
![Jenkins](https://img.shields.io/badge/Jenkins-CI/CD-red)
![Helm](https://img.shields.io/badge/Helm-Package%20Manager-purple)

## 📖 Project Overview

This project demonstrates a complete CI/CD pipeline for deploying a containerized network application on a Kubernetes cluster using:

- Docker
- GitHub
- Jenkins
- Kubernetes (Docker Desktop)
- Helm
- Prometheus
- Grafana

The pipeline automates build, testing, image publishing, deployment, and monitoring.

---

## 🏗 Architecture Overview
Developer
↓
GitHub Repository
↓
Jenkins (CI/CD Engine)
↓
Docker Image Build
↓
Docker Hub
↓
Kubernetes Cluster (2 Replicas)
↓
Service (NodePort)
↓
Prometheus → Grafana


---

## 📂 Project Structure

asdn-k8s-cicd/
│
├── app/ # Flask application
├── k8s/ # Kubernetes manifests
├── jenkins/ # Jenkins configuration
├── Jenkinsfile # CI/CD pipeline definition
├── grafana-values.yaml # Monitoring customization
└── README.md

---

## ⚙️ CI/CD Pipeline Stages

1. Checkout source code
2. Build Docker image
3. Run automated tests (pytest)
4. Push image to Docker Hub
5. Deploy to Kubernetes
6. Validate rollout

---

## 🚀 Kubernetes Deployment

Apply manifests:```bash

Verify deployment:
kubectl get pods
kubectl get deployments
kubectl get svc

----------

## 🔐 Kubernetes Authentication (Jenkins)

A ServiceAccount was created for secure cluster access:
kubectl create namespace jenkins
kubectl create serviceaccount jenkins-deployer -n jenkins
kubectl create clusterrolebinding jenkins-deployer-binding \
  --clusterrole=cluster-admin \
  --serviceaccount=jenkins:jenkins-deployer

----------

## 📊 Monitoring Stack

Installed using Helm:
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install monitoring prometheus-community/kube-prometheus-stack -n monitoring
Access Grafana:
kubectl -n monitoring port-forward svc/monitoring-grafana 3000:80
Then open:
http://localhost:3000

----------

## ✅ Final Validation

kubectl rollout status deployment asdn-project

## 🎯 Key Features

Automated CI/CD pipeline

Containerized application

Kubernetes deployment with replicas

Secure Jenkins authentication

Monitoring with Prometheus & Grafana

Self-healing & scalable architecture


