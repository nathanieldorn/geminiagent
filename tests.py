import unittest
from functions.get_files_info import get_files_info
'''
class TestGetFiles(unittest.TestCase):

    def calc_root(self):
        print(get_files_info("calculator", "."))

    def calc_pkg(self):
        print(get_files_info("calculator", "pkg"))

    def calc_bin(self):
        print(get_files_info("calculator", "/bin"))

    def calc_parent(self):
        print(get_files_info("calculator", "../"))


if __name__ == "__main__":
    unittest.main()'''

print(get_files_info("calculator", "."))
print(get_files_info("calculator", "pkg"))
print(get_files_info("calculator", "/bin"))
print(get_files_info("calculator", "../"))
