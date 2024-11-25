from flask import Flask, request, jsonify
from chatbot import create_response


app = Flask(__name__)


# Define a route to handle POST requests
@app.route('/api/get-response', methods=['POST'])
def get_ai_response():
    try:
        user_prompt = request.form.get("user_prompt")
        if not user_prompt:
            return jsonify({"error": "User prompt is required"}), 400
        
        doc_type = request.form.get("doc_type")
        if not doc_type:
            return jsonify({"error": "Document type is required"}), 400
        if not doc_type in ["MAS", "NAI", "OTI", "OTE", "OAI", "OAE", "NTI", "NTE", "NAE", "Custom Social"]:
            return jsonify({"error": 'Document type must be either "MAS", "NAI", "OTI", "OTE", "OAI", "OAE", "NTI", "NTE", "NAE", "Custom Social"'}), 400
        
        ai_reply = create_response(doc_type, user_prompt)

        # Process the data (for example, respond with a message)
        response = {
            'reply': ai_reply
        }

        # Return the response as JSON
        return jsonify(response), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
