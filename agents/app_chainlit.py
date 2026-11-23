import chainlit as cl
from dotenv import load_dotenv
from langchain_classic.agents import AgentExecutor , create_tool_calling_agent
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import ChatPromptTemplate ,MessagesPlaceholder
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage,AIMessage
from AI_memory import create_conversation , get_chat_history,save_message

from langchain_groq import ChatGroq

from AI_memory import create_conversation
# import nest_asyncio

load_dotenv()
# nest_asyncio.apply()
@cl.author_rename
def rename(orig_author: str):
    rename_dict = {"Chatbot": "Diyorbek AI","Assistant":"Diyorbek AI"}
    return rename_dict.get(orig_author,orig_author)

@cl.on_chat_start
async def start():
    user_id = "Diyorbek"

    conversation_id = create_conversation(
        user_id,
        "Yangi suhbat"
    )
    cl.user_session.set('user_id',user_id)
    cl.user_session.set('conversation_id',conversation_id)

    print("Yangi suhbat yaratildi:",conversation_id)

    await cl.Message(
        content="Salom! Meni Diyorbek tominidan yaratilgan AI Assistant"
    ).send()
    llm = ChatGroq(model_name="openai/gpt-oss-120b", temperature=0)
    search_tools = DuckDuckGoSearchRun()

    @tool
    def multiply(a: int, b: int) -> int:
        """Ikkita sonni bir-biriga ko`paytirish funksiya."""
        return a * b
    tools = [search_tools, multiply]

    prompt = ChatPromptTemplate.from_messages([
        ("system",
            "Sening isming Diyorbek. Sen aqlli va xushmuomala AI agentsan. ReAct"
            " sifatida fikr yurit va kerak bo'lsa foydali vositalardan"
            " foydalan."
        ),
        MessagesPlaceholder("chat_history"),
        ("human","{input}"),
        MessagesPlaceholder("agent_scratchpad")
    ])
    agent_runnable = create_tool_calling_agent(
        llm=llm, tools=tools,prompt=prompt,
    )
    agent = AgentExecutor(agent=agent_runnable,
                          tools=tools,
                          verbose=True)

    cl.user_session.set("agent",agent)
def run_agent_turn(agent ,user_id , conversation_id , user_input):
    chat_history = get_chat_history(
        user_id,
        conversation_id
    )

    response = agent.invoke({
        "input":user_input,
        "chat_history":chat_history,
    })
    ai_response = response['output']

    save_message(
        user_id,
        conversation_id,
        HumanMessage(content=user_input)
    )

    save_message(
        user_id,
        conversation_id,
        AIMessage(content=ai_response)
    )

    return ai_response

@cl.on_message
async def main(message: cl.Message):
    agent  = cl.user_session.get("agent")
    user_id = cl.user_session.get("id")
    conversation_id = cl.user_session.get("conversation_id")


    response_text = await cl.make_async(run_agent_turn)(
        agent,
        user_id,
        conversation_id,
        message.content
    )
    await cl.Message(content=response_text).send()
