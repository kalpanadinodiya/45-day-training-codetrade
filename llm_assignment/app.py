import time
import requests
import google.generativeai as genai

from config import GEMINI_API_KEY, OPENROUTER_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

prompt = "Explain Artificial Intelligence in simple words."

# ---------------- GEMINI ----------------

start = time.time()

gemini = genai.GenerativeModel("gemini-2.5-flash")

gemini_response = gemini.generate_content(prompt)

gemini_time = time.time() - start

print("="*60)
print("GEMINI RESPONSE")
print("="*60)
print(gemini_response.text)
print(f"\nResponse Time: {gemini_time:.2f} sec")
print(f"Response Length: {len(gemini_response.text)}")

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

openrouter_time = time.time() - start

result = response.json()

print(response.status_code)
print(result)

print("\n")
print("="*60)
print("OPENROUTER RESPONSE")
print("="*60)

if "choices" in result:
    print(result["choices"][0]["message"]["content"])

    print(f"\nResponse Time: {openrouter_time:.2f} sec")
    print(
        f"Response Length: {len(result['choices'][0]['message']['content'])}"
    )
else:
    print("OpenRouter Error:")
    print(result)

import pandas as pd

data = {
    "Provider": ["Gemini", "OpenRouter"],
    "Model": [
        "gemini-2.5-flash",
        result["model"]
    ],
    "Response Time (sec)": [
        round(gemini_time, 2),
        round(openrouter_time, 2)
    ],
    "Response Length": [
        len(gemini_response.text),
        len(result["choices"][0]["message"]["content"])
    ]
}

df = pd.DataFrame(data)

df.to_csv("results.csv", index=False)

print("\nResults saved to results.csv")