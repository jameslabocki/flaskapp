from flask import Flask, render_template, request
import requests

app = Flask(__name__)

LLM_API_URL = "http://host.containers.internal:42701/v1/chat/completions"

def get_llm_response(user_input):
    payload = {
        "model": "gpt-3.5-turbo",  # or whatever model name your endpoint expects
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    }

    try:
        response = requests.post(LLM_API_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        return data['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error calling LLM API: {e}")
        return "Sorry, something went wrong when trying to get a response from the chatbot."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    chatbot_response = get_llm_response(user_input)
    return render_template('index.html', user_input=user_input, chatbot_response=chatbot_response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
