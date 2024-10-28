from dotenv import dotenv_values
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

if __name__ == '__main__':
    config = dotenv_values("../.env")
    chat = ChatOpenAI(api_key=config["OPENAI_API_KEY"], model_name="gpt-3.5-turbo", temperature=0)

    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content="안녕하세요 저는 sh라고 합니다!"),
        AIMessage(content="안녕하세요, sh씨! 어떻게 도와드릴까요?"),
        HumanMessage(content="제 이름을 아세요?")
    ]

    result = chat.invoke(messages)
    print(result.content)
