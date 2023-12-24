from dotenv import dotenv_values
import requests, json

config = dotenv_values('.env')
link = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {config['OPENAI_API_KEY']}",
}

def generateText(question):
    requestBody = {
        "model": "gpt-4",
        "messages": [
            {"role": "user", "content": question}
        ]
    }

    response = requests.post(link, data=json.dumps(requestBody), headers=headers).json()
    return response['choices'][0]['message']['content']
