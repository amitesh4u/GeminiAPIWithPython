from config.GeminiModel import model

query = "tell me a joke"
prompt_parts = [
  query
]

print("Me: " + query + "\n")

response = model.generate_content(prompt_parts)
print(response.text)

# Me: tell me a joke
#
# Why don't scientists trust atoms?
# Because they make up everything!
