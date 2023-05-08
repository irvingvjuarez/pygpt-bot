import sys
sys.path.append("/home/irving/pygpt-bot/")

from utils.get_completion import get_completion

prod_review = """
Got this panda plush toy for my daughter's birthday, \
who loves it and takes it everywhere. It's soft and \
super cute, and its face has a friendly look. It's \
a bit small for what I paid though. I think there \
might be other options that are bigger for the \
same price. It arrived a day earlier than expected, \
so I got to play with it myself before I gave it \
to her.
"""

prompt = f"""
Your task is to extract relevant information from \
a product review from an ecommerce site to give \
feedback to the shipping department.

From the review below, delimited by triple backticks \
extract the information relevant to shipping and \
delivery. Limit to answer to max 30 words.

Review: ```{prod_review}```
"""

response = get_completion(prompt)
print(response)