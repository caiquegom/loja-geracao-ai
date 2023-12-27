from dotenv import dotenv_values
import requests, json

config = dotenv_values(".env")
url = "https://api.openai.com/v1/images/generations"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {config['OPENAI_API_KEY']}"
}

def generateImage(prompt):
    requestBody = {
        "model": "dall-e-3",
        "prompt": prompt,
        "n": 1,
        "quality": "hd",
        "size": "1024x1792",
        "style": "vivid"
    }

    response = requests.request("post", url, data=json.dumps(requestBody), headers=headers).json()
    return response['data'][0]['url']

