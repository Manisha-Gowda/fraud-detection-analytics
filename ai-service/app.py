from flask import Flask, jsonify
from flask_cors import CORS
import logging

# 🔹 Import blueprint
from routes.describe import describe_bp

app = Flask(__name__)
CORS(app)
# 🔹 Register blueprint
app.register_blueprint(describe_bp)

# 🔹 Logging setup
logging.basicConfig(level=logging.INFO)



# 🔹 Health Check Endpoint
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


# 🔹 Global Error Handler

@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(f"Unhandled Exception: {str(e)}")
    return jsonify({
        "status": "error",
        "message": "Internal server error"
    }), 500

if __name__ == "__main__":
    app.run(debug=True)