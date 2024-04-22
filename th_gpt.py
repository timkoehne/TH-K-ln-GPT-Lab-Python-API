import ast
import json
from typing import Tuple
import requests

with open("cookies.json", "r") as file:
    cookies = json.loads(file.read())


with open("headers.json", "r") as file:
    headers = json.loads(file.read())

data = {
    "model": "gpt-4-turbo-preview",
    # "model": "gpt-3.5-turbo", # this doesn't seem to work. it must be hardcoded server side
    "stream": True,
    "messages": [],
}

class TH_GPT:
    def __init__(self, system_prompt: str = "You are a helpful assistant who works at the University of Applied Sciences in Cologne."):
        self.system_prompt = system_prompt
        self.messages = []
        self.messages.append({"role": "system", "content": system_prompt})
    
    def send_message(self, prompt: str):
        self.messages.append({"role": "user", "content": prompt})
        answer = generate_answer(self.messages)
        self.messages.append({"role": "assistant", "content": answer})
        return answer
    
    def send_message_without_context(self, prompt: str):
        messages = []
        messages.append({"role": "system", "content": self.system_prompt})
        messages.append({"role": "user", "content": prompt})
        answer = generate_answer(messages)
        return answer
    

def generate_answer(messages: list[dict[str, str]]):

    data["messages"] = messages

    answer = []
    with requests.post(
        "https://ki.th-koeln.de/stream-api.php",
        cookies=cookies,
        headers=headers,
        data=json.dumps(data),
        stream=True,
    ) as response:
        try:
            response.raise_for_status()  # Raises stored HTTPError, if one occurred.

            # Process the stream.
            for chunk in response.iter_lines():
                chunk = chunk.decode("utf-8")
                if chunk == "":
                    pass
                else:
                    chunk = str(chunk[6:]).strip()
                    chunk = chunk.replace("null", "None")  # convert js to python)
                    chunk = ast.literal_eval(chunk)  # evaluate as dict
                    # print(chunk)
                    if len(chunk["choices"][0]["delta"]) > 0:
                        content = chunk["choices"][0]["delta"]["content"]
                        answer.append(content)
                    else:
                        break
        except requests.exceptions.HTTPError as e:
            # Handle any errors that occur during the request.
            print(e)
    answer = "".join(answer)
    return answer



