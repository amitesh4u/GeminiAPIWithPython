from config.GeminiModel import model

query = ("generate me a two color palette based on following sentence: \n"
         "'We sat by the fire as the snow fell'")

prompt_parts = [
  query
]
print("Me: " + query + "\n")

response = model.generate_content(prompt_parts)
print(response.text)

# Me: generate me a two color palette based on following sentence:
# 'We sat by the fire as the snow fell'
#
# * #bb0028 (burgundy)
# * #0099cc (ice blue)
