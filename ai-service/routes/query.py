from flask import Blueprint, request, jsonify
from services.groq_client import GroqClient
from services.chroma_client import ChromaClient

query_bp = Blueprint("query", __name__)

groq = GroqClient()
chroma = ChromaClient()


def load_prompt():
    with open("prompts/query_prompt.txt", "r") as f:
        return f.read()


@query_bp.route("/query", methods=["POST"])
def query():
    try:
        data = request.get_json()

        if not data or "question" not in data:
            return jsonify({"error": "Missing 'question'"}), 400

        question = data["question"]

        docs = chroma.query(question)

        sources = docs[0] if docs else []

        context = "\n".join([f"- {doc}" for doc in sources])

        prompt_template = load_prompt()

        prompt = prompt_template.format(
            context=context,
            question=question
        )

        answer = groq.generate(prompt)

        return jsonify({
            "answer": answer,
            "sources": sources,
            "confidence": round(len(sources) / 3, 2)
        })

    except Exception:
        return jsonify({"error": "Internal server error"}), 500