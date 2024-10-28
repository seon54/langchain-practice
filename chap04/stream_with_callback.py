from dotenv import dotenv_values
from langchain_core.callbacks import StreamingStdOutCallbackHandler
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

if __name__ == '__main__':
    config = dotenv_values("../.env")
    chat = ChatOpenAI(
        api_key=config["OPENAI_API_KEY"],
        model_name="gpt-3.5-turbo",
        temperature=0,
        streaming=True,
        callbacks=[StreamingStdOutCallbackHandler()],
    )

    messages = [
        HumanMessage(content="자기소개를 해주세요")
    ]

    result = chat.invoke(messages)
