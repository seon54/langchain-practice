from dotenv import dotenv_values
from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SimpleSequentialChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

if __name__ == '__main__':
    config = dotenv_values("../.env")
    api_key = config["OPENAI_API_KEY"]

    chat = ChatOpenAI(api_key=api_key, model_name="gpt-3.5-turbo", temperature=0)

    cot_template = """다음 질문에 답하세요.
    
    질문: {question}
    
    단계별로 생각해 봅시다.
    """

    cot_prompt = PromptTemplate(
        api_key=api_key,
        input_variables=["question"],
        template=cot_template,
    )

    cot_chain = LLMChain(llm=chat, prompt=cot_prompt)

    summarize_template = """다음 문장을 결론만 간단히 요약하세요.
    
    {input}
    """

    summarize_prompt = PromptTemplate(api_key=api_key, input_variables=["input"], template=summarize_template)

    summarize_chain = LLMChain(llm=chat, prompt=summarize_prompt)

    cot_summarize_chain = SimpleSequentialChain(chains=[cot_chain, summarize_chain])

    result = cot_summarize_chain.invoke(
        "저는 시장에 가서 사과 10개를 샀습니다. 이웃에게 2개, 수리공에게 2개를 주었습니다. 그런 다음에 사과 5개를 더 사서 1개를 먹었습니다. 남은 개수는 몇 개인가요?")

    print(result["output"])
