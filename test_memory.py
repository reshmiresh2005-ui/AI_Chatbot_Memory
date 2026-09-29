from memory import ChatMemory

# Create memory with maximum 6 messages
memory = ChatMemory(max_messages=6)

# Add messages
memory.add_message("User: My name is Resh")
memory.add_message("Chatbot: Nice to meet you, Resh!")

memory.add_message("User: I am learning Python")
memory.add_message("Chatbot: That's great!")

memory.add_message("User: I like data analysis")
memory.add_message("Chatbot: Data analysis is useful!")

# Show memory
memory.show_memory()

# Add another message
memory.add_message("User: Tell me about AI")

# Show memory again
memory.show_memory()