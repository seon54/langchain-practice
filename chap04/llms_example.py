from dotenv import dotenv_values
from langchain_openai import OpenAI


if __name__ == '__main__':
    config = dotenv_values("../.env")
    llm = OpenAI(api_key=config["OPENAI_API_KEY"], model_name="gpt-3.5-turbo-instruct", temperature=0)
    result = llm.invoke("자기소개를 해주세요.")
    print(result)