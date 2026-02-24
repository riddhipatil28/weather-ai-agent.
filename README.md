#  AI Weather Agent

An autonomous AI weather assistant that understands natural language, retrieves real-time weather data, remembers conversations, and responds intelligently using a **local Large Language Model**.

This project demonstrates a **tool-using AI agent architecture** with planning, memory, semantic recall, and context-aware reasoning — built as a full-stack AI system.

---

## Features

 Natural language weather queries
 Automatic city detection
 Real-time weather retrieval
 Temperature prediction model
 Short-term conversational memory
 Long-term semantic memory (vector search)
 Context-aware responses
 Local LLM (Ollama) — no paid AI APIs
 Agent planning + tool execution
 ChatGPT-style React UI
 Persistent conversation history
 Real-time weather data via OpenWeatherMap API

---

##  Weather Data Source

This project uses the **OpenWeatherMap API** to retrieve real-time weather data for cities worldwide.

The AI agent automatically:

* Detects the requested city
* Fetches live weather conditions
* Retrieves temperature, humidity, wind, and forecast
* Uses real data to generate grounded responses

Weather data is fetched through:

```
tools/weather_api.py
```

API Provider:
https://openweathermap.org/

---

## Agent Architecture

User Message
→ Intent Understanding
→ Planner decides tools
→ Tool execution (Weather API / Prediction Model)
→ Memory retrieval (semantic search)
→ LLM generates grounded response
→ Memory updated

This is a **tool-augmented, memory-augmented AI agent**.

---

## System Components

### 🔹 Frontend

* React (Vite)
* Chat-style UI
* Conversation history restore
* ChatGPT-like interface

### 🔹 Backend

* Flask API server
* Agent controller
* Tool registry
* Execution engine

### 🔹 AI Layer

* Local LLM via Ollama
* Prompt-controlled responses
* Tool-grounded generation

### 🔹 Memory System

* Short-term chat history
* Long-term vector database (FAISS)
* Semantic recall with embeddings

### 🔹 Tools

* City detection
* OpenWeatherMap weather API
* Temperature prediction model (ML)

---

##  Tech Stack

* Python
* Flask
* React (Vite)
* Ollama (local LLM)
* OpenWeatherMap API (real-time weather data)
* FAISS vector database
* Sentence Transformers
* Scikit-learn

---

##  Project Structure

```
weather-app/
│
├── src/                     # React frontend
│
├── weather-ai/
│   ├── agent/               # Core agent logic
│   ├── tools/               # External tools (API + ML)
│   ├── llm/                 # Local LLM interface
│   ├── memory_store/        # Vector database
│   └── server.py            # Flask backend
│
└── README.md
```

---

##  Installation

### Clone repository

```
git clone https://github.com/riddhipatil28/weather-ai-agent.
cd weather-app
```

---

### Install backend dependencies

```
pip install flask flask-cors requests sentence-transformers faiss-cpu ollama
```

---

### Install frontend dependencies

```
npm install
```

---

###  Run Ollama model

```
ollama run phi3
```

---

## Run Application

### Start backend

```
cd weather-ai
python server.py
```

### Start frontend

```
npm run dev
```

Open browser:

```
http://localhost:5173
```

---

## Example Queries

* What is the weather in Pune?
* Will it rain today in Mumbai?
* Should I carry an umbrella?
* Temperature forecast for tomorrow 

---

##  Learning Outcomes

This project demonstrates:

✔ Agent-based AI system design
✔ Tool-augmented LLMs
✔ Memory-augmented reasoning
✔ Semantic vector search
✔ Prompt engineering
✔ Local AI deployment
✔ Real-time API integration
✔ Full-stack AI application

---

## Future Improvements

* Multi-city comparison
* Weather alerts
* Voice interaction
* Mobile UI
* Cloud deployment
* Autonomous planning loop
* User profiles & personalization




