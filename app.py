from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Demo data for the Health360 dashboard.
# Replace these sample values with your own dataset when available.
SUMMARY = {
    "patients": 12480,
    "high_risk": 18.6,
    "avg_age": 46.8,
    "conditions": 8
}

DISEASES = [
    {"name": "Diabetes", "patients": 2180, "risk": "High", "rate": 17.5},
    {"name": "Hypertension", "patients": 2940, "risk": "High", "rate": 23.6},
    {"name": "Cardiovascular", "patients": 1420, "risk": "High", "rate": 11.4},
    {"name": "Asthma", "patients": 1180, "risk": "Moderate", "rate": 9.5},
    {"name": "Kidney disease", "patients": 760, "risk": "Moderate", "rate": 6.1},
    {"name": "Obesity", "patients": 2260, "risk": "Moderate", "rate": 18.1},
    {"name": "Arthritis", "patients": 1020, "risk": "Low", "rate": 8.2},
    {"name": "Other", "patients": 720, "risk": "Low", "rate": 5.8},
]

AGE_GROUPS = [
    {"label": "18–29", "value": 12},
    {"label": "30–39", "value": 18},
    {"label": "40–49", "value": 24},
    {"label": "50–59", "value": 22},
    {"label": "60–69", "value": 16},
    {"label": "70+", "value": 8},
]

@app.route("/")
def dashboard():
    return render_template(
        "index.html",
        summary=SUMMARY,
        diseases=DISEASES,
        age_groups=AGE_GROUPS
    )

@app.route("/api/overview")
def overview():
    return jsonify({"summary": SUMMARY, "diseases": DISEASES, "age_groups": AGE_GROUPS})

if __name__ == "__main__":
    # Run with: python app.py
    app.run(debug=True)
