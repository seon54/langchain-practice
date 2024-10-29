from dotenv import dotenv_values
from langchain_community.document_loaders import GitLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter


def file_filter(file_path):
    return file_path.endswith(".mdx")


if __name__ == '__main__':
    config = dotenv_values("../.env")
    api_key = config["OPENAI_API_KEY"]

    # document loader
    loader = GitLoader(
        clone_url="https://github.com/langchain-ai/langchain",
        repo_path=". /langchain",
        branch="master",
        file_filter=file_filter,
    )

    raw_docs = loader.load()
    print(len(raw_docs))

    # document transformer
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(raw_docs)

    print(len(docs))

    embeddings = OpenAIEmbeddings(api_key=api_key)

    query = "AWS S3에서 데이터를 불러올 수 있는 DocumentLoader가 있나요?"

    db = Chroma.from_documents(docs, embeddings)

    retriever = db.as_retriever()

    context_docs = retriever.get_relevant_documents(query)
    print(f'len = {len(context_docs)}')

    first_doc = context_docs[0]
    print(f'metadata = {first_doc.metadata}')
    print(first_doc.page_content)
