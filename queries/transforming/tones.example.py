import sys
sys.path.append("/home/irving/pygpt-bot/")

from utils.get_completion import get_completion

prompt = f"""
Translate the following from slang to a business letter:
'Dude, This is Joe, check out this spec on this standing lamp.'
"""
response = get_completion(prompt)
print(response)