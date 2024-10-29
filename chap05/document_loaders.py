from dotenv import dotenv_values
from langchain_community.document_loaders import GitLoader
from langchain_text_splitters import CharacterTextSplitter


def file_filter(file_path):
    return file_path.endswith(".py")


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
