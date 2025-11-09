🧠 AI-Powered Nutrition & Diet Recommendation System
📋 Overview

The AI-Powered Nutrition and Diet Recommendation System is an intelligent web application that provides personalized meal and diet plans based on user details such as age, gender, height, weight, and fitness goals.
It uses machine learning and deep learning algorithms to analyze user data and generate a customized diet that helps users maintain, gain, or lose weight in a healthy way.

🚀 Features

✅ AI-based personalized diet recommendations
✅ User-friendly Streamlit web interface
✅ Dynamic BMI and calorie calculations
✅ Nutrition analysis based on macro & micro nutrients
✅ Data visualization of diet plans and progress
✅ FastAPI backend for efficient API handling

🛠️ Tech Stack
Component	Technology Used
Frontend	Streamlit
Backend	FastAPI
Machine Learning	Python (Scikit-learn, TensorFlow, or custom model)
Database	SQLite / CSV
Deployment	GitHub / LocalHost
⚙️ Installation & Setup
🧩 1. Clone the Repository
git clone https://github.com/indumathi-27/AI_diet_recommendation.git
cd AI_diet_recommendation

🧩 2. Create Virtual Environment
python -m venv venv

🧩 3. Activate Virtual Environment

Windows (PowerShell)

venv\Scripts\activate


Mac / Linux

source venv/bin/activate

🧩 4. Install Requirements
pip install -r requirements.txt

🧩 5. Run the Backend (FastAPI)
uvicorn app:app --reload

🧩 6. Run the Frontend (Streamlit)

In another terminal window:

streamlit run utils.py


Your app will now be live at
👉 http://localhost:8501/

💡 How It Works

User enters details (age, gender, height, weight, activity level, goals).

Model predicts ideal calorie and nutrient intake.

System generates AI-based meal and diet plan.

User can visualize nutrition breakdown and track daily progress.

🧮 Sample Input & Output

Input:

Age: 22

Gender: Female

Height: 160 cm

Weight: 55 kg

Goal: Maintain Weight

Output:

Recommended Calories: ~2000 kcal/day

Breakfast: Oats with fruits & milk

Lunch: Brown rice, dal, and salad

Dinner: Grilled vegetables with chapati
