import os
from google import genai
from google.genai import types


def get_files_info(working_directory, directory=None):

    if directory is None:
        return "No directory specified"

    try:
        # limit LLM to working directory
        working_path = os.path.abspath(working_directory)
        get_directory = os.path.abspath(os.path.join(working_path, directory))
        if not get_directory.startswith(working_path):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # check for valid directory
        if not os.path.isdir(get_directory):
            return f'Error: "{directory}" is not a directory'

        # return directory contents
        directory_items = os.listdir(get_directory)
        contents = ""
        for item in directory_items:
            item_path = os.path.join(get_directory, item)
            contents += f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}\n"
        return contents

    except Exception as e:
        return f'Error: {e} for "{working_directory}" and "{directory}"'


def get_file_info_schema():
    # build function schema/declaration
    schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )
    return schema_get_files_info
