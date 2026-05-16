from interactions_services import create_interaction

def main():
    previous_interaction_id = None
    message = input("Enter your message: ")
    while message.lower() != "exit":
        response = create_interaction(message, previous_interaction_id)
        if response:
            previous_interaction_id = response.id
            print("Interaction ID:", previous_interaction_id)
            print("Response:", response.output_text)
        message = input("Enter your message: ")

if __name__ == "__main__":
    main()