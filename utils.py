
import math
from datetime import datetime, timedelta

def _bmi(weight, height_cm):
    h = height_cm/100
    return weight / (h*h)

def _activity_factor(activity_label):
    mapping = {
        "Sedentary (little/no exercise)": 1.2,
        "Light (1-3 days/week)": 1.375,
        "Moderate (3-5 days/week)": 1.55,
        "Active (6-7 days/week)": 1.725,
        "Very Active (physical job)": 1.9
    }
    return mapping.get(activity_label,1.2)

def kcal_estimate(user):
    # Mifflin-St Jeor
    w = user['weight_kg']
    h = user['height_cm']
    a = user['age']
    gender = user['gender']
    if gender.lower().startswith('m'):
        bmr = 10*w + 6.25*h - 5*a + 5
    else:
        bmr = 10*w + 6.25*h - 5*a - 161
    return bmr * _activity_factor(user['activity'])

def recommend_diet(user):
    """
    Lightweight scoring engine that selects one of:
    - Balanced
    - High Protein
    - Low Carb (Keto-friendly)
    - Vegan / Plant-Based
    - Weight Loss (Calorie deficit)
    """
    scores = {"Balanced":0,"High Protein":0,"Low Carb":0,"Vegan":0,"Weight Loss":0}
    bmi = _bmi(user['weight_kg'], user['height_cm'])
    # Goals influence
    if user['goal']=="Lose weight":
        scores["Weight Loss"] += 3
        scores["Low Carb"] += 1
    elif user['goal']=="Gain muscle / weight":
        scores["High Protein"] += 3
        scores["Balanced"] += 1
    else:
        scores["Balanced"] += 2

    # Diet pref
    pref = user.get("diet_pref","No preference")
    if pref=="Vegetarian":
        scores["Vegan"] += 1
        scores["Balanced"] += 1
    if pref=="Vegan":
        scores["Vegan"] += 3
    if pref=="Pescatarian":
        scores["Balanced"] += 2
    if pref=="Keto/Low-carb":
        scores["Low Carb"] += 3
        scores["High Protein"] += 1

    # BMI signals
    if bmi >= 25:
        scores["Weight Loss"] += 2
    if bmi < 18.5:
        scores["Balanced"] += 1
        scores["High Protein"] += 1

    # Activity
    if user['activity'].startswith("Active") or user['activity'].startswith("Very"):
        scores["High Protein"] += 1

    # Allergies reduce some categories
    allergies = user.get("allergies",[])
    if "Seafood" in allergies:
        # Pescatarian less likely
        scores["Balanced"] -= 1
    if "Dairy" in allergies:
        scores["High Protein"] -= 1

    # final selection
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top = sorted_scores[0][0]
    # ensure non-negative display
    return top, scores

def macro_split_text(diet_category, goal):
    if diet_category=="High Protein":
        return "Protein 35-40%, Carbs 30-35%, Fat 25-30% — focus on lean proteins and complex carbs."
    if diet_category=="Low Carb":
        return "Protein 30-40%, Carbs 10-20%, Fat 40-50% — lower carbs, higher healthy fats."
    if diet_category=="Vegan":
        return "Protein 20-25% (plant sources), Carbs 45-55%, Fat 20-30% — include legumes, tofu, nuts."
    if diet_category=="Weight Loss":
        return "Create a 300-700 kcal deficit from maintenance; balanced macros around Protein 25-30%."
    return "Protein 20-30%, Carbs 40-50%, Fat 20-30% — a balanced diet."

# Sample meal templates (simple)
_MEALS = {
    "Balanced": {
        "breakfast":"Oats porridge with milk, banana and almonds",
        "lunch":"Grilled chicken (or tofu), brown rice, mixed vegetables",
        "snack":"Greek yogurt with honey / fruit",
        "dinner":"Baked fish / lentil curry, salad, quinoa"
    },
    "High Protein": {
        "breakfast":"Egg-white omelette with spinach and whole grain toast",
        "lunch":"Grilled chicken breast, sweet potato, broccoli",
        "snack":"Cottage cheese / protein shake",
        "dinner":"Stir-fried tofu/lean beef with vegetables"
    },
    "Low Carb": {
        "breakfast":"Greek yogurt with seeds and berries",
        "lunch":"Grilled salmon / paneer with large salad",
        "snack":"Mixed nuts (if not allergic)",
        "dinner":"Zucchini noodles with pesto and chicken"
    },
    "Vegan": {
        "breakfast":"Smoothie bowl with soy yogurt, oats and fruits",
        "lunch":"Chickpea salad with quinoa and avocado",
        "snack":"Hummus with carrot sticks",
        "dinner":"Tofu curry with brown rice"
    },
    "Weight Loss": {
        "breakfast":"Poha / upma with veggies",
        "lunch":"Grilled veg wrap with hummus",
        "snack":"Fruit / green tea",
        "dinner":"Mixed vegetable soup and salad"
    }
}

def sample_meal_plan(category, allergies):
    plan = {}
    today = datetime.now().date()
    for i in range(7):
        day = (today + timedelta(days=i)).strftime("%A, %d %b")
        template = _MEALS.get(category, _MEALS['Balanced']).copy()
        # remove allergen items simply by note (basic)
        if "Nuts" in allergies:
            template['snack'] = template['snack'].replace("nuts","seeds")
        if "Dairy" in allergies:
            template = {k:v.replace("milk","soy milk").replace("Greek yogurt","soy yogurt") for k,v in template.items()}
        kcal = 1800 + (i%3)*50  # rough est per day
        template['kcal'] = kcal
        plan[day] = template
    return plan
