import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY"),
) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/triage', methods=['POST'])
def triage():
    data = request.get_json()
    symptoms = data.get('symptoms', '')

    if not symptoms or len(symptoms.strip()) < 3:
        return jsonify({'triage': 'Please describe your symptoms in more detail (at least 3 characters).'})

    prompt = f"""You are a medical triage assistant. The user reports these symptoms: {symptoms}

    Provide a triage assessment with:
    1. Possible conditions (list 2-3)
    2. Urgency level: SELF-CARE, GP, or A&E
    3. Recommended next steps (2-3 specific actions)

    Be clear, direct, and include a disclaimer that this is not a diagnosis.
    """

    try:
        message = client.chat.completions.create(
            model="openrouter/free",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
        )
        response_text = message.choices[0].message.content
    except Exception as e:
        return jsonify({'triage': f'Error: {str(e)}. Please try again.'})

    return jsonify({'triage': response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)