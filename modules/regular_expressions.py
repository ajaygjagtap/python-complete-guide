''' 
Regular Expressions :
Also known as regex.
Used to search, match and manipulate text patterns.


Pattern     Meaning                     Pattern     Meaning                                 Character Classes :
.           Any Character               {n, m}      Between n and m                             [a-z] -------> Lowercase letters
^           Start of string             \d          Digit                                       [A-Z] -------> Uppercase letters
$           End of string               \D          Non-digit                                   [0-9] -------> Digits
*           0 or more                   \w          Letter, digit, underscore                   [^0-9] ------> Not digits
+           1 or more                   \W          Non-word
?           0 or 1                      \s          Whitespace
{n}         Exactly n                   \S          Non-whitespace


Quick Tip :
To avoid python string escaping problems, always use raw string.
(r" ") -------> Don't interpret backslashes pass them as-is. 
'''


import re

'''
re.search() :
Finds the first match anywhere in the string.
Use when you just need to know if pattern exists.
'''
re.search(r"\d+", "Order 123 received")

"-----------------------------------------------------------------------------"

'''
re.findall() :
Returns all matches as a list.
Most used for data extraction.
'''
re.findall(r"\d+", "item 12, 45, 78") # ['12', '45', '78']

"-----------------------------------------------------------------------------"

'''
re.match() :
Matches only at the start of the string.
Useful for validation.
'''
re.match(r"\d+", "123abc") # Match
re.match(r"\d+", "xyz789") # No match

"-----------------------------------------------------------------------------"

'''
re.sub() :
Replaces matched text.
Used for cleaning and formatting text.
'''
re.sub(r"\d+", "x", "Phone : 1234") # Phone : xxxx

"-----------------------------------------------------------------------------"

'''
re.split() :
Split string using a regex pattern.
Useful when delimeters are inconsistent.
'''
re.split(r"[,\s]+", "apple,banana orange grapes") # ['apple', 'banana', 'orange', 'grapes']

"-----------------------------------------------------------------------------"

'''
re.finditer() :
Returns an iterator of match objects.
Best when you need position of matches.
'''
for m in re.finditer(r"\d+", "Age 25, year 2024"):
    print(m.group(), m.start())

"-----------------------------------------------------------------------------"

'''
re.compile() :
Compiles a regex for reuse and better performance.
Used in performance-critical code.
'''
pattern = re.compile(r"\w+")
pattern.findall("Fast and efficient")

"-----------------------------------------------------------------------------"

'''
Some imp. Methods/ Attributes:
.group()  ---------> Returns the matched text.
.groups() ---------> Returns all captured groups as tuple.
.group(n) ---------> Returns a specific capturing group.
.groupdict() ------> Returns named groups as a dictionary.
.start()  ---------> Start index of the match.
.end()    ---------> End index of the match.
.span()   ---------> Returns (start, end) tuple.
'''
