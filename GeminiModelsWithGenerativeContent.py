from config.GeminiModel import genai

for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
      print(model.name + " : " + model.display_name)
