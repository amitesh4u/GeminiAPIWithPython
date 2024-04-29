from config.GeminiModel import model

query = "find the missing number 2,6,18, ,162, 486"

prompt_parts = [
  query
]

print("Me: " + query + "\n")

response = model.generate_content(prompt_parts)
print(response.text)

# Me: find the missing number 2,6,18, ,162, 486
#
# The missing number in the sequence is 54.
#
# This sequence follows a pattern of multiplying the previous number by 3.
#
# Here's the breakdown:
#
# 2 * 3 = 6
# 6 * 3 = 18
# 18 * 3 = 54
# 54 * 3 = 162
# 162 * 3 = 486
