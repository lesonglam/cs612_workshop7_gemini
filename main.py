import os
from dotenv import load_dotenv
from google import genai

# Load .env file and get key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

# chat loop
print("💬 Gemini Chat — type 'exit' to quit\n")

# Store message history
history = []

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in {"exit", "quit"}:
        print(" Goodbye!")
        break

    # Add user message to history
    history.append({"role": "user", "parts": [{"text": user_input}]})

    # Send entire conversation for context
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=history
    )

    reply = response.text
    print(f"Gemini: {reply}\n")

    # Add model response back to history
    history.append({"role": "model", "parts": [{"text": reply}]})
