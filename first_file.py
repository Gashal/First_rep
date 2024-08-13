print('Hello, I am new file!')

print('Create ssh keys and commit to GitHub')

import string

inp_text = "The sunset sets at twelve o' clock."
letter_upper = string.ascii_uppercase
d1 = dict(zip(letter_upper, range(1, len(letter_upper)+1)))
letter_lower = string.ascii_lowercase
d2 = dict(zip(letter_lower, range(1, len(letter_lower)+1)))
def repl(inp: str) -> str:
    new_str = ''
    for c in inp:
        if c in d1:
            new_str += str(d1[c]) + ' '
        elif c in d2:
            new_str += str(d2[c]) + ' '
    return new_str.strip()

print(repl(inp_text))
print(d1)
print(d2)
print(len('14 17 18 7 21 19 22 9 16 1 3 10 17 23 15 2 16 17 17 3 25 11 1 7 24 9 7 5 4 9 7 5 4 21 25 8 22 25 17 6 4 11 2 21 22 6 11 2 25 10 14 13 4 25 11 7 24 6 18 19 24 15 3 17 15 10 14 17 22 6 10 1 15 12 23 4 16 21 11 12 25 14 2 19 11 19 22 13 14 15 20 18 25 2 1'))
print(len('14 17 18 7 21 19 22 9 16 1 3 10 17 23 15 2 16 17 26 17 3 25 11 1 7 24 9 7 26 5 4 9 7 5 4 21 25 8 22 25 17 6 4 11 2 21 22 6 11 2 25 10 14 13 4 25 11 7 24 6 18 19 24 15 3 17 15 10 14 17 22 6 10 1 15 12 26 23 4 16 21 11 12 25 14 2 19 11 19 22 13 26 14 15 20 18 26 25 2 1'))
