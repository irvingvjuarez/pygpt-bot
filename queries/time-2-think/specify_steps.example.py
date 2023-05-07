import sys
sys.path.append("/home/irving/pygpt-bot/")

from utils.get_completion import get_completion

text = f"""
In a charming village, siblings Jack and Jill set out on \
a quest to fetch water from a hilltop \
well. As they climbed, singing joyfully, misfortune \
struck—Jack tripped on a stone and tumbled \
down the hill, with Jill following suit. \
Though slightly battered, the pair returned home to \
comforting embraces. Despite the mishap, \
their adventurous spirits remained undimmed, and they \
continued exploring with delight.
"""

# example 1
prompt_1 = f"""
Perform the following actions:
1. Summarize the following text delimited by triple backticks \
in one sentence.
2. Translate the summary into French.
3. List each name in the French summary.
4. Output a JSON object that contains the following \
keys: french_summary, num_names.

Separate your answers with line breaks.

Text:
```{text}```
"""

# example 2: asking for output in a specified format
prompt_2 = f"""
Your task is to perform the following actions:
1. Summarize the following text delimited by \
triple backticks with one sentence.
2. Translate the summary into French.
3. List each name in the French summary
4. Output a json object that contains the \
following keys: french_summary, num_names.

Use the following format:
Text: <text to summarize>
Summary: <summary>
Translation: <summary translation>
Names: <list of names in French summary>
Output JSON: <json with summary and num_names>

Text to summarize:
```{text}```
"""

response = get_completion(prompt_2)
print(response)