from google import genai
from config import GEMINI_API_KEY

# Create client
client = genai.Client(api_key=GEMINI_API_KEY)

# Chat history
history = [
    {
        "role": "user",
        "parts": [{"text": "You are a helpful AI assistant. Give clear and concise answers."}]
    }
]

print("=" * 60)
print("Streaming AI Chat Assistant")
print("Type 'exit' to quit")
print("=" * 60)

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("\nGoodbye!")
        break

    history.append(
        {
            "role": "user",
            "parts": [{"text": user_input}]
        }
    )

    print("\nAssistant: ", end="", flush=True)

    full_response = ""

    response = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=history
    )

    for chunk in response:
        if chunk.text:
            print(chunk.text, end="", flush=True)
            full_response += chunk.text

    print()

    history.append(
        {
            "role": "model",
            "parts": [{"text": full_response}]
        }
    )