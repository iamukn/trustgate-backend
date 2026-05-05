---

# TrustGate 🔐

TrustGate is a lightweight fraud detection and trust scoring system built for the GSMA CAMARA Hackathon. It leverages telco APIs such as SIM Swap, Device Status, and Number Verification to assess the risk level of mobile transactions and user authentication attempts in real time.

---

## 🚀 Problem Statement

Mobile fraud (especially SIM swap-based account takeover) is a growing threat in digital identity and financial systems. Traditional OTP-based security is no longer sufficient.

TrustGate addresses this by adding a **real-time trust layer using telecom network signals**.

---

## 🧠 Solution Overview

TrustGate evaluates user trust using a multi-signal scoring engine:

### Core Signals:
- 📱 **SIM Swap Detection**
- 📡 **Device Connectivity Status**
- 🔐 **Number Verification (identity consistency check)**

Each signal contributes to a unified **TrustScore (0–100)**:
- 0–30 → Low Risk (Allow)
- 31–60 → Medium Risk (Step-up Verification)
- 61–100 → High Risk (Block / Reject)

---

## How to run TrustGate Locally

- Create .env file in the root of the app with the below required variables

1. BASE_URL="https://network-as-code.p-eu.rapidapi.com" 
2. nokiaApiKey="youApiKeyFromNokiaPlatform"

- Create and start a Virtual Environment
- Install app requirements
- Start the Uvicorn Server

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

-- Visit http://localhost:8000/docs

## ⚙️ How It Works

1. User initiates a sensitive action (transaction)
2. System checks SIM swap status via CAMARA API
3. If SIM swap is detected, risk score is initialized (up to 60)
4. Device status is evaluated to adjust confidence
5. If risk remains high, Number Verification API is triggered
6. Final TrustScore is computed and action is returned

---

## 📊 Scoring Model

- SIM Swap (strong signal): up to **60 points**
- Device Status (moderate signal): ±15 adjustment
- Number Verification (identity validation): ±25 adjustment

Final score is normalized to 0–100.

---

## 🧩 Tech Stack

- Python (FastAPI)
- GSMA CAMARA APIs (via Nokia RapidAPI)
- Pydantic (data validation)
- Requests (API calls)

---

## 🔐 Key Features

- Real-time SIM swap fraud detection
- Progressive risk-based verification flow
- Step-up authentication using telco intelligence
- Lightweight scoring engine (easy to extend)
- API-ready for fintech / identity systems

---

## 🛠️ API Flow

```

Request → SIM Swap Check → Device Check → (Optional) Number Verification → TrustScore → Decision

````

---

## 🎯 Output Example

```json
{
  "trustScore": 72,
  "risk_level": "HIGH",
  "simSwap": true,
  "deviceStatus": true,
  "numbersVerification": true,
  "action": "BLOCK"
}
````

---

## 💡 Future Improvements

* ML-based adaptive risk scoring
* Geo-velocity fraud detection

---

## 👨‍💻 Built For

GSMA Open Gateway / CAMARA Hackathon

---

## 📌 Summary

TrustGate turns telecom network intelligence into a **real-time fraud prevention layer**, helping secure digital identity at the infrastructure level.

---
