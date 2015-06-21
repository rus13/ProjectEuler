import string

__author__ = 'Ruslan'

import Library.string as string

text = "aaaaaaaaaaaa"
pattern = "aa"
test = "ababaca"
m = len(pattern)
matches = string.matcher(text, pattern)

print(matches)
for i in matches:
    print(text[i:i+m])