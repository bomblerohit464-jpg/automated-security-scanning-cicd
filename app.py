from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Automated Security Scanning</title>
        <style>
            body {
                font-family: Arial;
                background: #eef2f7;
                text-align: center;
                padding: 50px;
            }
            .container {
                background: white;
                padding: 40px;
                border-radius: 12px;
                max-width: 700px;
                margin: auto;
            }
            h1 { color: #173b65; }
            .success {
                color: green;
                font-weight: bold;
            }
            button {
                background: #1769aa;
                color: white;
                padding: 12px 25px;
                border: none;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Automated Security Scanning in CI/CD</h1>
            <h3>GitHub + Jenkins Integration</h3>
            <p class="success">Application Running Successfully!</p>
            <p>Automated Python Security Scanning</p>
            <p>Bandit - Source Code Security Scanner</p>
            <p>pip-audit - Dependency Vulnerability Scanner</p>
            <button onclick="alert('Security Scanning Project')">
                Check Project
            </button>
        </div>
    </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)