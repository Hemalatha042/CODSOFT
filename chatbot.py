import re
def chatbot():
    print("Hello! I am a simple chatbot. Type 'bye' to end the chat.") 
    while True:
        user_input = input("You: ").lower()  
        if user_input in ['bye', 'goodbye', 'exit']:
            print("ChatBot: Goodbye! Have a nice day!")
            break
        
        elif re.search(r"hello|hi|hey", user_input):
            print("ChatBot: Hello! How can I help you today?")
            
        elif re.search(r"what is your name", user_input):
                print("ChatBot: I'm a chatbot. You can call me ChatBot!")
            
        elif re.search(r"how are you", user_input):
            print("ChatBot: I'm doing great, thank you! How about you?")
    
        elif re.search(r"your favorite color", user_input):
            print("ChatBot: I don't have a favorite color, but I like all colors!")
        
        elif re.search(r"what is your hobby", user_input):
            print("ChatBot: i don't have any hobby,i help people to solve their querries")
        
        elif re.search(r"thank you|thanks", user_input):
            print("ChatBot: You're welcome!")
        
        else:
            print("ChatBot: Sorry, I didn't understand that. Can you ask something else?")
chatbot()