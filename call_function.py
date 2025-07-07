from google.genai import types
from functions.get_file_content import get_file_content, get_file_content_schema
from functions.get_files_info import get_files_info, get_file_info_schema
from functions.run_python_file import run_python_file, run_python_file_schema
from functions.write_file import write_file, write_file_schema


available_functions = types.Tool(
    function_declarations=[
        get_file_info_schema(),
        get_file_content_schema(),
        write_file_schema(),
        run_python_file_schema()
    ]
)

functions = {
    "get_file_content": get_file_content,
    "get_files_info": get_files_info,
    "write_file": write_file,
    "run_python_file": run_python_file
}


def call_function(function_call_part, verbose=False):

    function_name = function_call_part.name

    if verbose:
        print(f"Calling function: {function_name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_name}")

    # check function name against dictionary and return error if not found
    if function_name not in functions:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    # return result of functions found in dictionary
    function_result = functions[function_name](working_directory="./calculator", **function_call_part.args)
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
