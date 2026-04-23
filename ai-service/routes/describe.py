from flask import Blueprint, request, jsonify
from datetime import datetime
import json

# 🔹 RAG + Groq
from services.chroma_client import query_documents
from services.groq_client import generate_response

describe_bp = Blueprint("describe", __name__)


# =========================================================
# 🔹 Utility: Load Prompt
# =========================================================
def load_prompt():
    with open("prompts/describe_prompt.txt", "r") as file:
        return file.read()


# =========================================================
# 🔹 Endpoint 1: /describe (AI + RAG Analysis)
# =========================================================
@describe_bp.route("/describe", methods=["POST"])
def describe():
    data = request.get_json()

    # ✅ Input validation
    if not data or "text" not in data:
        return jsonify({"error": "text field is required"}), 400

    text = data["text"]

    # ✅ Load prompt
    base_prompt = load_prompt().replace("{text}", text)

    # ✅ RAG context
    context_docs = query_documents(text)
    context = ""

    if context_docs and len(context_docs) > 0:
        context = "\n".join(context_docs[0])

    # ✅ Final prompt
    final_prompt = f"""
You are a fraud detection expert.

Context:
{context}

{base_prompt}
"""

    try:
        # ✅ Call Groq
        ai_output = generate_response(final_prompt)

        # ✅ Parse JSON response
        parsed_output = json.loads(ai_output)

    except Exception as e:
        print("Describe Error:", e)
        parsed_output = {
            "risk_level": "Unknown",
            "explanation": "Error generating response",
            "key_indicators": []
        }

    return jsonify({
        "analysis": parsed_output,
        "generated_at": datetime.utcnow().isoformat()
    })


# =========================================================
# 🔹 Endpoint 2: /recommend (Static Actions)
# =========================================================
@describe_bp.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "text field is required"}), 400

    text = data["text"]

    recommendations = [
        {
            "action_type": "BLOCK_TRANSACTION",
            "description": f"Block suspicious activity related to: {text}",
            "priority": "HIGH"
        },
        {
            "action_type": "VERIFY_IDENTITY",
            "description": "Request additional user verification",
            "priority": "MEDIUM"
        },
        {
            "action_type": "MONITOR_ACCOUNT",
            "description": "Monitor account for further unusual activity",
            "priority": "LOW"
        }
    ]

    return jsonify({
        "recommendations": recommendations
    })


# =========================================================
# 🔹 Endpoint 3: /generate-report (Structured Report)
# =========================================================
@describe_bp.route("/generate-report", methods=["POST"])
def generate_report():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "text field is required"}), 400

    text = data["text"]

    # ✅ RAG context
    context_docs = query_documents(text)
    context = ""

    if context_docs and len(context_docs) > 0:
        context = "\n".join(context_docs[0])

    # ✅ Prompt
    prompt = f"""
    You are a fraud analysis expert.

    Context:
    {context}

    User Input:
    {text}

    Return JSON ONLY in this exact format:

    {{
    "title": "",
    "executive_summary": "",
    "overview": "",
    "top_items": ["item1", "item2", "item3"],
    "recommendations": ["rec1", "rec2", "rec3"]
    }}

    Rules:
    - top_items must be a list of short strings
    - recommendations must be a list of short actionable strings
    - Do not return objects inside arrays
    - No extra text outside JSON
    """

    try:
        ai_output = generate_response(prompt)
        parsed_output = json.loads(ai_output)
    except Exception as e:
        print("Report Error:", e)
        parsed_output = {"error": "Failed to generate report"}

    return jsonify(parsed_output)