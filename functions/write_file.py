import os
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from google.genai import types


def write_file(working_directory, file_path, content):

    try:
        # check if in working directory
        working_path = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_path, file_path))
        if not abs_file_path.startswith(working_path):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # create path if not found
        if not os.path.exists(os.path.dirname(abs_file_path)):
            directory = os.path.dirname(file_path)
            os.makedirs(os.path.join(working_directory, directory))

        # write file if not found
        with open(abs_file_path, "w") as f:
            f.write(content)

        # verify written file/conents
        with open(abs_file_path, "r") as r:
            file_contents = r.read()
            if file_contents == content:
                return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
            else:
                return f'Contents of "{file_path}" do not match the content passed in'
    except Exception as e:
        return f'Error: {e} for "{working_directory}", "{file_path}", and {content[:20]}...'


def write_file_schema():
    # build function schema/declaration
    schema_write_file = types.FunctionDeclaration(
        name="write_file",
        description="Write contents to the file, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The path of the file to be run.",
                ),
                "content": types.Schema(
                    type=types.Type.STRING,
                    description="The content to be written to a file, relative to the working directory. If not provided, state that the content must be provided.",
                ),
            },
        ),
    )
    return schema_write_file
