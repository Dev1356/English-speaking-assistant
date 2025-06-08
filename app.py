from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")  # Set your OpenAI API key in environment variable

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-response", methods=["POST"])
def get_response():
    user_text = request.json.get("message")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful English-speaking assistant."},
                {"role": "user", "content": user_text}
            ]
        )
        reply = response['choices'][0]['message']['content']
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)