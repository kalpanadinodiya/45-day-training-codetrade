import pandas as pd
from google import genai
from config import GEMINI_API_KEY

# Configure Gemini
client = genai.Client(api_key=GEMINI_API_KEY)

prompts = [
    "What is Artificial Intelligence?",
    "Explain Machine Learning.",
    "What is Deep Learning?",
    "What is Generative AI?",
    "Give three applications of AI."
]

records = []

TOTAL_TOKENS = 0
TOTAL_COST = 0

# Approximate cost (example for educational purpose)
COST_PER_1000_TOKENS = 0.0003

for prompt in prompts:

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    answer = response.text

    # Estimate tokens
    prompt_tokens = len(prompt.split())
    response_tokens = len(answer.split())
    total_tokens = prompt_tokens + response_tokens

    estimated_cost = (total_tokens / 1000) * COST_PER_1000_TOKENS

    TOTAL_TOKENS += total_tokens
    TOTAL_COST += estimated_cost

    records.append({
        "Prompt": prompt,
        "Response": answer,
        "Prompt Tokens": prompt_tokens,
        "Response Tokens": response_tokens,
        "Total Tokens": total_tokens,
        "Estimated Cost ($)": round(estimated_cost, 6)
    })

df = pd.DataFrame(records)

df.to_csv("token_usage_log.csv", index=False)

print("="*60)
print("FINAL USAGE REPORT")
print("="*60)

print(f"Total Requests : {len(prompts)}")
print(f"Total Tokens   : {TOTAL_TOKENS}")
print(f"Total Cost ($) : {TOTAL_COST:.6f}")

print("\nToken log saved as token_usage_log.csv")