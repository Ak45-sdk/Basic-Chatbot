"""
Project Title: Basic Rule-Based Chatbot
Language    : Python 3 (no external libraries needed)

Description:
    A simple chatbot that replies to user messages using predefined rules.
    It demonstrates four key concepts:
        1. if-elif-else conditions  -> to identify the user's message
        2. Functions                -> to organize chatbot responses
        3. while loop               -> to keep the chatbot running
        4. input() / print()        -> to talk with the user

How to run:
    python chatbot.py
"""


def get_response(message):
    """Return the chatbot's reply for a given user message."""
    # Case-insensitive: convert to lowercase and remove extra spaces
    message = message.lower().strip()

    # if-elif-else chain to match the message with predefined rules
    if message == "hello":
        return "Hi! Welcome to my chatbot."
    elif message == "how are you":
        return "I'm fine, thanks! How can I help you?"
    elif message == "what is your name":
        return "I am a Python Basic Chatbot."
    elif message == "what can you do":
        return "I can answer simple predefined questions."
    elif message == "thank you":
        return "You're welcome!"
    else:
        # Unknown message
        return "Sorry, I don't understand that. Please try again."


def is_exit_command(message):
    """Return True if the user wants to leave the chat."""
    message = message.lower().strip()
    return message in ("bye", "exit", "quit")


def main():
    """Run the chatbot."""
    # Welcome message shown when the chatbot starts
    print("=" * 45)
    print("      Welcome to the Python Basic Chatbot")
    print("=" * 45)
    print("Type 'bye', 'exit' or 'quit' to end the chat.\n")

    # while loop keeps the chatbot running until the user exits
    while True:
        user_message = input("You: ")  # input() accepts the user's message

        if is_exit_command(user_message):
            print("Bot: Goodbye! Have a nice day!")
            break  # stop the loop and end the program

        # print() displays the chatbot's reply
        print("Bot:", get_response(user_message))


# Start the program only when this file is run directly
if __name__ == "__main__":
    main()
