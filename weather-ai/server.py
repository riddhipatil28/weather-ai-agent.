from flask import Flask, request, jsonify
from flask_cors import CORS

# ===== AGENT =====
from agent.controller import WeatherAgent

# ===== TOOLS =====
from tools.detect_city import detect_city
from tools.weather_api import get_weather
from tools.prediction_model import predict_temp


# ==============================
# FLASK APP
# ==============================
app = Flask(__name__)
CORS(app)


# ==============================
# REGISTER TOOLS
# ==============================
tools = {
    "detect_city": detect_city,
    "get_weather": get_weather,
    "predict_temp": predict_temp
}

agent = WeatherAgent(tools)


# ==============================
# CHAT ROUTE
# ==============================
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        if not data or "message" not in data:
            return jsonify({"error": "Message is required"}), 400

        user_message = data["message"]
        result = agent.handle_message(user_message)

        return jsonify({
            "reply": result.get("reply", ""),
            "trace": result.get("trace", []),
            "memory_recall": result.get("memory_recall", [])
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ==============================
# RETURN LAST 4 CHAT MESSAGES
# ==============================
@app.route("/history", methods=["GET"])
def history():
    try:
        history = agent.memory.get_history()
        return jsonify(history[-4:] if len(history) > 4 else history)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ==============================
# CLEAR MEMORY
# ==============================
@app.route("/clear", methods=["POST"])
def clear_memory():
    try:
        agent.memory.clear()
        return jsonify({"status": "memory cleared"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ==============================
# HEALTH CHECK
# ==============================
@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "Weather AI running"})


# ==============================
if __name__ == "__main__":
    app.run(debug=True)
