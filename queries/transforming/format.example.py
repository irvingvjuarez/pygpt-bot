import sys
sys.path.append("/home/irving/pygpt-bot/")

from utils.get_completion import get_completion

data_json = {
  "resturant employees" : [
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
    {"name":"Bob", "email":"bob32@gmail.com"},
    {"name":"Jai", "email":"jai87@gmail.com"}
	]
}

prompt = f"""
Your task is to translate the following python dictionary \
from JSON to a HTML table with column headers and title.

JSON: ```{data_json}```
"""

response = get_completion(prompt)
print(response)