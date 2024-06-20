# ref: https://pypi.org/project/openai-functions/

import json
from functools import wraps
from typing import Any, Callable
from pydantic import BaseModel, validate_arguments


def _remove_key_recursively(d, key_to_remove) -> None:
    """Recursively remove a key from a dictionary."""
    if isinstance(d, dict):
        keys = list(d.keys())
        for key in keys:
            if key == key_to_remove:
                del d[key]
            else:
                _remove_key_recursively(d[key], key_to_remove)


class completion_call:
    """
    Decorator to convert a function into an OpenAI function.
    """

    def __init__(self, func: Callable) -> None:
        self.func = func
        self.validate_func = validate_arguments(func)

        parameters = self.validate_func.model.model_json_schema()
        parameters["properties"] = {
            k: v
            for k, v in parameters["properties"].items()
            if k not in ("v__duplicate_kwargs", "args", "kwargs")
        }
        parameters["required"] = sorted(
            k for k, v in parameters["properties"].items() if "default" not in v
        )
        _remove_key_recursively(parameters, "additionalProperties")
        _remove_key_recursively(parameters, "title")
        self.schema = {
            "name": self.func.__name__,
            "description": self.func.__doc__,
            "parameters": parameters,
        }
        self.model = self.validate_func.model

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        @wraps(self.func)
        def wrapper(*args, **kwargs):
            return self.validate_func(*args, **kwargs)

        return wrapper(*args, **kwargs)

    def from_response(self, completion, throw_error=True):
        """
        Parse the response from OpenAI's API and return the function call result.

        Parameters:
            completion (openai.ChatCompletion): The response from OpenAI's API.
            throw_error (bool): Whether to throw an error if the response does not contain a function call.

        Returns:
            any: The result of the function call.
        """
        message = completion.choices[0].message
        if throw_error:
            if hasattr(message, "function_call"):
                assert (
                    message.function_call.name == self.schema["name"]
                ), "Function name does not match"
                _args = message.function_call.arguments

            elif "function_call" in message:
                assert (
                    message.get("function_call").get("name") == self.schema["name"]
                ), "Function name does not match"
                _args = message["function_call"]["arguments"]
            else:
                raise ValueError("No function call detected")

            components = json.loads(_args, strict=False)
            return self.validate_func(**components)

        return eval(message.function_call.arguments)["files"]
