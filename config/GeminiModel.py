import google.generativeai as genai

from config.GeminiSettings import generation_config, safety_settings, \
  gemini_api_key, \
  gemini_model, gemini_vision_model

genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel(model_name=gemini_model,
                              generation_config=generation_config,
                              safety_settings=safety_settings)

vision_model = genai.GenerativeModel(model_name=gemini_vision_model,
                                     generation_config=generation_config,
                                     safety_settings=safety_settings)
