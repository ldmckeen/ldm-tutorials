"""
Q: You are given a string containing various types of brackets interspersed with text, for instance
"{(cat[dog])<mouse>}". The brackets need to be correctly nested. How would you detect
if they are correctly nested or not.

A:
string_success = "<{cat[mat](dog)}>"
string_fail = "<{cat(mat](dog]}>"


brackets = {"{": "}",
            "<": ">",
            "[": "]",
            "(": ")" }

def matches(s):
    stack = list()
    for c in s:
        if c in brackets:
            # Push it.
            stack.append(c)
        if c in brackets.values():
            # Pop it
            top = stack.pop()
            # Ensure it matches
            expected_closing = brackets[top]
            if expected_closing != c:
                return False
    return True

print(matches(string_success))
print(matches(string_fail))

"""
brackets = {"{": "}",
            "<": ">",
            "[": "]",
            "(": ")" }

def matches(s):
    stack = list()
    for c in s:
        if c in brackets:
            # Push it.
            stack.append(c)
        if c in brackets.values():
            # Pop it
            top = stack.pop()
            # Ensure it matches
            expected_closing = brackets[top]
            if expected_closing != c:
                return False
    return True


if __name__ == '__main__':
    print(matches(string_success))
    print(matches(string_fail))
    
