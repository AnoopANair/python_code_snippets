
import re
# raw string in python is a string prefixed with r which tells python not to handle backslashes in any special way.
print(r"\t Tab")

# We would  use re.compile method to search for patterns . It would aloow to seperate out patterns into variables hence easeier for reuse

pattern = re.compile(r'abc')

Texttosearch = """
abcdefghijklmnoabc
"""

matches = pattern.finditer(Texttosearch)

print(Texttosearch[1:4])
for match in matches :
    print(match)