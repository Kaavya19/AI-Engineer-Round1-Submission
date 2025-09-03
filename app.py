from flask import Flask, jsonify, request
from email_fetcher import fetch_emails
from nlp_pipeline import analyze_email
from response_generator import generate_response

app = Flask(__name__)

@app.route('/emails', methods=['GET'])
def get_emails():
    emails = fetch_emails()
    processed = [analyze_email(e) for e in emails]
    return jsonify(processed)

@app.route('/respond', methods=['POST'])
def respond():
    data = request.json
    reply = generate_response(data['email_body'])
    return jsonify({'reply': reply})

if __name__ == "__main__":
    app.run(debug=True)
    