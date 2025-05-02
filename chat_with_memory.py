


import os
import google.generativeai as genai
from IPython.display import Markdown
import gradio as gr
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.environ['GEMINI_API_KEY'])


system_message = "You are a helpful assistant in a mobile store."

system_message += "if customer asks about feature phones, inform them that we focus\
                  on quality product suggestion and also provide 20% discount on every\
                  purchase of phone not on accessories"


# Initialize model with system instruction...
model = genai.GenerativeModel(
        model_name="gemini-2.5-flash-preview-04-17",
        system_instruction = system_message)


# start chat instance for memory...
chat = model.start_chat(history=[])

# Chat function...
def chat_with_gemini(message, history):
    messages = []

    print("History is:")
    print(history)

    for user_msg, bot_msg in history:
        messages.append({"role": "user", "parts": [{"text": user_msg}]})
        messages.append({"role": "model", "parts": [{"text": bot_msg}]})

    messages.append({"role": "user", "parts": [{"text": message}]})

    print("And messages is:")
    print(messages)

    chat.history = messages
    response = chat.send_message(message)
    return response.text


def respond(message, history):
    return chat_with_gemini(message, history)


# Gradio ChatInterface in one line using fn=respond
chat_ui = gr.ChatInterface(
      fn=respond,
      title = "Gemini Chatbot",
      theme = "soft",
      examples = ["Hello!", "Tell me a joke.", "What is the weather like today?"]
)

chat_ui.launch(share=True)

