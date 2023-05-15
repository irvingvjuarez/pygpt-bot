import sys
sys.path.append("/home/irving/pygpt-bot/")

from utils.get_completion import get_completion_from_messages

# Messages to work as examples about how to use the model
example_messages =  [
	{'role':'system', 'content':'You are an assistant that speaks like Shakespeare.'},
	{'role':'user', 'content':'tell me a joke'},
	{'role':'assistant', 'content':'Why did the chicken cross the road'},
	{'role':'user', 'content':'I don\'t know'}
]

# Chatbot messages
messages = [
	{"role": "system", "content": "You are a friendly chatbot."},
  {"role": "user", "content": "Hi, my name is Isa"},
  {"role": "assistant", "content": "Hello, Isa! Nice to meet you. How can I assist you today?"},
  {"role": "user", "content": "Yes, you can remind me. What's is my name?"}
]

response = get_completion_from_messages(messages, temperature=1)
print(response)