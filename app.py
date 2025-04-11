from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    
    # For now, let's just echo the user's input
    # This is where we'll eventually connect to the LLM.
    chatbot_response = f"Echo: {user_input}"

    return render_template('index.html', user_input=user_input, chatbot_response=chatbot_response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
