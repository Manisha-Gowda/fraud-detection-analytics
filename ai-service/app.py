from flask import Flask
from routes.categorise import categorise_bp
from routes.query import query_bp
from services.data_loader import load_data_to_chroma

app = Flask(__name__)

# 🔥 Load dataset into ChromaDB
load_data_to_chroma()

# Register routes
app.register_blueprint(categorise_bp)
app.register_blueprint(query_bp)

if __name__ == "__main__":
    app.run(debug=True)