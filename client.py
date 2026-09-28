import os
import json
import asyncio
from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_mcp_adapters.client import MultiServerMCPClient

from langchain_core.messages import AIMessage, HumanMessage, ToolMessage

load_dotenv()

groq_api_key = os.getenv('groq_api_key')
groq_model = os.getenv('groq_model')

async def main(groq_api_key, groq_model):
    llm = ChatGroq(model = groq_model, api_key = groq_api_key)

    server = {
        "expense_tracker":{
            "transport": "stdio",
            "command": "uv",
            "args": [
                "run",
                "--directory",
                r"C:\Users\USER\OneDrive\Work\expense_tracker_mcp",
                "python",
                "server.py"
            ]

        }
    }


    client = MultiServerMCPClient(server)

    tools = await client.get_tools()

    named_tools = {}

    for tool in tools:
        named_tools[tool.name] = tool

    #print("Available tools:", named_tools.keys())

    llm_with_tools = llm.bind_tools(tools)

    #question = "add ₹2500 on groceries from the supermarket today"

    #question = "give all expenses on food from august till yesterday"

    question = "give total expenses on food from august till yesterday"

    #question = "2500 + 2500"

    llm_response = await llm_with_tools.ainvoke(question)

    #print(llm_response.tool_calls)

    # if tool involved
    """content='' additional_kwargs={'reasoning_content': 'The user wants to add an expense: amount ₹2500, category groceries, note maybe "from the supermarket", date today.
      Use add_expense function. Provide fields: amount, category, date, note. date: today 2026-09-27. Use amount numeric? Probably number. Provide note.',
    'tool_calls': [{'id': 'fc_6ea983a3-b51f-4a06-8bc4-41af74459f9e', 'function': {'arguments': '{"amount":2500,"category":"groceries","date":"2026-09-27","note":"from the supermarket"}', 'name': 'add_expense'},
      'type': 'function'}]} response_metadata={'token_usage': {'completion_tokens': 123, 'prompt_tokens': 247, 'total_tokens': 370, 'completion_time': 0.258940036, 'completion_tokens_details':
    {'reasoning_tokens': 65}, 'prompt_time': 0.067034045, 'prompt_tokens_details': None, 'queue_time': 0.454758798, 'total_time': 0.325974081}, 'model_name': 'openai/gpt-oss-120b', 'system_fingerprint': 'fp_9241e9962b', 'service_tier': 'on_demand', 'finish_reason': 'tool_calls', 
    'logprobs': None, 'model_provider': 'groq'} id='lc_run--01a0e209-b9ff-7433-ac3f-8134129e1eba-0' tool_calls=[{'name': 'add_expense', 'args': {'amount': 2500, 'category': 'groceries', 'date': '2026-09-27', 
    'note': 'from the supermarket'}, 'id': 'fc_6ea983a3-b51f-4a06-8bc4-41af74459f9e', 'type': 'tool_call'}] invalid_tool_calls=[] usage_metadata={'input_tokens': 247, 'output_tokens': 123, 'total_tokens': 370, 'output_token_details': {'reasoning': 65}}
    """

    # no tool involved
    """content='4.' additional_kwargs={'reasoning_content': 'User asks "add 2 + 2". They want a simple arithmetic answer: 4. No tool needed.'} response_metadata={'token_usage':
    {'completion_tokens': 36, 'prompt_tokens': 243, 'total_tokens': 279, 'completion_time': 0.077619191, 'completion_tokens_details': {'reasoning_tokens': 25},
    'prompt_time': 0.08833644, 'prompt_tokens_details': None, 'queue_time': 0.425131447,
      'total_time': 0.165955631}, 'model_name': 'openai/gpt-oss-120b', 'system_fingerprint': 'fp_c652c0ffaa', 'service_tier': 'on_demand', 'finish_reason': 'stop',
    'logprobs': None, 'model_provider': 'groq'} id='lc_run--01a0e20c-af0b-70e0-bf4b-8c32ee72e8d3-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 243,
    'output_tokens': 36, 'total_tokens': 279, 'output_token_details': {'reasoning': 25}}"""

    """
    [{'name': 'add_expense', 'args': {'amount': 2500, 'category': 'groceries', 
    'date': '2026-09-27', 'note': 'from the supermarket'},
    'id': 'fc_57984e26-b84f-4899-856c-31d72a3b4d33', 'type': 'tool_call'}]
    """

    if not llm_response.tool_calls:
        return AIMessage(content=llm_response.content)

    tool_response = []

    for tool_call in llm_response.tool_calls:
        selected_tool = tool_call['name']
        selected_tool_args = tool_call['args']
        selected_tool_call_id = tool_call['id']

        result = await named_tools[selected_tool].ainvoke(selected_tool_args)

        #print(result)

        """
        [{'type': 'text', 'text': '["Expense Inserted Successfully"]',
        'id': 'lc_c3a272d8-445c-4787-af10-ecc3637b3652'}]
        """

        tool_msg = ToolMessage(content=json.dumps(result), tool_call_id = selected_tool_call_id)

        tool_response.append(tool_msg)


    llm_response = await llm_with_tools.ainvoke([question, llm_response, *tool_response])

    return llm_response




if __name__ == '__main__':
    print(asyncio.run(main(groq_api_key, groq_model)))


