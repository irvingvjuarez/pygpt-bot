import sys
sys.path.append("/home/irving/pygpt-bot/")

from utils.get_completion import get_completion

lamp_review = """
Needed a nice lamp for my bedroom, and this one had \
additional storage and not too high of a price point. \
Got it fast.  The string to our lamp broke during the \
transit and the company happily sent over a new one. \
Came within a few days as well. It was easy to put \
together.  I had a missing part, so I contacted their \
support and they very quickly got me the missing piece! \
Lumina seems to me to be a great company that cares \
about their customers and products!!
"""

# Identify the sentiment of the review
prompt1 = f"""
Your task is to determine the sentiment of the product review \
wrapper in triple backticks.

Product review: ```{lamp_review}```
"""

# Looking for a set of emotions in the review
prompt2 = f"""
Your task is to idenitfy a list of emotions that the writer \
of the product review is expressing. Include no more than \
five items in the list. Format your answer as a list of \
lower-case words separated by commas.

Review text: ```{lamp_review}```
"""

response = get_completion(prompt2)
print(response)