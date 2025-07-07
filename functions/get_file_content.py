import os
from google.genai import types


def get_file_content(working_directory, file_path):

    try:
        # check if in working directory
        working_path = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_path, file_path))
        if not abs_file_path.startswith(working_path):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # check if the path is a file
        if not os.path.isfile(abs_file_path):
            return f'Error: File not foun dor is not a regular file: "{file_path}"'

        # read file and return contents as a string
        with open(abs_file_path) as open_file:
            file_contents = ""
            file_contents = open_file.read()

            # trunc string to 10k
            if len(file_contents) > 10000:
                file_contents = file_contents[:10000]
            return file_contents

    except Exception as e:
        return f'Error: {e} for "{working_directory}" and "{file_path}"'


def get_file_content_schema():
    # build function schema/declaration
    schema_get_content = types.FunctionDeclaration(
        name="get_file_content",
        description="Get contents of the file, limited to 10,000 characters and constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The path of the file to be read.",
                ),
            },
        ),
    )
    return schema_get_content
