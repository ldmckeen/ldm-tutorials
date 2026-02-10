
def mergeArrays(a, b):
    len_a = len(a)
    len_b = len(b)
    c = [None] * (len_a + len_b)
    a_i = 0
    b_i = 0
    c_i = 0

    while a_i < len_a and b_i < len_b:
        if a[a_i] < b[b_i]:
            c[c_i] = a[a_i]
            a_i += 1
            c_i += 1
        else:
            c[c_i] = b[b_i]
            b_i += 1
            c_i += 1

    print(f"Array after initial while: {c}")

    while a_i < len_a:
        c[c_i] = a[a_i]
        a_i += 1
        c_i += 1

    while b_i < len_b:
        c[c_i] = b[b_i]
        b_i += 1
        c_i += 1

    print(f"Array after remaining integers added: {c}")

    return c

if __name__ == '__main__':

    a = [1, 2, 3]
    b = [2, 5, 5]
    result = mergeArrays(a, b)
    print(result)
