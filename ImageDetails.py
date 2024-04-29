from pathlib import Path

from config.GeminiModel import vision_model

image_url = "./resource/image0.jpg"
if not (img := Path(image_url)).exists():
    raise FileNotFoundError(f"Could not find the image: {img}")

query = "Describe this image.\n"
img_data = Path(image_url).read_bytes()

print("Me: " + query + "\n " + image_url + "\n")

prompt_parts = [
  query,
  {
    "mime_type": "image/jpeg",
    "data": img_data
  }
]
response = vision_model.generate_content(prompt_parts)
print(response.text)

# Me: Describe this image.
#
# ./resource/image0.jpg
#
# A ginger cat is sitting on a green lawn and looking at the camera. The cat
# has green eyes and a pink nose. Its fur is short and well-groomed. The cat
# is sitting in a relaxed position with its tail wrapped around its paws. The
# background of the image is a green lawn, which is blurred, so the cat
# stands out.
