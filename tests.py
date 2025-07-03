from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

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

print(get_file_content("calculator", "main.py"))
print(get_file_content("calculator", "pkg/calculator.py"))
print(get_file_content("calculator", "/bin/cat"))
