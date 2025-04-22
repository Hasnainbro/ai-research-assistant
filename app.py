from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from graphs.langgraph_flow import langgraph_flow  # update this import based on your folder structure

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        query = data.get("message", "")
        if not query:
            return jsonify({"response": "Please enter a valid message."}), 400

        response = langgraph_flow(query)
        cleaned_response = response.strip().replace("* ", "- ") 
        return jsonify({"response": cleaned_response})
    except Exception as e:
        return jsonify({"response": f"❌ Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
