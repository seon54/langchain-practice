from dotenv import dotenv_values
from langchain_openai import OpenAIEmbeddings

if __name__ == '__main__':
    config = dotenv_values("../.env")
    api_key = config["OPENAI_API_KEY"]


    embeddings = OpenAIEmbeddings(api_key=api_key)

    query = "AWS S3에서 데이터를 불러올 수 있는 DocumentLoader가 있나요?"

    vector = embeddings.embed_query(query)

    print(len(vector))
    print(vector)
