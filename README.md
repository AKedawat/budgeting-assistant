# Budgeting Assistant

## 📌 Overview
Budgeting Assistant is an AI-powered tool that takes an **expense string** in JSON format as input, categorizes spending, and provides budgeting insights. 

## 🚀 Features
- Accepts expenses as a JSON object
- Categorizes spending into essential & discretionary
- Provides insights and savings recommendations

## 📦 Tech Stack
- Python (Flask for API)
- Sonnet API (for AI-powered categorization)

## 🔧 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AKedawat/budgeting-assistant.git
pip install -r requirements.txt
python app.py
{
  "expense_string": "Groceries: 5000, Rent: 12000, Dining Out: 3000, Travel: 5000"
}
response : 
{
  "categorized_expenses": {
    "Essentials": ["Groceries", "Rent"],
    "Discretionary": ["Dining Out", "Travel"]
  },
  "suggestions": [
    "Reduce dining out expenses",
    "Optimize travel costs"
  ]
}


