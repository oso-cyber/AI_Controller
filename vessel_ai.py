import google.generativeai as genai
import json
import os

# 1. SETUP - Replace with your key
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel('gemini-1.5-flash')

# Path to the 'Nerve' folder
project_path = r"C:\unreal\fvessel\Content\Data"
full_path = os.path.join(project_path, "active_power.json")

def manifest_power(description):
    prompt = f"""
    Act as an Unreal Engine Physics Architect. Describe: "{description}" 
    Return ONLY a JSON object with:
    - "viscosity": (0.0 to 1.0)
    - "volatility": (0.0 to 100.0)
    - "gravity_influence": (-1.0 to 1.0)
    - "color_hex": Hex code.
    """
    response = model.generate_content(prompt)
    clean_json = response.text.strip().replace('```json', '').replace('```', '')
    
    if not os.path.exists(project_path): os.makedirs(project_path)
    with open(full_path, 'w') as f:
        f.write(clean_json)
    print(f"AI Sent Physics: {clean_json}")

# Loop for practice
while True:
    cmd = input("Describe power: ")
    if cmd == "exit": break
    manifest_power(cmd)