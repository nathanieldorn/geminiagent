import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_function import available_functions, call_function


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

    if "--verbose" in prompt:
        verbose = True
        prompt = prompt.replace("--verbose", "")
    else:
        verbose = False

    if verbose:
        print(f"User prompt: {prompt}")

    try:
        generate_content(client, messages, verbose)
    except Exception as e:
        print(f"Error: content generation - {e}")


def generate_content(client, messages, verbose):

    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
    iterations = 0
    while iterations < 20:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
        )

        # break out and print text if there are no more function calls
        if not response.function_calls:
            print(response.text)
            break

        for candidate in response.candidates:
            messages.append(candidate.content)

        # call each function and append results to the messages list, raising an exception if unsuccessful
        for call in response.function_calls:
            function_call_result = call_function(call, verbose)
            messages.append(function_call_result)
            if (not function_call_result.parts or not function_call_result.parts[0].function_response.response):
                raise Exception("Fatal exception.")
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")

        iterations += 1


if __name__ == "__main__":
    main()
