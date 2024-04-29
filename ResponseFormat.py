from config.GeminiModel import model

# Getting data in Text, JSON and HTML
query = "What is world's current population in Text, JSON and HTML formats?"

prompt_parts = [
  query
]

print("Me: " + query + "\n")

response = model.generate_content(prompt_parts)
print(response.text)

# Me: What is world's current population in Text, JSON and HTML formats?
#
# **Text:**
#
# As of today, the world's population is estimated to be approximately
# 8,057,417,000.
#
# **JSON:**
#
# ```json
# {
#   "world_population": 8057417000
# }
# ```
#
# **HTML:**
#
# ```html
# <!DOCTYPE html>
# <html>
# <body>
#
# <p>As of today, the world's population is estimated to be approximately
# 8,057,417,000.</p>
#
# </body>
# </html>
# ```
