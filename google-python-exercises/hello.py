#!/usr/bin/env python

# import modules used here -- sys is a very standard one
import sys

# Gather our code in a main() function
def main():
    print('Hello there', sys.argv[1])
    # print(sys.argv)
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

# def main():
#     print(repeat('Yay', False))      ## YayYayYay
#     print(repeat('Woo Hoo', True))   ## Woo HooWoo HooWoo Hoo!!!

# Defines a "repeat" function that takes 2 arguments.
def repeat(s, exclaim):
    """
    Returns the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = s + s + s # can also use "s * 3" which is faster (Why?)
    if exclaim:
        result = result + '!!!'
    return result

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
