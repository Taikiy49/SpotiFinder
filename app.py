from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from datasets import load_dataset
from youtube import YoutubeQuery

app = Flask(__name__)

genai.configure(api_key="AIzaSyBd31J9setEcfjVr5tjNyRzjuQ4BpX_6K0")
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chatbot.html')
def chatbot():
    return render_template('chatbot.html')

@app.route('/chatbot', methods=['POST'])  # Second route
def chatbot_api():
    user_input = request.json.get('input', '')
    chatbot_response = chatbot_interaction(user_input)
    YoutubeQuery(chatbot_response).run()
    return '', 204 # this allows me to return nothing

def chatbot_interaction(user_input):
    convo = model.start_chat(history=[])
    convo.send_message(user_input)
    bot_response = convo.last.text
    return bot_response


if __name__ == '__main__':
    app.run(debug=True)

