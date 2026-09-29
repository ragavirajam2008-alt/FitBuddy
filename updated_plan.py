import google.generativeai as genai
from app.database import get_original_plan

def update_workout_plan(user_id, feedback):
    original_plan = get_original_plan(user_id)
    prompt = f"Update this workout plan based on feedback: {feedback}\nPlan:\n{original_plan}"
    response = genai.GeminiPro.generate_text(prompt=prompt)
    return response.text
