from config.GeminiModel import model

chat = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["Hi. How are you?"]
  },
  {
    "role": "model",
    "parts": ["I am doing fine. Thanks for asking."]
  },
  {
    "role": "user",
    "parts": ["What are you doing today?"]
  },
  {
    "role": "model",
    "parts": ["Just surfing web and waiting for any task to perform"]
  },
])

print("Chat History before conversation:\n" + str(chat.history))

message = "I have one for you. Should I ask?"
print("Me: " + message)
reply = chat.send_message(message)
print("Gemini: " + reply.text)

message = "What's your favorite fruit?"
print("Me: " + message)
reply = chat.send_message(message)
print("Gemini: " + reply.text)

message = "What is today's date?"
print("Me: " + message)
reply = chat.send_message(message)
print("Gemini: " + reply.text)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\nComplete Chat History after conversation: \n" + str(chat.history))
