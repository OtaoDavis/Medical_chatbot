from model import MedicalAssistant  

def main():
    assistant = MedicalAssistant()

    print("Welcome to the Medical Chatbot!")
    print("Ask me any medical question or describe symptoms.")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye!")
            break
        
        response = assistant.generate_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
