import google.generativeai as genai

def generate_nutrition_tip_with_flash(goal):
    prompt = f"Give a concise nutrition or recovery tip for {goal}."
    response = genai.GeminiFlash.generate_text(prompt=prompt)
    return response.text
