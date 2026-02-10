"""
https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-python/
"""

def swapPositions(list, pos1, pos2):
    list[pos1-1], list[pos2-1] = list[pos2-1], list[pos1-1]
    return list

def swapPositions2(list, pos1, pos2):
    first_elem = list.pop(pos1-1)
    second_elem = list.pop(pos2-2)
    list.insert(pos1, second_elem)
    list.insert(pos2, first_elem)
    return list


open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


def check_balanced_parenthesis(p_str):
    stack = []
    for i in p_str:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


def check_balanced_parenthesis2(p_str):
    open_tup = tuple('({[')
    close_tup = tuple(')}]')
    map = dict(zip(open_tup, close_tup))
    queue = []
    for i in p_str:
        if i in open_tup:
            queue.append(map[i])
        elif i in close_tup:
            if not queue or i != queue.pop():
                return "Unbalanced"
    if not queue:
        return "Balanced"
    else:
        return "Unbalanced"

def check_balanced_parenthesis3(p_str):
    while len(p_str) > 0:
        if p_str[-1] == close_list[open_list.index(p_str[0])]:
    # for i in p_str:
    #     if p_str[-1] == close_list[open_list.index(i)]:
        # if i != p_str[-1]:
        #     if p_str[-1] == close_list[open_list.index(i)]
            p_str = p_str[1:-1]
        else:
            return "Unbalanced"

    if len(p_str) == 0:
        return "Balanced"
    else:
        return "Unbalanced"
if __name__ == '__main__':

    # Position Swap
    input_list = [23, 65, 19, 90]
    # input_list = [1, 2, 3, 4, 5]
    pos1 = 1
    pos2 = 3
    result = swapPositions2(input_list, pos1, pos2)

    # Balanced Parenthesis
    input = "{[]{()}}"
    # input = "[{}{})(]"
    # input = "((()"
    result = check_balanced_parenthesis3(input)
    print(result)
