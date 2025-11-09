# Run the project locally (VS Code)

1. Install Python 3.8+ and create a venv:
   ```
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   .\venv\Scripts\activate  # Windows PowerShell
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```
   streamlit run app.py
   ```
   The app will open in your browser at http://localhost:8501

# How to push to GitHub (simple commands)

1. Create a new repository on GitHub (do not initialize with README).
2. In your project folder:
   ```
   git init
   git add .
   git commit -m "Initial commit - AI Nutrition & Diet Recommendation"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git push -u origin main
   ```

If Git prompts for username/password, use your GitHub credentials or a personal access token.

Good luck with your submission!
