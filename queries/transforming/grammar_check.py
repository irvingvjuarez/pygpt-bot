import sys
sys.path.append("/home/irving/pygpt-bot/")

from utils.get_completion import get_completion

# Grammar checking for several sentences at once
texts = [
  "The girl with the black and white puppies have a ball.",  # The girl has a ball.
  "Yolanda has her notebook.", # ok
  "Its going to be a long day. Does the car need it’s oil changed?",  # Homonyms
  "Their goes my freedom. There going to bring they’re suitcases.",  # Homonyms
  "Your going to need you’re notebook.",  # Homonyms
  "That medicine effects my ability to sleep. Have you heard of the butterfly affect?", # Homonyms
  "This phrase is to cherck chatGPT for speling abilitty"  # spelling
]
prompt1 = f"""
Your task is to check the grammar from the sentences wrapped in triple backticks \
and correct the grammatical errors if they exists.

In case the sentence is correct, return: Correct sentence.
Otherwise, return the sentence corrected.

Use the following format to return your answer:
<Sentence Number #>
<Response>

Sentences: ```{texts}```
"""

# Grammar checking for a longer paragraph
product_review = f"""
Got this for my daughter for her birthday cuz she keeps taking \
mine from my room.  Yes, adults also like pandas too.  She takes \
it everywhere with her, and it's super soft and cute.  One of the \
ears is a bit lower than the other, and I don't think that was \
designed to be asymmetrical. It's a bit small for what I paid for it \
though. I think there might be other options that are bigger for \
the same price.  It arrived a day earlier than expected, so I got \
to play with it myself before I gave it to my daughter.
"""
prompt2 = f"""
Proofread and correct the text wrapped by triple backticks:

Text: ```{product_review}```
"""

# Asking for a more formal correction and transformation
prompt3 = f"""
Proofread and correct the text wrapped by triple backticks. \
Make it more compelling and ensure it follows APA style guide \
and targets and advanced reader.

Text: ```{product_review}```
"""

response = get_completion(prompt3)
print(response)