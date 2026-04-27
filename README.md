# 🚀 AI DevOps Copilot

## 📌 Overview
AI DevOps Copilot is an AI-powered prototype designed to automate incident resolution in DevOps environments.

The system intelligently processes:
- ServiceNow Tickets  
- Application Logs  
- Codebase  

and generates:
- Root Cause Analysis  
- Fix Suggestions  
- Impacted Files  
- Priority Levels  
- Business Requirement Document (BRD)  
- Proactive Recommendations  

---

## 🎯 Problem Statement
In traditional DevOps workflows, incident resolution is manual and time-consuming:
- Engineers analyze logs  
- Debug code  
- Identify root cause  

This leads to delays and inefficiencies.

👉 This project demonstrates how AI can automate and accelerate this process.

---

## 💡 Solution Approach
This solution is designed as an **AI-driven automated pipeline**:

1. ServiceNow ticket acts as a trigger  
2. Logs and codebase are collected  
3. AI model analyzes the issue  
4. Root cause and fix suggestions are generated  
5. BRD and recommendations are created  
6. DevOps task is triggered  

---

## 🧠 Architecture

ServiceNow Ticket
↓
Copilot / Power Automate
↓
Data Collection (Logs + Code)
↓
AI Engine (Python + LLM)
↓
Analysis Layer
↓
BRD Generator
↓
Azure DevOps Task

---

## ⚙️ Tech Stack
- Python  
- OpenAI / Azure OpenAI  
- DevOps Concepts  
- Copilot Integration (Conceptual)  

---

## 🚀 Features
- AI-based Root Cause Analysis  
- Automated Fix Suggestions  
- Code-level Issue Detection  
- BRD Generation  
- DevOps Task Simulation  
- Proactive Issue Prevention  

---

## ▶️ How to Run

### Install dependencies

pip install openai

### Add API Key
Update in `ai_engine.py`:

openai.api_key = "YOUR_API_KEY"

### Run the project

python app/main.py

---

## 📊 Sample Output

Root Cause:
NullPointerException due to missing null check

Fix:
Add null validation before accessing object

Impacted File:
UserService.java

Priority:
High

Prevention:
Add validation and improve logging

---

## 🔮 Future Scope
- Real ServiceNow Integration  
- Azure DevOps API Integration  
- CI/CD pipeline monitoring  
- Copilot-based automation  
- Real-time issue detection  

---

## 👨‍💻 Author
Rahul Bharambe  

---

## ⭐ Key Highlight
This project demonstrates how AI can be integrated into DevOps workflows to automate incident resolution, reduce manual effort, and improve system reliability.
