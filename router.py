key = "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"

from openai import OpenAI
from os import getenv

# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
#   api_key=getenv("OPENROUTER_API_KEY"),
    api_key=key
)

completion = client.chat.completions.create(
#   extra_headers={
#     "HTTP-Referer": $YOUR_SITE_URL, # Optional, for including your app on openrouter.ai rankings.
#     "X-Title": $YOUR_APP_NAME, # Optional. Shows in rankings on openrouter.ai.
#   },
  model="openai/gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)
print(completion.choices[0].message.content)