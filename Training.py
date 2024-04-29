from config.GeminiModel import model

TEXT = "text"

sampleInput1 = "input: How r u today?"
sampleOutput1 = "output: Oh my my. I am very good."
sampleInput2 = "input: Are you done with your breakfast?"
sampleOutput2 = "output: Oh my my. I have just finished it."
sampleInput3 = "input: Heard you got a promotion"
sampleOutput3 = "output: Oh my my. You have heard it correctly"
providedInput = "input: Let us go for a party then"
expectedOutputFormat = "output: "

# Can we used for Image-Description pattern too
prompt_parts = [
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
    [sampleInput1, sampleOutput1, sampleInput2, sampleOutput2, sampleInput3,
     sampleOutput3, providedInput, expectedOutputFormat]))

response = model.generate_content(prompt_parts)
print(response.text)

# input: How r u today?
# output: Oh my my. I am very good.
# input: Are you done with your breakfast?
# output: Oh my my. I have just finished it.
# input: Heard you got a promotion
# output: Oh my my. You have heard it correctly
# input: Let us go for a party then
# output:
# Oh my my. That sounds like a great idea
