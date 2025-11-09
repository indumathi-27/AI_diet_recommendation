
import streamlit as st
from utils import recommend_diet, sample_meal_plan, kcal_estimate, macro_split_text

st.set_page_config(page_title="AI Nutrition & Diet Recom.", layout="centered")
st.title("🍎 AI‑Powered Nutrition & Diet Recommendation System")
st.markdown("""
This project produces a personalized diet recommendation and a 7‑day sample meal plan.
It uses a compact, explainable scoring engine (can be swapped with an ML model).
""")

with st.form("user_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name", value="Student")
        age = st.number_input("Age", min_value=10, max_value=100, value=22)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        height_cm = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)
    with col2:
        weight_kg = st.number_input("Weight (kg)", min_value=30, max_value=250, value=70)
        activity = st.selectbox("Activity level",
                                ["Sedentary (little/no exercise)","Light (1-3 days/week)",
                                 "Moderate (3-5 days/week)","Active (6-7 days/week)","Very Active (physical job)"])
        goal = st.selectbox("Goal", ["Lose weight","Maintain weight","Gain muscle / weight"])
        diet_pref = st.selectbox("Dietary preference", ["No preference","Vegetarian","Vegan","Pescatarian","Keto/Low-carb"])
    allergies = st.multiselect("Allergies / Avoids", ["None","Gluten","Dairy","Nuts","Eggs","Soy","Seafood","Red meat"])

    submitted = st.form_submit_button("Get Recommendation")

if submitted:
    user = dict(name=name, age=age, gender=gender, height_cm=height_cm,
                weight_kg=weight_kg, activity=activity, goal=goal,
                diet_pref=diet_pref, allergies=allergies)
    diet_category, score_breakdown = recommend_diet(user)
    st.success(f"Recommended diet: **{diet_category}**")
    st.write("Why this recommendation? (score breakdown)")
    st.json(score_breakdown)

    est_kcal = kcal_estimate(user)
    st.markdown(f"**Estimated daily calories target:** {int(est_kcal)} kcal")
    st.markdown("**Suggested macronutrient split:**")
    st.write(macro_split_text(diet_category, goal))

    st.subheader("7-day sample meal plan")
    plan = sample_meal_plan(diet_category, user.get("allergies", []))
    for day, meals in plan.items():
        st.markdown(f"**{day}** — kcal ~ {meals.get('kcal', 'est')}")
        st.markdown(f"- Breakfast: {meals['breakfast']}")
        st.markdown(f"- Lunch: {meals['lunch']}")
        st.markdown(f"- Snack: {meals['snack']}")
        st.markdown(f"- Dinner: {meals['dinner']}")
        st.write("---")

    st.info("This prototype is built for demonstration. For higher accuracy replace `recommend_diet` with a trained ML/Deep Learning model (hooks provided).")
    st.markdown("### Export / Save")
    if st.button("Download recommendation as JSON"):
        import json, streamlit as _st
        _st.download_button("Download JSON", json.dumps({"user":user,"diet":diet_category,"plan":plan}, indent=2), file_name="recommendation.json")
