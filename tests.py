from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file

'''
# commented out for get file contents testing
print(get_files_info("calculator", "."))
print(get_files_info("calculator", "pkg"))
print(get_files_info("calculator", "/bin"))
print(get_files_info("calculator", "../"))
'''

# commented out for additional content tests below
#print(len(get_file_content("calculator", "lorem.txt")) <= 10000)
#print(f'# of Chars: {len(get_file_content("calculator", "lorem.txt"))}')

# commented out for file write testing
# print(get_file_content("calculator", "main.py"))
# print(get_file_content("calculator", "pkg/calculator.py"))
# print(get_file_content("calculator", "/bin/cat"))

# commented out for run python testing
# print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
# print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
# print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

# run python tests
print(run_python_file("calculator", "main.py"))
print(run_python_file("calculator", "tests.py"))
print(run_python_file("calculator", "../main.py")) # should error
print(run_python_file("calculator", "nonexistent.py")) # should error
