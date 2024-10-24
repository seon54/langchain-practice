from dotenv import dotenv_values
from openai import OpenAI

if __name__ == '__main__':
    config = dotenv_values(".env")
    client = OpenAI(api_key=config["OPENAI_API_KEY"])

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello! I'm SH."}
        ]
    )

    print(response.model_dump_json(indent=2))
