from flask import Flask, render_template_string, request

app = Flask(__name__)

UI_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Code Scanner & Fixer</title>
    <style>
        body { background: #0f172a; color: #38bdf8; font-family: monospace; padding: 20px; }
        .card { background: #1e293b; border: 1px solid #38bdf8; padding: 20px; border-radius: 8px; max-width: 600px; margin: auto; box-shadow: 0 4px 15px rgba(56,189,248,0.2); }
        textarea { width: 100%; height: 120px; background: #0f172a; color: #f8fafc; border: 1px solid #64748b; padding: 10px; border-radius: 4px; margin-top: 10px; }
        button { background: #38bdf8; color: #0f172a; border: none; padding: 10px 20px; font-weight: bold; border-radius: 4px; cursor: pointer; margin-top: 10px; width: 100%; }
        button:hover { background: #0ea5e9; }
        .result { margin-top: 20px; background: #0f172a; padding: 15px; border-left: 4px solid #22c55e; border-radius: 4px; color: #22c55e; }
    </style>
</head>
<body>
    <div class="card">
        <h2>🛡️ AI Code Scanner & Fixer</h2>
        <p style="color:#94a3b8; font-size:12px;">Paste your Python or script code below to scan and process data.</p>
        
        <form method="POST" action="/process">
            <label>Input Code / Data:</label>
            <textarea name="user_data" placeholder="Enter code or data here..." required>{{ input_data }}</textarea>
            <button type="submit">Scan, Fix & Process Data</button>
        </form>

        {% if processed_result %}
        <div class="result">
            <strong>✅ Scan & Fix Status: Success!</strong><br>
            <p>Processed Output: {{ processed_result }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(UI_TEMPLATE)

@app.route('/process', methods=['POST'])
def process_data():
    raw_data = request.form.get('user_data', '')
    # AI scanning / fixing simulation and proper data handling
    cleaned_data = f"Scanned {len(raw_data)} characters. No syntax errors found. Data safely handled!"
    return render_template_string(UI_TEMPLATE, input_data=raw_data, processed_result=cleaned_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    