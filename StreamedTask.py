from config.GeminiModel import model

query = "give me a summary of Gemini AI"
prompt_parts = [
  query
]

print("Me: " + query + "\n")

response = model.generate_content(prompt_parts, stream=True)
for chunk in response:
    print(chunk.text)


# Me: give me a summary of Gemini AI
#
# **Gemini AI**
#
# Gemini AI is a multimodal AI platform developed by Google AI.
# It combines the strengths of various AI models into a single, cohesive system.
#
# **Key Features:**
#
# * **Text-to-Text Generation:** Generates coherent and contextually relevant
# text for different tasks, such as story writing, translation, and
# summarization.
#
# * **Code Generation:** Writes and completes code in multiple programming
# languages, making it a valuable tool for programmers and researchers.
#
# * **Image Generation:** Creates high-quality images from text descriptions,
# enabling the creation of realistic and visually appealing artwork.
#
# * **Music Generation:** Composes music in various styles, allowing musicians
# and music enthusiasts to explore new creative possibilities.
#
# * **Multimodal Intelligence:** Combines text, code, images, and music
# capabilities to foster cross-modal understanding and enhance problem-solving
# abilities.
#
# * **Cloud-Based Platform:** Deployed on Google's cloud infrastructure,
# providing scalability and accessibility for a wide range of users.
#
# **Applications:**
#
# Gemini AI finds applications in various fields, including:
#
# * Natural language processing
# * Software engineering
# * Creative arts
# * Education
# * Healthcare
#
# **Benefits:**
#
# * **Augmented Creativity:** Enhances human creativity by providing
# AI-generated suggestions and ideas.
#
# * **Improved Efficiency:** Automates repetitive tasks, freeing up users to
# focus on higher-level work.
#
#
# * **Personalized Experiences:** Tailors results to individual preferences
# and context.
#
# * **Innovation:** Drives advancements in AI research and development.
