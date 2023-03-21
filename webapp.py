import openai
import gradio

# gpt-3.5-turbo

openai.api_key = "sk-<your-key>"

messages = [{"role": "system", "content": "You are a cloud expert and specialized in designing the cloud solutions"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Cloud Chat Bot")

demo.launch(share=True)