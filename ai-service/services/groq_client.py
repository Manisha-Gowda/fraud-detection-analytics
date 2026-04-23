from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_response(prompt):
    try:
        print("Calling Groq...")

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You are a strict JSON generator. Always return valid JSON only."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,   # 🔹 more consistent output
            max_tokens=500
        )

        response = completion.choices[0].message.content

        print("Groq response received")

        # 🔹 Basic validation
        if not response:
            raise ValueError("Empty response from Groq")

        return response

    except Exception as e:
        print("Groq Error:", e)
        return '{"risk_level": "Unknown", "explanation": "Error generating response", "key_indicators": []}'