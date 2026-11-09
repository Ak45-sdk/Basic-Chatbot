# Basic Rule-Based Chatbot (Python)

A beginner-friendly chatbot that replies to user messages using predefined rules.

## Key Concepts Demonstrated

| Concept | Where it is used |
|---|---|
| `if-elif-else` | `get_response()` matches the user's message to a reply |
| Functions | `get_response()`, `is_exit_command()`, `main()` |
| `while` loop | `main()` keeps the chat running until the user exits |
| `input()` / `print()` | `main()` reads the user's message and shows the bot's reply |

## Project Structure

```
basic-chatbot/
├── chatbot.py          # main program
├── test_chatbot.py     # unit tests
├── sample_output.txt   # example chat session
└── README.md           # this file
```

## Requirements

- Python 3.6 or higher
- No external libraries

## How to Run

```bash
python chatbot.py
```

To run the tests:

```bash
python -m unittest test_chatbot.py -v
```

## Supported Conversations

| User types | Bot replies |
|---|---|
| hello | Hi! Welcome to my chatbot. |
| how are you | I'm fine, thanks! How can I help you? |
| what is your name | I am a Python Basic Chatbot. |
| what can you do | I can answer simple predefined questions. |
| thank you | You're welcome! |
| bye / exit / quit | Goodbye! Have a nice day! (program ends) |
| anything else | Sorry, I don't understand that. Please try again. |

Messages are case-insensitive, so `HELLO`, `Hello` and `hello` all work.

## How the Code Works

1. **`get_response(message)`** converts the message to lowercase, removes extra
   spaces, and uses an `if-elif-else` chain to return the matching reply. If
   nothing matches, the `else` branch returns the "don't understand" message.
2. **`is_exit_command(message)`** checks whether the message is `bye`, `exit`
   or `quit` (in any letter case).
3. **`main()`** prints a welcome message and starts a `while True` loop. Each
   time around, it reads input with `input()`. If it is an exit command, the bot
   says goodbye and `break` stops the loop. Otherwise the reply is shown with
   `print()`.

## Sample Session

See `sample_output.txt`.

## Ideas to Extend

- Add more rules, such as `help` or `what is python`.
- Use `in` to match keywords inside longer sentences.
- Store replies in a dictionary instead of `if-elif`.
