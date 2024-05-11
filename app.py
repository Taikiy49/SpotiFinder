from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from youtube import YoutubeQuery  # Ensure you have this module imported if necessary
from datasets import load_dataset  # Ensure you have this module imported if necessary

app = Flask(__name__)

# Configure generative AI model
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

@app.route('/chatbot', methods=['POST'])
def chatbot_api():
    user_input = request.json.get('input', '')
    chatbot_response = chatbot_interaction("Find a song about " + user_input + " and ONLY give me the song title. ONLY the song TITLE")
    # Assuming YoutubeQuery is correctly implemented
    data = YoutubeQuery(chatbot_response).run()
    videos = []
    for item in data.get('items', []):
        if item['id']['kind'] == 'youtube#video':
            video_title = item['snippet']['title']
            video_id = item['id']['videoId']
            videos.append({video_title + ":" + video_id})
    return jsonify({"message": f"{videos}"})


def chatbot_interaction(user_input):
    convo = model.start_chat(history=[])
    convo.send_message(user_input)
    bot_response = convo.last.text
    return bot_response




if __name__ == '__main__':
    app.run(debug=True)
