from config.GeminiModel import model

TEXT = "text"

query = ("Give the hexadecimal color code for the items based on provided "
         "samples")
sampleInput1 = "input: mango"
sampleOutput1 = "output: {\n\"hex\" : \"#FFCC33\"\n}"
sampleInput2 = "input: orange"
sampleOutput2 = "output: {\n\"hex\" : \"#FFA500\"\n}"
sampleInput3 = "input: cucumber"
sampleOutput3 = "output: {\n\"hex\" : \"#00AF40\"\n}"
providedInput = "input: strawberry"
expectedOutputFormat = "output: "

# Can we used for Image-Description pattern too
prompt_parts = [
  {TEXT: query},
  {TEXT: sampleInput1},
  {TEXT: sampleOutput1},
  {TEXT: sampleInput2},
  {TEXT: sampleInput2},
  {TEXT: sampleInput3},
  {TEXT: sampleOutput3},
  {TEXT: providedInput},
  {TEXT: expectedOutputFormat}
]

print("\n".join(
    [query, sampleInput1, sampleOutput1, sampleInput2, sampleOutput2,
     sampleInput3, sampleOutput3, providedInput, expectedOutputFormat]))

response = model.generate_content(prompt_parts)
print(response.text)
