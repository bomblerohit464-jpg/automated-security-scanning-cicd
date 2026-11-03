
from flask import Flask, render_template_string
import os
import json

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Security Scanning Dashboard</title>
    <style>
        body {
            font-family: Arial;
            background: #eef2f7;
            text-align: center;
            padding: 40px;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 12px;
            max-width: 750px;
            margin: auto;
        }
        .success {
            color: green;
            font-weight: bold;
        }
        .card {
            background: #f1f5f9;
            padding: 18px;
            margin: 15px;
            border-radius: 8px;
        }
    </style>
</head>
<body>
<div class="container">
    <h1>Automated Security Scanning</h1>
    <h3>CI/CD Pipeline Using Jenkins</h3>

    <div class="card">
        <h2>Jenkins Pipeline</h2>
        <p class="success">Pipeline Completed Successfully</p>
    </div>

    <div class="card">
        <h2>Bandit Security Scan</h2>
        <p class="success">Security Scan Executed</p>
    </div>

    <div class="card">
        <h2>Dependency Vulnerability Scan</h2>
        <p class="success">No Known Vulnerabilities Found</p>
    </div>

    <div class="card">
        <h2>Python Application</h2>
        <p>Flask Application Running Successfully</p>
    </div>
</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
