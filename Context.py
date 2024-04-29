from config.GeminiModel import model

# Prefer to add as many data points for better response
query = ("I am not happy with my current salary of $100000 for the role of "
         "Software Engineer. I have 6 years of experience in Python, Java, "
         "Spring. Help me draft a letter to my manager Mr. Smith indicating "
         "that I'm very interested in the job role but need higher "
         "compensation.")

prompt_parts = [
  query
]

print("Me: " + query + "\n")

response = model.generate_content(prompt_parts)
print(response.text)
