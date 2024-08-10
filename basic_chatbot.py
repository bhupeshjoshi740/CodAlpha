responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there! What can I do for you?",
    "how are you?": "I'm a bot, so I don't have feelings, but thanks for asking!",
    "what is your name?": "I am a simple chatbot created in Python.",
    "bye": "Goodbye! Have a nice day!",
}
def get_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for case-insensitive matching
    for keyword in responses:
        if keyword in user_input:
            return responses[keyword]
    return responses["default"]

def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: " + responses["bye"])
            break
        response = get_response(user_input)
        print("Chatbot: " + response)

if __name__ == "__main__":
    chat()





