
def maxSubString(s):
    maxchar = 'a'
    subs = []

    for i in range(len(s)):
        if (s[i] >= maxchar):
            maxchar = s[i]
            subs.append(i)

    max_ss = ""

    for i in range(len(subs)):
        if (s[subs[i]: len(s)] > max_ss):
            max_ss = s[subs[i]: len(s)]
    return max_ss

if __name__ == '__main__':

    s = "baca"
    result = maxSubString(s)
    print(result)
