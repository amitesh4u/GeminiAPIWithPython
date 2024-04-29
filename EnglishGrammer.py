from config.GeminiModel import model

query = ("Find the parts of speech in this sentence."
         "The quick brown fox instantly jumps over a lazy dog.")

print("Me: " + query)

prompt_parts = [
  query
]

response = model.generate_content(prompt_parts)
print(response.text)


# Me: Find the parts of speech in this sentence.
# The quick brown fox instantly jumps over a lazy dog.

# The: article
# quick: adjective
# brown: adjective
# fox: noun
# instantly: adverb
# jumps: verb
# over: preposition
# a: article
# lazy: adjective
# dog: noun
