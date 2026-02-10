
def findCompletePrefixes(names, query):

    prefix_count_list = []

    for q in query:
        prefix_count = 0
        for n in names:
            if q in n and len(q) != len(n) and n.find(q) == 0:
                prefix_count += 1

        prefix_count_list.append(prefix_count)

    return prefix_count_list

if __name__ == '__main__':

    names = ['sssteve', 'stevens', 'danny', 'steves', 'dan', 'john', 'johnny', 'joe', 'alex', 'alexander']
    query = ['steve', 'alex', 'joe', 'john', 'dan']
    result = findCompletePrefixes(names, query)
    print(result)
