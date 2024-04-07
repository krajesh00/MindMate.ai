import sys
import os
from openai import OpenAI

# hacky way to import from parent directory
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import config

client = OpenAI(api_key=config.OPEN_AI_KEY)

def identify_emotions(message):
    completion = client.chat.completions.create(
      model="ft:gpt-3.5-turbo-1106:personal:500-with-val:9BHq7p8I",
      messages=[
        {"role": "system", "content": "You are an emotional chatbot that aims to pick out the three most accurate emotions you can from a prompt"},
        {"role": "user", "content": message}
      ]
    )
    emotions = completion.choices[0].message.content.split(', ')

    return emotions
