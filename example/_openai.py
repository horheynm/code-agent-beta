from api.generate import Client


prompt = """
create react components
"""

client = Client()
response = client.generate(prompt)
