from config.GeminiModel import model

query = "write a java code to parse and solve mathematical equations"

prompt_parts = [
  query
]
print("Me: " + query + "\n")

response = model.generate_content(prompt_parts)
print(response.text)
