import sys
sys.path.append("/home/irving/pygpt-bot/")

from utils.get_completion import get_completion

prompt = f"""
Tell me which language this is and it's meaning in English:
```Combien coûte le lampadaire?```
"""

response = get_completion(prompt)
print(response)