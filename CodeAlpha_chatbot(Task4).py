# Simple Rule-Based Chatbot

def chatbot():
    print("Chatbot: Hello!Welcome.  \n Type 'bye' to end the chat.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi!")
        
        elif user_input == "hi":
            print("Chatbot: Hello,How do your doing?")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print("Chatbot: I am a simple chatbot.")

        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break 
        
        elif user_input == "who created you":
            print("Chatbot: I was created using Python.")

        elif user_input == "what can you do":
             print("Chatbot: I can answer simple questions.")

        elif user_input == "good morning":
             print("Chatbot: Good morning! Have a great day.")

        elif user_input == "good night":
             print("Chatbot: Good night! Sweet dreams.")

        elif user_input == "thank you":
             print("Chatbot: You're welcome!")

        elif user_input == "where are you from":
             print("Chatbot: I live inside this computer.")
             
        elif user_input == "tell me a joke":
            print("Chatbot: Why did the computer go to school? To improve its bytes!")
         
        else:
            print("Chatbot: Sorry, I don't understand")
             
# Run the chatbot
chatbot()