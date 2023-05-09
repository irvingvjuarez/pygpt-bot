import sys
sys.path.append("/home/irving/pygpt-bot/")

from utils.get_completion import get_completion

user_messages = [
  "La performance du système est plus lente que d'habitude.",  # System performance is slower than normal
  "Mi monitor tiene píxeles que no se iluminan.",              # My monitor has pixels that are not lighting
  "Il mio mouse non funziona",                                 # My mouse is not working
  "Mój klawisz Ctrl jest zepsuty",                             # My keyboard has a broken control key
  "我的屏幕在闪烁"                                               # My screen is flashing
]

prompt = f"""
Your task is to determine which language is used in \
the following text messages as well as its translation \
to English.

Format your answer as follows:
<Message No #>
<original message>
<Language>
<Translation>

Messages: ```{user_messages}```
"""
response = get_completion(prompt)
print(response)