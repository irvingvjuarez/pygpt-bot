import sys
sys.path.append("/home/irving/pygpt-bot/")

from utils.get_completion import get_completion

# Basic translating skills
prompt1 = f"""
Translate the following English text to Spanish: \
```Hi, I would like to order a blender```
"""

# Translating in more than one language
prompt2 = """
Translate the following text to French and Spanish and English pirate: \
```I want to order a basketball```
"""

# Translating into more than one format of a same language
prompt3 = """
Translate the following text to regular and mexican Spanish \
```How do you feel today, buddie? Ready to start working?```
"""

response = get_completion(prompt3)
print(response)