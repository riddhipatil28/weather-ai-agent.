import ollama


def generate_reply(user_message, tool_results, history, past_context):

    # ===============================
    # FORMAT HISTORY (last 6 only)
    # ===============================
    history_text = "\n".join(
        [f"{m['role']}: {m['text']}" for m in history[-6:]]
    )

    # ===============================
    # FORMAT MEMORY
    # ===============================
    memory_text = "\n".join(past_context) if past_context else "None"

    # ===============================
    # STRICT AGENT CONTROL PROMPT
    # ===============================
    prompt = f"""
You are a professional real-time weather assistant.

YOU MUST FOLLOW THESE RULES STRICTLY:

1. Answer ONLY using the provided weather data.
2. Do NOT explain science, climate change, or theory.
3. Do NOT give long paragraphs.
4. Do NOT guess missing data.
5. If city is missing → ask user for city.
6. If weather data exists → respond in 1–3 short sentences.
7. Never invent information.
8. Never discuss global warming or environmental analysis.

--------------------------------

Relevant memory:
{memory_text}

Recent conversation:
{history_text}

User question:
{user_message}

Weather tool results:
{tool_results}

--------------------------------

Respond naturally like a weather assistant.
Short, clear, factual.
"""

    # ===============================
    # LOCAL LLM CALL
    # ===============================
    res = ollama.chat(
        model="phi3",   # keep your model
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return res["message"]["content"].strip()
