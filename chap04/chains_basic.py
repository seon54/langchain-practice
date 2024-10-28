from dotenv import dotenv_values
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from chap04.output_parsers import Recipe

if __name__ == '__main__':
    config = dotenv_values("../.env")

    parser = PydanticOutputParser(pydantic_object=Recipe)

    # 프롬프트에 포함할 출력 형식 설명문
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
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )

    chat = ChatOpenAI(api_key=config["OPENAI_API_KEY"], model_name="gpt-3.5-turbo", temperature=0)

    # 이후에 deprecated
    # chain = LLMChain(prompt=prompt, llm=chat, output_parser=parser)
    chain = prompt | chat | parser

    recipe = chain.invoke("카레")

    print(recipe)
