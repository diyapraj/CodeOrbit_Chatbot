# Simple Rule-Based Chatbot
# This chatbot uses if-elif-else statements to match keywords in user input
# and return predefined responses. If no keyword matches, it uses a fallback response.

def chatbot_response(user_input):
    user_input = user_input.lower()  # convert input to lowercase for easy matching

    # Rule 1: Greetings
    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    
    # Rule 2: Asking how the bot is doing
    elif "how are you" in user_input:
        return "I'm just code, but I'm doing great! How about you?"
    
    # Rule 3: Asking the bot's name
    elif "your name" in user_input:
        return "I'm CodeOrbit Bot, your friendly assistant!"
    
    # Rule 4: Exit condition
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    
    # Fallback response for anything the bot doesn't recognize
    else:
        return "Sorry, I don't understand that. Can you rephrase?"


# Main loop - keeps running until user types 'bye'
print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Chatbot:", response)
    
    if "bye" in user_input.lower():
        break