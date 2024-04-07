from openai import OpenAI

client = OpenAI(api_key='<----- KEY GOES HERE ------->')


message = "I don't have an appetite" # Template message


completion = client.chat.completions.create(
  model="ft:gpt-3.5-turbo-1106:personal:500-with-val:9BHq7p8I",
  messages=[
    {"role": "system", "content": "You are an emotional chatbot that aims to pick out the three most accurate emotions you can from a prompt"},
    {"role": "user", "content": message}
  ]
)


print(completion.choices[0].message)
