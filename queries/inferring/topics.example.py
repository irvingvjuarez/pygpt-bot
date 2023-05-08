import sys
sys.path.append("/home/irving/pygpt-bot/")

from utils.get_completion import get_completion

story = f"""
In a recent survey conducted by the government,
public sector employees were asked to rate their level
of satisfaction with the department they work at.
The results revealed that NASA was the most popular
department with a satisfaction rating of 95%.

One NASA employee, John Smith, commented on the findings,
stating, "I'm not surprised that NASA came out on top.
It's a great place to work with amazing people and
incredible opportunities. I'm proud to be a part of
such an innovative organization."

The results were also welcomed by NASA's management team,
with Director Tom Johnson stating, "We are thrilled to
hear that our employees are satisfied with their work at NASA.
We have a talented and dedicated team who work tirelessly
to achieve our goals, and it's fantastic to see that their
hard work is paying off."

The survey also revealed that the
Social Security Administration had the lowest satisfaction
rating, with only 45% of employees indicating they were
satisfied with their job. The government has pledged to
address the concerns raised by employees in the survey and
work towards improving job satisfaction across all departments.
"""

# Asking for topics in a certain text
prompt1 = f"""
Your task is to identify the topics in the text wrapped \
by triple backticks.

Make each topic one or two words long and format your \
response as a list of items separated by commas

Text: ```{story}```
"""

# Asking if some of certain topics are included in the text
topic_list = [
  "nasa", "local government", "engineering",
  "employee satisfaction", "federal government"
]
prompt2 = f"""
Your task is to determine if some of the topics listed in \
the following list match some of the topics discussed in \
the text wrapped in triple backticks.

Return the items that match in the topic list.
Format your answer as a list of topics divided by commas

Topic list: {topic_list}
Text: ```{story}```
"""

response = get_completion(prompt2)
print(response)