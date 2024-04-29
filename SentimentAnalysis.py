from config.GeminiModel import model

query = ("analyze the sentiment as positive or negative for following "
         "sentences: \n"
         "'I love pasta'\n"
         "'I hate London rain'\n"
         "'Should I change my Job?'\n"
         "'I don't know about next rain in Karnataka'")

prompt_parts = [
  query
]

print("Me: " + query + "\n")

response = model.generate_content(prompt_parts)
print(response.text)


# Me: analyze the sentiment as positive or negative for following sentences:
#   'I love pasta'
# 'I hate London rain'
# 'Should I change my Job?'
# 'I don't know about next rain in Karnataka'
# **Sentence 1: 'I love pasta'**
# Sentiment: Positive
#
# **Sentence 2: 'I hate London rain'**
# Sentiment: Negative
#
# **Sentence 3: 'Should I change my Job?'** Sentiment: Neutral (the sentence
# expresses uncertainty rather than a clear positive or negative sentiment)
#
# **Sentence 4: 'I don't know about next rain in Karnataka'** Sentiment:
# Neutral (the sentence conveys a lack of information rather than a clear
# positive or negative sentiment)
