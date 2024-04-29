from config.GeminiModel import model

query1 = ("summarize this in 5-6 bullet points: 'Mohandas Karamchand Gandhi 2 "
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
          "for 21 years. There, Gandhi raised a family and first   employed "
          "nonviolent resistance in a campaign for civil rights. In 1915,   "
          "aged 45, he returned to India and soon set about organising "
          "peasants,   farmers, and urban labourers to protest against "
          "discrimination and   excessive land-tax.   Assuming leadership of "
          "the Indian National Congress in 1921, Gandhi led   nationwide "
          "campaigns for easing poverty, expanding women \'s rights,   "
          "building religious and ethnic amity, ending untouchability, and,   "
          "above all, achieving swaraj or self-rule. Gandhi adopted the short "
          "dhoti   woven with hand-spun yarn as a mark of identification with "
          "India \'s rural   poor. He began to live in a self-sufficient "
          "residential community, to eat   simple food, and undertake long "
          "fasts as a means of both introspection and   political protest. "
          "Bringing anti-colonial nationalism to the common   Indians, "
          "Gandhi led them in challenging the British-imposed salt tax with   "
          "the 400 km (250 mi) Dandi Salt March in 1930 and in calling for "
          "the   British to quit India in 1942. He was imprisoned many times "
          "and for many   years in both South Africa and India.   Gandhi \'s "
          "vision of an independent India based on religious pluralism was   "
          "challenged in the early 1940s by a Muslim nationalism which "
          "demanded a   separate homeland for Muslims within British India. "
          "In August 1947,   Britain granted independence, but the British "
          "Indian Empire was   partitioned into two dominions, "
          "a Hindu-majority India and a   Muslim-majority Pakistan. As many "
          "displaced Hindus, Muslims, and Sikhs   made their way to their new "
          "lands, religious violence broke out,   especially in the Punjab "
          "and Bengal. Abstaining from the official   celebration of "
          "independence, Gandhi visited the affected areas, attempting   to "
          "alleviate distress. In the months following, he undertook several  "
          " hunger strikes to stop the religious violence. The last of these "
          "was begun   in Delhi on 12 January 1948, when he was 78. The "
          "belief that Gandhi had   been too resolute in his defense of both "
          "Pakistan and Indian Muslims   spread among some Hindus in India. "
          "Among these was Nathuram Godse,   a militant Hindu nationalist "
          "from Pune, western India, who assassinated   Gandhi by firing "
          "three bullets into his chest at an interfaith prayer   meeting in "
          "Delhi on 30 January 1948.   Gandhi \'s birthday, 2 October, "
          "is commemorated in India as Gandhi   Jayanti, a national holiday, "
          "and worldwide as the International Day of   Nonviolence. Gandhi is "
          "considered to be the Father of the Nation in   post-colonial "
          "India. During India \'s nationalist movement and in several   "
          "decades immediately after, he was also commonly called Bapu ("
          "Gujarati   endearment for \'father\', roughly \'papa\',"
          "[2] \'daddy\'[3]).'")

prompt_parts = [
  query1
  ]

print("Me: summarize this in 5-6 bullet points \n Mohandas Karamchand Gandhi 2 "
      "October 1869 – 30 January 1948) was an Indian lawyer, anti-colonial...")

response1 = model.generate_content(prompt_parts)
print(response1.text)

query2 = "extract keywords and dates from the paragraph given earlier"
print("Me: " + query2)

prompt_parts = [
  query1,
  response1.text,
  query2
]

response2 = model.generate_content(prompt_parts)
print(response2.text)


# Me: summarize this in 5-6 bullet points Mohandas Karamchand Gandhi 2
# October 1869 – 30 January 1948) was an Indian lawyer, anti-colonial... -

# **Early Life and Education:
# ** Mohandas Karamchand Gandhi was born in India in 1869 and
# studied law in London.
#
# **Civil Rights Activist in South Africa:
#
# ** From 1893, Gandhi lived in South Africa for 21 years, where he
# led nonviolent resistance campaigns for civil rights. -
#
# **Leadership in India's Independence Movement:
#
# ** Returning to India in 1915, Gandhi became a key figure in the
# Indian National Congress and led nationwide campaigns
# for independence. -
#
# **Philosophy and Practices:
# ** Gandhi practiced nonviolent resistance, advocated for social reforms,
# and promoted religious harmony. -
#
# **Assassination and Legacy:**
# Gandhi was assassinated in 1948, but his teachings continue to inspire
# civil rights and freedom movements worldwide. -
#
# **Honors and Celebrations:** Gandhi's birthday is celebrated
# as Gandhi Jayanti, a national holiday in India, and the International Day
# of Nonviolence.
#
# Me: extract keywords and dates from the paragraph given earlier
#
# **Keywords:**
# - Mohandas Karamchand Gandhi
# - Mahatma
# - Nonviolent resistance
# - Civil rights
# - Indian National Congress
# - Swaraj
# - Dandi Salt March
# - Quit India Movement
# - Partition of India
#
# **Dates:**
# - October 2, 1869: Birth of Gandhi
# - June 1891: Gandhi called to the bar
# - 1893: Gandhi moves to South Africa
# - 1915: Gandhi returns to India
# - 1921: Gandhi becomes leader of the Indian National Congress
# - 1930: Dandi Salt March
# - 1942: Quit India Movement
# - August 1947: India gains independence
# - January 30, 1948: Gandhi is assassinated
