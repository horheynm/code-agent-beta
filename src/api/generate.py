from openai import OpenAI
from dotenv import dotenv_values


class Client:

    def __init__(self, backend: str = "openai", env: str = ".env"):
        self.backend = backend
        self.config = dotenv_values(env)

    def generate(self, prompt: str, model: str = "gpt-3.5-turbo"):

        if self.backend == "openai":
            try:
                client = OpenAI(
                    # This is the default and can be omitted
                    api_key=self.config.get("OPENAI_API_KEY"),
                )

                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                    model=model,
                )
                return {
                    "id": chat_completion.id,
                    "content": chat_completion.choices[0].message.content,
                    "usage": chat_completion.usage.dict(),
                }
            except Exception as err:
                raise err
