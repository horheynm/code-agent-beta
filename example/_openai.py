from api.generate import Client
import subprocess
from api.transform import apply

import logging

logger = logging.getLogger(__name__)
react_project_name = "project1"

project_name = f"Project name: {react_project_name}"
task = "Create tik tac toe game using material ui"
prompt = f"""
{project_name}
{task}

Create a new react-app from scratch
Download all relevant packages
If the task is large, breakdown the project into smaller components in an appropriate folder structure.

Only provide me a single bash file that contains:
* All relevant code must be in the bash script
* Each component must be written as its own file following the above folder structure
* All components must be in the bash script
* Do not start the application at the end

Remove all texts that are not inside the bash script in the response. 
Only provide me a single bash file with code only
"""

client = Client()
response = client.generate(prompt)

code = apply(response["content"])


# save the response to a bash script
script = "script.sh"
with open(script, "w") as file:
    file.write(code)

# use docker instance to run the server
subprocess.run(["docker", "build", "-t", f"{react_project_name}-app", "."])
subprocess.run(["docker", "run", "-p", "3000:3000", f"{react_project_name}-app"])
