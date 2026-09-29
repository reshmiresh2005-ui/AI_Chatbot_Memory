from google import genai
import time
from memory import ChatMemory

client = genai.Client()

chat = client.chats.create(
    model="gemini-3.8-flash"
)

# Create memory with maximum 6 messages
memory = ChatMemory(max_messages=6)


while True:

    user_input = input("You: ")

    # Show memory
    if user_input.lower() == "memory":
        memory.show_memory()
        continue

    # Exit
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    # Empty input check
    if not user_input.strip():
        print("Chatbot: Please enter something.")
        continue

    # Add user message to memory
    memory.add_message("User: " + user_input)

    try:
        response = chat.send_message(user_input)

        print("Chatbot:", response.text)

        # Add chatbot response to memory
        memory.add_message("Chatbot: " + response.text)

        # Show current memory
        memory.show_memory()

    except Exception as e:

        if "503" in str(e) or "UNAVAILABLE" in str(e):
            print("Chatbot: Gemini is temporarily busy. Please try again later.")
            time.sleep(5)

        else:
            print("Chatbot: Something went wrong.")
            print("Error:", e)