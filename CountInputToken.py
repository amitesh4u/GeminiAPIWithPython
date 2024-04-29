from config.GeminiModel import model

query = ("summarize this in 5-6 bullet points: 'Mohandas Karamchand Gandhi 2 "
         "October 1869 – 30 January 1948) was an Indian lawyer, "
         "anti-colonial nationalist and political ethicist who   employed "
         "nonviolent resistance to lead the successful campaign for   "
         "India/'s independence from British rule. He inspired movements for "
         "civil   rights and freedom across the world. The honorific Mahātmā "
         "(from Sanskrit   /'great-souled, venerable/'), first applied to "
         "him in South Africa in   1914, is now used throughout the world.   "
         "Born and raised in a Hindu family in coastal Gujarat, Gandhi "
         "trained in   the law at the Inner Temple in London, and was called "
         "to the bar in June   1891, at the age of 22. After two uncertain "
         "years in India, where he was   unable to start a successful law "
         "practice, he moved to South Africa in   1893 to represent an "
         "Indian merchant in a lawsuit. He went on to live in   South Africa "
         "for 21 years.")

prompt_parts = [
  query
]

response = model.count_tokens(prompt_parts)
print(response)
