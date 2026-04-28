from flask import Blueprint, request, jsonify
from datetime import datetime
import json
import logging

# 🔹 Services
from services.chroma_client import query_documents
from services.groq_client import generate_response

describe_bp = Blueprint("describe", __name__)


# 🔹 Utility: Load Prompt

def load_prompt():
    with open("prompts/describe_prompt.txt", "r") as file:
        return file.read()



# 🔹 Endpoint 1: /describe

@describe_bp.route("/describe", methods=["POST"])
def describe():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"status": "error", "message": "text field is required"}), 400

    text = data["text"]
    logging.info(f"/describe called with input: {text}")

    # 🔹 Load prompt
    base_prompt = load_prompt().replace("{text}", text)

    # 🔹 RAG context
    context_docs = query_documents(text)
    context = ""

    if context_docs and len(context_docs) > 0:
        context = "\n".join(context_docs[0])

    # 🔹 Final prompt
    final_prompt = f"""
You are a fraud detection expert.

Context:
{context}

{base_prompt}
"""

    try:
        ai_output = generate_response(final_prompt)
        parsed_output = json.loads(ai_output)
    except Exception as e:
        logging.error(f"/describe error: {str(e)}")
        parsed_output = {
            "risk_level": "Unknown",
            "explanation": "Error generating response",
            "key_indicators": []
        }

    return jsonify({
        "status": "success",
        "data": parsed_output,
        "generated_at": datetime.utcnow().isoformat()
    })



# 🔹 Endpoint 2: /recommend

@describe_bp.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"status": "error", "message": "text field is required"}), 400

    text = data["text"]
    logging.info(f"/recommend called with input: {text}")

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
        "status": "success",
        "data": recommendations
    })


# =========================================================
# 🔹 Endpoint 3: /generate-report
@describe_bp.route("/generate-report", methods=["POST"])
def generate_report():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"status": "error", "message": "text field is required"}), 400

    text = data["text"]
    logging.info(f"/generate-report called with input: {text}")

    # 🔹 RAG context
    context_docs = query_documents(text)
    context = ""

    if context_docs and len(context_docs) > 0:
        context = "\n".join(context_docs[0])

    # 🔹 Prompt
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
  "top_items": ["item1", "item2"],
  "recommendations": ["rec1", "rec2"]
}}
"""

    try:
        ai_output = generate_response(prompt)
        parsed_output = json.loads(ai_output)
    except Exception as e:
        logging.error(f"/generate-report error: {str(e)}")
        parsed_output = {"error": "Failed to generate report"}

    return jsonify({
        "status": "success",
        "data": parsed_output
    })