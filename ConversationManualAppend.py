from config.GeminiModel import model

query1 = "Me: What is world's population?"
print(query1)

prompt_parts = [
  query1
]

response1 = model.generate_content(prompt_parts)
print(response1.text)

query2 = "multiply world's population with world's population."
print("Me: " + query2)

# We need to pass complete previous conversation for context
prompt_parts = [
  query1,
  response1.text,
  query2
]

response2 = model.generate_content(prompt_parts)
print(response2.text)

# Me: What is world's population?
# As of August 24, 2023, the world's population is estimated to be approximately 8,042,624,819.
# Me: multiply world's population with world's population.
# 8,042,624,819 * 8,042,624,819 = 64,695,804,630,110,691