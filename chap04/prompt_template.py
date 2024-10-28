from dotenv import dotenv_values
from langchain_core.prompts import PromptTemplate

if __name__ == '__main__':
    config = dotenv_values("../.env")

    template = """
    다음 요리의 레시피를 생각해주세요.
    
    요리: {dish}
    """

    prompt = PromptTemplate(
        api_key=config["OPENAI_API_KEY"],
        input_variables=["dish"],
        template=template,
    )

    result = prompt.format(dish="알리오 올리오")
    print(result)