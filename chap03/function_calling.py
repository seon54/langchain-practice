import json

from dotenv import dotenv_values
from openai import OpenAI


def get_current_weather(location, unit="celsius"):
    weather_info = {
        "location": location,
        "temperature": 25,
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }

    return json.dumps(weather_info)


if __name__ == '__main__':
    config = dotenv_values(".env")
    client = OpenAI(api_key=config["OPENAI_API_KEY"])

    functions = [
        {
            "name": "get_current_weather",
            "description": "Get the current weather information of a location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. Seoul",
                    },
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
            },
            "required": ["location"],
        }
    ]

    messages = [
        {"role": "user", "content": "What's the weather like in Seoul?"}
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        functions=functions,
    )

    print(response.model_dump_json(indent=2))
    response_message = response.choices[0].message

    available_functions = {"get_current_weather": get_current_weather}

    function_name = response_message.function_call.name
    function_to_call = available_functions[function_name]
    function_args = json.loads(response_message.function_call.arguments)

    function_response = function_to_call(location=function_args["location"], unit=function_args.get("unit"))

    print(function_response)

    messages.append(response_message)
    messages.append(
        {"role": "function", "name": function_name, "content": function_response}
    )

    second_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    print(second_response.model_dump_json(indent=2))



