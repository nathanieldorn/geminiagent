import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():

    load_dotenv()
    args = sys.argv[1:]

    if not args:
        print("Invalid prompt provided")
        exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    prompt = " ".join(args)
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]
    if "verbose" in prompt:
        prompt_response = response(client, messages)
        print("Response:")
        print(prompt_response.text)
        print(f"User prompt: {prompt}")
        print("Prompt tokens:", prompt_response.usage_metadata.prompt_token_count)
        print("Response tokens:", prompt_response.usage_metadata.candidates_token_count)
    else:
        print(response(client, messages))

def response(client, messages):
    return client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )




if __name__ == "__main__":
    main()
