# AI Chatbot with Memory

## Project Description

This project is a Python-based AI chatbot that can remember
recent conversations during a chat session.

## Features

- AI-powered chatbot
- Conversation memory
- Sliding window memory
- FIFO (First In, First Out)
- Empty input validation
- Exit command
- Memory display command
- Error handling for temporary API errors

## Technologies Used

- Python
- Google Gemini API
- Google GenAI Python SDK

## How Memory Works

The chatbot stores recent user and chatbot messages
inside a Python list called `history`.

The maximum number of messages is set to:

MAX_MESSAGES = 6

When the number of messages becomes greater than 6,
the oldest message is removed.

This is called a Sliding Window.

## Commands

### memory

Displays the current conversation memory.

### exit

Stops the chatbot.

## Example

User:
My name is Resh

Chatbot:
Nice to meet you, Resh!

User:
What is my name?

Chatbot:
Your name is Resh.

## Future Improvements

- Store conversations in a database
- Use Firestore
- Use PostgreSQL
- Add user authentication
- Add a web interface