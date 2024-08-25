from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will allow all domains; you can customize this as needed

# Your existing code...

# Helper function to extract highest lowercase alphabet
def get_highest_lowercase(alphabets):
    lowercase = [ch for ch in alphabets if ch.islower()]
    return max(lowercase) if lowercase else None

# POST endpoint
@app.route('/bfhl', methods=['POST'])
def process_bfhl():
    data = request.json.get('data', [])
    
    # Filter numbers and alphabets
    numbers = [x for x in data if x.isdigit()]
    alphabets = [x for x in data if x.isalpha()]
    
    # Get the highest lowercase alphabet
    highest_alpha = get_highest_lowercase(alphabets)
    
    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",  # Replace with dynamic user_id generation logic
        "email": "john@xyz.com",         # Replace with actual email
        "roll_number": "ABCD123",        # Replace with actual roll number
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_alpha] if highest_alpha else []
    }
    
    return jsonify(response)

# GET endpoint
@app.route('/bfhl', methods=['GET'])
def operation_code():
    return jsonify({
        "operation_code": 1
    })

if __name__ == '__main__':
    app.run(debug=True)
