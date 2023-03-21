import openai

openai.api_key = "sk-<your-key>"


completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me 3 ideas for apps I could build with openai apis "}])
print(completion.choices[0].message.content)

completion1 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Write a blog post on redhat openshift"}])
print(completion1.choices[0].message.content)