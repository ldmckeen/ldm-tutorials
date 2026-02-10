import sys


def findMedian(arr):
    # Write your code here
    # arr_len = len(arr) - 1
    # sort_arr = sorted(arr)
    # index = int(arr_len/2)
    # return sort_arr[index]

    return sorted(arr)[int((len(arr) - 1) / 2)]


if __name__ == '__main__':
    input = ' '.join(sys.argv[1:])
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input.strip())

    arr = list(map(int, input.rstrip().split()))
    result = findMedian(arr)
    print(result)

    # fptr.write(str(result) + '\n')
    # fptr.close()
