import nltk
import random
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('punkt_tab')
# Predefined responses
responses = {
    "hello": ["Hello! How can I help you?", "Hi there!", "Hello Krutika!"],
    "hi": ["Hi!", "Hello!", "Hey!"],
    "how are you": ["I am fine!", "Doing great!", "I'm good, thanks!"],
    "your name": ["I am a chatbot created using NLP.", "You can call me AI Chatbot."],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a nice day."]
}

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    tokens = word_tokenize(user_input)

    response_found = False

    for key in responses:
        if key in user_input:
            print("Chatbot:", random.choice(responses[key]))
            response_found = True
            break

    if not response_found:
        print("Chatbot: Sorry, I didn't understand that.")

    if "bye" in user_input:
        break