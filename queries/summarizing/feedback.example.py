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

# Plain and simple prompt
prompt1 = f"""
Your task is to generate a short summary of a product \
review from an ecommerce site.

Summarize the review below, delimited by triple backticks, \
in at most 30 words.

Review: ```{prod_review}```
"""

# Prompt focused on giving feedback
# for a certain part of your business
# In this case the shipping department
prompt2 = f"""
Your task is to generate a short summary of a product \
review from an ecommerce site in order to provide \
feedback to the shipping department.

Summarize the review below, delimited by triple backticks, \
in at most 30 words, and focusing on any aspects \
that mention shipping and delivery of the product.

Review: ```{prod_review}```
"""

# Giving feedback to the pricing department
prompt3 = f"""
Your task is to generate a short summary of a product \
review from an ecommerce site to give feedback to the \
price department.

Summarize the review below, delimited by triple backticks, \
in at most 30 words, and focusing on price aspects mentioned \
about the product.

Review: ```{prod_review}```
"""

response = get_completion(prompt3)
print(response)