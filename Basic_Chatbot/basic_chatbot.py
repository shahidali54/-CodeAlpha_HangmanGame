def chatbot():
    print("Welcome to the Chatbot! Type 'bye' to exit.")

    # Predefined responses
    responses = {
        "hello": "Hi!",
        "hi": "Hello there!",
        "how are you": "I'm fine, thanks!",
        "bye": "Goodbye!"
    }

    # Main loop
    while True:
        # Get user input
        user_input = input("You: ").lower().strip()

        # Check for matching response
        if user_input in responses:
            print("Bot:", responses[user_input])
            if user_input == "bye":
                break
        else:
            print("Bot: Sorry, I don't understand. Try 'hello', 'how are you', or 'bye'.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()