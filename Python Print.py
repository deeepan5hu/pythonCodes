import random

def greet():
    greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!"]
    print(random.choice(greetings))

def chat():
    responses = {
        "how are you?": "I'm good, thank you for asking!",
        "what's your name?": "I'm a chatbot, you can call me ChatGPT.",
        "bye": "Goodbye! Have a great day!",
        "default": "Hello!! how can I help you today?Hi."
    }

    print("Welcome to the chatbot! How can I assist you?")
    
    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print(responses["bye"])
            break
        response = responses.get(user_input, responses["default"])
        print("Chatbot:", response)

if __name__ == "__main__":
    greet()
    chat()
