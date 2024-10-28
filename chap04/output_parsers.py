from dotenv import dotenv_values
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


class Recipe(BaseModel):
    ingredients: list[str] = Field(description="ingredients of the dish")
    steps: list[str] = Field(description="steps to make the dish")


if __name__ == '__main__':
    config = dotenv_values("../.env")

    parser = PydanticOutputParser(pydantic_object=Recipe)

    # 프롬프트에 포함할 출력 형식 설명문
    format_instructions = parser.get_format_instructions()

    # PromptTemplate 생성
    template = """
    다음 요리의 레시피를 생각해주세요.
    
    {format_instructions}

    요리: {dish}
    """

    prompt = PromptTemplate(
        api_key=config["OPENAI_API_KEY"],
        template=template,
        input_variables=["dish"],
        partial_variables={"format_instructions": format_instructions}
    )

    formatted_prompt = prompt.format(dish="카레")

    # print(formatted_prompt)

    chat = ChatOpenAI(api_key=config["OPENAI_API_KEY"], model_name="gpt-3.5-turbo", temperature=0)
    messages = [HumanMessage(content=formatted_prompt)]
    output = chat.invoke(messages)

    print(output.content)

    # 응답값을 Pydantic class 변환
    recipe = parser.parse(output.content)
    print(recipe)
