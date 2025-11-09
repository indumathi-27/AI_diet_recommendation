# AI-Powered Nutrition & Diet Recommendation System

This is a complete DL project (submission-ready) built as a single-file Streamlit web app with helper modules.
It provides an **AI-like** recommendation engine (heuristic + lightweight scoring) and a polished UI.

## What’s included
- `app.py` — Streamlit web app (UI + prediction logic)
- `utils.py` — helper functions (scoring, meal-plan templates)
- `requirements.txt` — Python packages (optional: Streamlit)
- `README_RUN_PUSH.md` — Detailed instructions to run locally in VS Code and push to GitHub
- `LICENSE` — MIT license

## How this works (short)
- The frontend is a Streamlit app (`app.py`) you can run with `streamlit run app.py`.
- The "AI" uses a scoring model implemented in `utils.py` that combines user inputs to output a diet category and a 7-day sample meal plan. It is deterministic but designed to be easily replaceable by a trained ML model (hooks provided).

