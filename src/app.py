import glob
from tree_hugger.core import PythonParser
import os

repo_src_path = "/github/workspace/" + os.environ.get("SOURCE_PATH")

python_parser = PythonParser("./languages.so")


python_files = glob.glob(repo_src_path + "**/*.py", recursive=True)

docstr_arr = []

for file in python_files:
    if (python_parser.parse_file(file)):
        docstr_arr.append(python_parser.get_all_function_docstrings())
        docstr_arr.append(python_parser.get_all_method_documentations())

print("::set-output name=documented-files::" + str(docstr_arr))