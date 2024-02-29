import openai

class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        ).choices[0].message['content']
        return response

if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Tell me about birds")
    print(response)
