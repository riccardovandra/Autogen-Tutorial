from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Load LLM inference endpoints from an env variable or a file
# See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
# and OAI_CONFIG_LIST_sample

#Import openai api key
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

#Create assistant agent
assistant = AssistantAgent(name="assistant", llm_config={"config_list": config_list})

#Create user proxy agent. Code Exection config means that all the code will be saved under coding
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})

user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD")
# This initiates an automated chat between the two agents to solve the task

