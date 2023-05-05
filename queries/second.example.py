import sys
sys.path.append("/home/irving/pygpt-bot/")

from utils.get_completion import get_completion

prompt = f"""
Generate a list of three made-up book titles along \
with their authors and genres.
Provide them in JSON format with the following keys:
book_id, title, author, genre.

book_id data type is a uuid
titile is a string
author is an array of strings
genre is an array of strings
"""
response = get_completion(prompt)
print(response)

# Example Response

# [
#   {
#     "book_id": "d7c5f5c5-7c5d-4c5d-8c5d-5c5d7c5f5c5d",
#     "title": "The Last Voyage of the Starship Andromeda",
#     "author": ["Ava Lee", "Jared Kim"],
#     "genre": ["Science Fiction", "Adventure"]
#   },
#   {
#     "book_id": "f5c5d7c5-5c5d-7c5d-5c5d-d7c5f5c5d7c5",
#     "title": "The Secret Life of Beeswax",
#     "author": ["Lila Chen"],
#     "genre": ["Mystery", "Historical Fiction"]
#   },
#   {
#     "book_id": "7c5d5c5d-d7c5f5c5-5c5d-7c5d-5c5d7c5f5c5d",
#     "title": "The Art of Forgetting",
#     "author": ["Ethan Wong"],
#     "genre": ["Contemporary Fiction", "Romance"]
#   }
# ]