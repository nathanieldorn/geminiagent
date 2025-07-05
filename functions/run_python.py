import os
import subprocess

def run_python_file(working_directory, file_path):

    try:
        working_path = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_path, file_path))
        if not abs_file_path.startswith(working_path):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_file_path):
            return f'Error: File "{file_path}" not found.'

        if file_path[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file'

        result = subprocess.run(["python", file_path], cwd=working_path, text=True, capture_output=True, check=True, timeout=30)

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
