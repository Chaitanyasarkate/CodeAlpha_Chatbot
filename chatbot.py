
def chatbot_response(user_input):
    user_input = user_input.lower()  
    
    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you?"
    elif "how are you" in user_input:
        return "I'm fine, thanks for asking! How about you?"
    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
        return "Goodbye! Have a great day!"
    elif "help" in user_input:
        return "You can say hello, ask how I am, or say bye to end the chat."
    else:
        return "I'm sorry, I didn't understand that. Can you rephrase?"

def run_chatbot():
    print("=== Welcome to CodeAlpha Chatbot ===")
    print("Type 'bye', 'exit' or 'quit' to end the chat.\n")
    
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)
        
        if "Goodbye" in response:
            break

if __name__ == "__main__":
    run_chatbot()
