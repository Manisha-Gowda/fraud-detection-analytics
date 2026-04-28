from flask import Blueprint, request, jsonify
import json
import re
import time

from services.shared import groq_client as client

categorise_bp = Blueprint("categorise", __name__)


def load_prompt():
    with open("prompts/categorise_prompt.txt", "r") as file:
        return file.read()


@categorise_bp.route("/categorise", methods=["POST"])
def categorise():
    try:
        data = request.get_json()

        if not data or "text" not in data:
            return jsonify({"error": "Missing 'text' field"}), 400

        input_text = data["text"]

        prompt_template = load_prompt()
        prompt = prompt_template.format(input_text=input_text)

        # 🔥 Timing start
        start = time.time()
        response = client.generate(prompt)
        end = time.time()

        # 🔥 Extract JSON
        try:
            json_match = re.search(r'\{[\s\S]*?\}', response)

            if json_match:
                parsed_response = json.loads(json_match.group())
            else:
                raise ValueError("No JSON found")

        except Exception:
            parsed_response = {
                "category": "Unknown",
                "confidence": 0.0,
                "reasoning": response
            }

        return jsonify({
            "data": parsed_response,
            "meta": {
                "confidence": parsed_response.get("confidence", 0.0),
                "model_used": client.model,
                "tokens_used": len(prompt.split()),
                "response_time_ms": int((end - start) * 1000),
                "cached": False
            }
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500