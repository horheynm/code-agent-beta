# Component generator

Simple component generator using simplified agents. Generate react/next.js code from input prompt! 

![Demo](./static/demo.gif)

## How to run
Create `.env` file and enter your `OPENAI_API_KEY`, where the value should start with `sk-...`. Also include your github access token to push your project. 

Create `src/api/constant.py` and populate your constants for agents.

### Verify your tokens
Run the below commands to verify your github and openai tokens. 
```bash
 src/bin/validation/[(github|openai).sh]
```


## Commands

To create projects from scratch:
```python3
python3 './example/create_bash_script.py'
```
^ Generates bash script executable from LLM

To generate components frome existing framework:
```python3
python3 './example/completion.py'
```
^ Generates a "plan" and "executes" the plan to generate code according to the plan

Note: constants are not included in this repo. For usage please contact george.scratch.dev@gmail.com

## How it works

### `create_bash_script.py'
`create_bash_script.py' asks LLM to generate a bash script executable to create, install and modify code. Generated bash script and all dependecies are carried out in a fresh docker container that only has node. 


### './example/completion.py'
Asks agents to plan, execute the plan (layout the files and the folder structure), and generate code each of the file to be created. 