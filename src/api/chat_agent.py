from typing import List, Dict
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


class ChatAgent:

    def __init__(self, model: str, env: str = ".env"):
        self.model = model
        config = dotenv_values(env)

        self.client = OpenAI(
            # This is the default and can be omitted
            api_key=config.get("OPENAI_API_KEY"),
        )

    def create_plan(self, prompt: str, path: str):
        print("Planning...")
        messages = [
            {
                "role": "system",
                "content": SYSTEM_CONTENT,
            },
            {
                "role": "user",
                "content": CONTENT_PROMPT.format(prompt),
            },
        ]

        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)

        content = self.make_request(messages)

        with open(path, "w") as f:
            f.write(content)

    def execute_plan(
        self,
        prompt: str,
        path: str,
    ):
        print("Execting plan...")
        with open(path, "r", encoding="utf-8") as file:
            plan = file.read()

        function_call = {"name": "get_file_paths"}
        functions = [get_file_paths.schema]

        messages = [
            {
                "role": "system",
                "content": EXECUTE_PLAN_SYSTEM_PROMPT,
            },
            {"role": "user", "content": USER_PROMPT.format(prompt)},
            {"role": "user", "content": EXECUTE_PLAN_USER_PROMPT.format(plan)},
        ]

        response = self.make_request(
            function_call=function_call,
            functions=functions,
            messages=messages,
        )
        return response

    def code_gen(
        self,
        path: str,
        plan: str,
        prompt: str,
        files: List[str],
    ):

        for file in files:
            print(f"Generating code for {file}")
            current_file = os.path.abspath(
                os.path.join(
                    path,
                    file,
                )
            )
            messages = [
                {
                    "role": "system",
                    "content": CODE_GEN_SYSTEM_PROMPT.format(
                        SYSTEM_PROMPT, current_file
                    ),
                },
                {
                    "role": "user",
                    "content": EXECUTE_PLAN_USER_PROMPT.format(plan),
                },
                {
                    "role": "user",
                    "content": CONTENT_PROMPT.format(prompt),
                },
                {
                    "role": "user",
                    "content": CODE_GEN_USER_PROMPT.format(current_file),
                },
            ]

            response = self.make_request(messages=messages)

            pattern = r"```[\w\s]*\n([\s\S]*?)```"
            code_blocks = re.findall(pattern, response, re.MULTILINE)
            code = code_blocks[0] if code_blocks else response

            # save code into a file
            os.makedirs(os.path.dirname(current_file), exist_ok=True)

            with open(current_file, "w") as file:
                # Write the string into the file
                file.write(code)

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
        if "function_call" in kwargs:
            func_name = kwargs.get("function_call")["name"]
            # Get the function object from the string
            func = globals()[func_name]
            return func.from_response(response)

        message = response.choices[0].message
        return message.content
