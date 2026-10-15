import json
import os
from pathlib import Path

from flask import Flask, jsonify, render_template

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
REPORT_DIR = BASE_DIR / "reports"


def load_report(filename):
    path = REPORT_DIR / filename

    if not path.exists():
        return None

    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def get_summary():
    bandit = load_report("bandit-report.json")
    audit = load_report("pip-audit.json")

    bandit_results = bandit.get("results", []) if bandit else []
    dependency_results = audit if isinstance(audit, list) else (
        audit.get("dependencies", []) if audit else []
    )

    return {
        "reports_available": {
            "bandit": bandit is not None,
            "dependency_audit": audit is not None,
        },
        "bandit": {
            "findings": len(bandit_results),
            "high": sum(
                1 for item in bandit_results
                if item.get("issue_severity", "").upper() == "HIGH"
            ),
            "medium": sum(
                1 for item in bandit_results
                if item.get("issue_severity", "").upper() == "MEDIUM"
            ),
            "low": sum(
                1 for item in bandit_results
                if item.get("issue_severity", "").upper() == "LOW"
            ),
        },
        "dependency_audit": {
            "vulnerable_dependencies": len(dependency_results)
        },
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/status")
def status():
    return jsonify(get_summary())


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=int(os.environ.get("PORT", "5000")),
        debug=False,
    )
