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

prompt = f"""
Your task if to identify the following items from \
a product review:
- Item purchased by the reviewer
- Name of the company that made the item
- Price of the product

Format your answer in a JSON object with "Item", \
"Price" and "Brand" as keys. In case one of the items is \
not provided, set the javascript data type "undefined" as value.

Product review: ```{lamp_review}```
"""

response = get_completion(prompt)
print(response)