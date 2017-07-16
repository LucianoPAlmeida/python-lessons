import os
import re

def rename_files(directory):
    files = os.listdir(directory)
    for filename in files:
        path = os.path.join(directory, filename)
        newPath = os.path.join(directory, re.sub(r"[0-9]", "", filename))
        os.rename(path, newPath)

rename_files("/Users/lucianoalmeida/Downloads/prank")