from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Initialize OpenAI client
client = openai.OpenAI(api_key="sk-...PGcA")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json["message"]

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        bot_reply = response.choices[0].message.content
        return jsonify({"reply": bot_reply})
    
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
