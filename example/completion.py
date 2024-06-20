# Use for code completion

from api.chat_agent import ChatAgent

model = "gpt-3.5-turbo"
prompt = "next.js tic tac toe app using typescript"
file_path = "./created/plan.md"

agent = ChatAgent(model)


agent.create_plan(prompt=prompt, path=file_path)

files = agent.execute_plan(prompt=prompt, path=file_path)

with open(file_path, "r", encoding="utf-8") as file:
    plan = file.read()
agent.code_gen(
    path="./created",
    prompt=prompt,
    plan=plan,
    files=files,
)
