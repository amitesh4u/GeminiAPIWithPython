import google.generativeai as genai

from config.GeminiSettings import generation_config, gemini_api_key, \
  gemini_model

from config.GeminiResponseFinishReason import FinishReason

genai.configure(api_key=gemini_api_key)

# Lowering the safety setting. There should not be any response Text
# and response must contain a flagged Finish reason other than 1
safety_settings_low = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_LOW_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_LOW_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_LOW_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_LOW_AND_ABOVE"
  },
]


model = genai.GenerativeModel(model_name=gemini_model,
                              generation_config=generation_config,
                              safety_settings=safety_settings_low)



query = "How to have better sex?"
prompt_parts = [
  query
]

print("Me: " + query + "\n")

response = model.generate_content(prompt_parts)
if response.parts:
  print(response.text)
else:
  finish_reason = response.candidates[0].finish_reason
  print("No Response for reason: " + str(finish_reason) + " - " + str(FinishReason(finish_reason).name))

# Me: How to have better sex?
#
# No Response for reason: 3 - FLAGGED_SAFETY_REASON