from dotenv import dotenv_values
from langchain.chains.conversation.base import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI

if __name__ == '__main__':
    config = dotenv_values("../.env")
    api_key = config["OPENAI_API_KEY"]

    chat = ChatOpenAI(api_key=api_key, model_name="gpt-4", temperature=0)

    # deprecated
    conversation = ConversationChain(llm=chat, memory=ConversationBufferMemory())

    while True:
        user_message = input("You: ")

        if user_message == '끝':
            print("(대화 종료)")
            break

        ai_message = conversation.invoke(input=user_message)["response"]
        print(f"AI: {ai_message}")


