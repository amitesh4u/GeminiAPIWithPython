from config.GeminiModel import model

chat = model.start_chat()
print("Chat History before conversation: " + str(chat.history))

message = "Hi. How are you?"
print("Me: " + message)
reply = chat.send_message(message)
print("Gemini: " + reply.text)

message = "What's your favorite color?"
print("Me: " + message)
reply = chat.send_message(message)
print("Gemini: " + reply.text)

message = "What day is today?"
print("Me: " + message)
reply = chat.send_message(message)
print("Gemini: " + reply.text)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\nComplete Chat History after conversation: \n" + str(chat.history))
