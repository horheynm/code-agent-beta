from typing import List, Dict, Optional
from openai import OpenAI

from api.constant import *
import re


import os
from dotenv import dotenv_values
from api.func_call import completion_call


@completion_call
def get_file_paths(files: List[str]) -> List[str]:
    """Given paths of files, return each file path as a List"""
    return files


class ChatCompletion:

    def __init__(
        self,
        openai_key: str,
        model: str,
        language: str = "python",
    ):
        self.model = model
        self.language = language
        self.client = OpenAI(api_key=openai_key)

    def generate(self, prompt: str) -> str:
        """
        Given a prompt, return code only
        """
        messages = [
            {
                "role": "system",
                "content": CHAT_COMPLETION_SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": CONTENT_PROMPT.format(prompt),
            },
            {
                "role": "user",
                "content": CHAT_COMPLETION_CODE_GEN_USER_PROMPT.format(self.language),
            },
        ]
        return self.make_request(messages=messages)

    def make_request(
        self,
        messages: List[Dict],
        temperature: float = 0.7,
        stream: bool = False,
        **kwargs,
    ):
        print(
            "LLM inference with ",
            f"model: {self.model}",
            f"temperature: {temperature}",
            f"message keys: {list(messages[0].keys())}",
            f"params: {list(kwargs.keys())}",
        )
        response = self.client.chat.completions.create(
            model=self.model,
            temperature=temperature,
            messages=messages,
            stream=stream,
            **kwargs,
        )

        # if stream:
        #     for chunk in response:
        #         if "choices" in chunk and len(chunk["choices"]) > 0:
        #             if (
        #                 "delta" in chunk["choices"][0]
        #                 and "content" in chunk["choices"][0]["delta"]
        #             ):
        #                 yield chunk["choices"][0]["delta"]["content"]
        # else:

        message = response.choices[0].message
        return message.content
