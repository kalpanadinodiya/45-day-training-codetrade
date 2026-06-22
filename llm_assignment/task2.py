import time
import pandas as pd
import requests
import google.generativeai as genai

from config import GEMINI_API_KEY, OPENROUTER_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
gemini_model = genai.GenerativeModel("gemini-2.5-flash")

# Read prompts
prompts = pd.read_csv("prompts.csv")

results = []

for index, row in prompts.iterrows():

    prompt = row["Prompt"]

    print("=" * 80)
    print(f"Prompt {row['Prompt ID']}")
    print(prompt)
    print("=" * 80)

    # ---------------- GEMINI ----------------
    start = time.time()

    gemini_response = gemini_model.generate_content(prompt)

    gemini_time = round(time.time() - start, 2)

    gemini_text = gemini_response.text

    # ---------------- OPENROUTER ----------------

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "openrouter/free",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    start = time.time()

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )

    openrouter_time = round(time.time() - start, 2)

    result = response.json()

    if "choices" in result:
        openrouter_text = result["choices"][0]["message"]["content"]
    else:
        openrouter_text = str(result)

    print("\nGemini Response:\n")
    print(gemini_text)

    print("\nOpenRouter Response:\n")
    print(openrouter_text)

    results.append({
        "Prompt ID": row["Prompt ID"],
        "Prompt": prompt,
        "Gemini Response": gemini_text,
        "Gemini Time": gemini_time,
        "OpenRouter Response": openrouter_text,
        "OpenRouter Time": openrouter_time
    })

# Save Results
df = pd.DataFrame(results)

df.to_csv("task2_results.csv", index=False)

print("\n\nTask 2 Completed Successfully!")
print("Results saved in task2_results.csv")