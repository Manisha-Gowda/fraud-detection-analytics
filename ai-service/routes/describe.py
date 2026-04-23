from flask import Blueprint, request, jsonify
from datetime import datetime

describe_bp = Blueprint("describe", __name__)

def load_prompt():
    with open("prompts/describe_prompt.txt", "r") as file:
        return file.read()

@describe_bp.route("/describe", methods=["POST"])
def describe():
    data = request.get_json()

    # ✅ Input validation
    if not data or "text" not in data:
        return jsonify({"error": "text field is required"}), 400

    text = data["text"]

    # ✅ Load prompt
    prompt = load_prompt().replace("{text}", text)

    # ❗ AI call will come later (Day 4+)
    # For now, return mock structured response

    result = {
        "risk_level": "Medium",
        "explanation": f"Analysis based on input: {text}",
        "key_indicators": [
            "pattern anomaly",
            "frequency spike"
        ],
        "generated_at": datetime.utcnow().isoformat()
    }

    return jsonify(result)