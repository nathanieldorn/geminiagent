import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):

    try:
        working_path = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_path, file_path))
        if not abs_file_path.startswith(working_path):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_file_path):
            return f'Error: File "{file_path}" not found.'

        if file_path[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file'


        command = ["uv", "run", file_path]
        if args:
            command.append(args)
        result = subprocess.run(command, cwd=working_path, text=True, capture_output=True, check=True, timeout=30)

        if len(result.stdout) > 0:
            output = "STDOUT: " + result.stdout
            return output
        if len(result.stderr) > 0:
            error = "STDERR: " + result.stderr
            return error
        if result.check_returncode != 0:
            return f"Process exited with code {result.check_returncode}"
        if len(result.stdout) == 0 and len(result.stderr) == 0:
            return "No output produced."

    except Exception as e:
        return f"Error: executing Python file: {e}"


def run_python_file_schema():
    # build function schema/declaration
    schema_run_python_file = types.FunctionDeclaration(
        name="run_python_file",
        description="Run the specified file, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The path of the file to be run.",
                ),
                "args": types.Schema(
                    type=types.Type.STRING,
                    description="Arguments passed to the python file."
                )
            },
        ),
    )
    return schema_run_python_file
