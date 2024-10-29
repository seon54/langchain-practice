from dotenv import dotenv_values
from langchain_community.document_loaders import GitLoader


def file_filter(file_path):
    return file_path.endswith(".mdx")


if __name__ == '__main__':
    config = dotenv_values("../.env")
    api_key = config["OPENAI_API_KEY"]

    loader = GitLoader(
        clone_url="https://github.com/langchain-ai/langchain",
        repo_path=". /langchain",
        branch="master",
        file_filter=file_filter,
    )

    raw_docs = loader.load()
    print(len(raw_docs))
