# Iudicium – AI-Powered Symptom Triage

**Live Demo:** [https://iudicium-production.up.railway.app/]

---

## What It Does

Iudicium is a web-based medical triage tool. The user describes symptoms in plain English, and the app uses Claude AI to return:
- **Possible conditions** (2–3)
- **Urgency level** – SELF-CARE, GP, or A&E
- **Recommended next steps**

**Disclaimer:** This is not a diagnosis. Always consult a qualified healthcare professional.

---

## Why I Built This

This project sits at the intersection of AI, healthcare, and social impact – exactly where I want to build my career. I am pursuing an MSc in Medical Robotics and AI at UCL / ETH Zurich, and Iudicium demonstrates my ability to:
- Build full-stack web applications
- Integrate large language models (Claude API)
- Design user‑friendly interfaces
- Apply AI to real‑world medical problems

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Flask (Python) |
| AI Engine | Anthropic Claude 3.5 Sonnet |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Deployment | Railway (live URL) |
| Version Control | Git + GitHub |

---

## How to Run It Locally

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/iudicium.git
cd iudicium

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up API key
# Create a .env file with: ANTHROPIC_API_KEY=sk-ant-your-key-here

# 5. Run the app
python app.py

# 6. Open browser to http://127.0.0.1:5000
