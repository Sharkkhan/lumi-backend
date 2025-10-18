# 🌟 Lumi Backend

This is the **backend API** for the **Lumi App**, built with **FastAPI** and hosted on **Render**.  
It powers Lumi’s voice analysis, speech-to-text, and AI rewriting features.

---

## 🚀 Overview

**Lumi** helps users improve their communication skills through AI-powered feedback.  
The backend acts as a secure middle layer between the frontend (Base44) and the OpenAI API.

### ✨ Features
- 🎙️ **Speech-to-Text** using OpenAI Whisper (`whisper-1`)
- 🧠 **Text Analysis & Rewrite** using GPT-4o-mini
- 🎚️ **Voice Upload & Analysis Endpoints**
- 🔒 **Secure API key management (via Render environment variables)**
- 🌐 **CORS enabled** for integration with Base44 frontend

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| Framework | FastAPI |
| Server | Uvicorn |
| Hosting | Render |
| Language | Python 3.10+ |
| AI APIs | OpenAI Whisper + GPT-4o-mini |
| Env Management | python-dotenv |
| HTTP Client | requests |

---

## 📂 Project Structure


