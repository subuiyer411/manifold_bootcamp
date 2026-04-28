from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-nano",seed=6)

resp1 = llm.invoke("We are building an AI system for processing medical insurance claims.")
print(f"Response 1: {resp1.content}")

resp2 = llm.invoke("What are the main risks in this system?")
print(f"Response 2: {resp2.content}")

# Why the second question may fail or behave inconsistently without conversation history.
# Answer : Because the model is not aware of the previous conversation. The question is referring to a system which was mentioned in the previous question.

messages=[
    SystemMessage(content="You are a Senior AI Architect reviewing production systems."),
    HumanMessage(content="We are building an AI system for processing medical insurance claims."),
    HumanMessage(content="What are the main risks in this system?")
]

resp3 =  llm.invoke(messages)
print(f"Response 3: {resp3.content}")

"""
Reflection:

1. Why did string-based invocation fail?
A1: Because it not store any history of the conversation.
2. Why does message-based invocation work?
A2: Using HumanMessage, we are able to pass two consecutive messages to the model giving it the context of the conversation.
3. What would break in a production AI system if we ignore message history?
A3: It will not be able to understand the context of the conversation. Each message would be considered independently without any context.
"""