from dotenv import dotenv_values
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

if __name__ == '__main__':
    config = dotenv_values("../.env")


    chat_prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template("당신은 {country} 요리 전문가입니다."),
        HumanMessagePromptTemplate.from_template("다음 요리의 레시피를 생각해주세요.\n\n요리: {dish}"),
    ])

    messages = chat_prompt.format_prompt(country="영국", dish="고기감자조림").to_messages()

    print(messages)
