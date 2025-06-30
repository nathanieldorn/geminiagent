import os


def get_files_info(working_directory, directory=None):

    if directory is None:
        return "No directory specified"

    # limit LLM to working directory
    try:
        working_path = os.path.abspath(working_directory)
        get_directory = os.path.abspath(os.path.join(working_path, directory))
        if not get_directory.startswith(working_path):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    except Exception as e:
        return f'Error: {e} for "{working_directory}" and "{directory}"'

    # check for valid directory
    try:
        if not os.path.isdir(get_directory):
            return f'Error: "{directory}" is not a directory'
    except Exception as e:
        return f'Error: {e} for "{working_directory}" and "{directory}"'

    # return directory contents
    try:
        directory_items = os.listdir(get_directory)
        contents = ""
        for item in directory_items:
            item_path = os.path.join(get_directory, item)
            contents += f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}\n"
        return contents
    except Exception as e:
        return f'Error: {e} for "{working_directory}" and "{directory}"'
