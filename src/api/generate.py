from openai import OpenAI
from dotenv import dotenv_values

import logging

logger = logging.getLogger(__name__)


class Client:

    def __init__(self, backend: str = "openai", env: str = ".env"):
        self.backend = backend
        self.config = dotenv_values(env)

    def generate(self, prompt: str, model: str = "gpt-3.5-turbo"):

        logger.info(("Making api request to openai. ", f"Model: {model}"))

        if self.backend == "openai":
            try:
                client = OpenAI(
                    # This is the default and can be omitted
                    api_key=self.config.get("OPENAI_API_KEY"),
                )

                response = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                    model=model,
                )
                logger.info("Api response recieved")
                return {
                    "id": response.id,
                    "content": response.choices[0].message.content,
                    "usage": response.usage.dict(),
                }

            except Exception as err:
                raise err
