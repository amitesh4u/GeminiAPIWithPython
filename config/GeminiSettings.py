from jproperties import Properties

configs = Properties()

with open('./config/config.properties', 'rb') as config_file:
    configs.load(config_file)

_config_temperature = float(configs.get("TEMPERATURE").data)
_config_top_p = float(configs.get("TOP_P").data)
_config_top_k = int(configs.get("TOP_K").data)
_config_max_output_token = int(configs.get("MAX_OUTPUT_TOKENS").data)
_config_candidate_count = int(configs.get("CANDIDATE_COUNT").data)

_safety_harm_category_harassment = configs.get("HARM_CATEGORY_HARASSMENT_LEVEL").data
_safety_harm_category_speech = configs.get("HARM_CATEGORY_HATE_SPEECH_LEVEL").data
_safety_harm_category_sexually_explicit = configs.get("HARM_CATEGORY_SEXUALLY_EXPLICIT_LEVEL").data
_safety_harm_category_dangerous_content = configs.get("HARM_CATEGORY_DANGEROUS_CONTENT_LEVEL").data


# Set up the model
generation_config = {
  "temperature": _config_temperature,
  "top_p": _config_top_p,
  "top_k": _config_top_k,
  "max_output_tokens": _config_max_output_token,
  "candidate_count": _config_candidate_count,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": f"{_safety_harm_category_harassment}"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": f"{_safety_harm_category_speech}"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": f"{_safety_harm_category_sexually_explicit}"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": f"{_safety_harm_category_dangerous_content}"
  },
]

gemini_api_key = configs.get("GEMINI_API_KEY").data
gemini_model = configs.get("GEMINI_MODEL").data
gemini_vision_model = configs.get("GEMINI_VISION_MODEL").data
