from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/budget-analysis', methods=['POST'])
def analyze_budget():
    data = request.get_json()
    
    if not data or "expense_string" not in data:
        return jsonify({"error": "No expense string provided"}), 400

    expense_string = data["expense_string"]

    # Simulating AI-powered categorization
    response = {
        "categorized_expenses": {
            "Essentials": ["Groceries", "Rent"],
            "Discretionary": ["Dining Out", "Travel"]
        },
        "suggestions": [
            "Reduce dining out expenses",
            "Optimize travel costs"
        ]
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

