"""
Q:
from random import randint
'''
 You receive a stream of events (potentially infinite). The events are just a number in the range 0 -> 10.
 If a particular number appears more than <threshold> times in the last <period> events, please call the
 raise_alarm function.  If there are multiple events in the window that exceed the threshold, only show the
 one that occurred the most times.

 Note: The period does not need to be a moving window. You may handle the events in batches of size <period>

'''

threshold = 5
period = 100

def raise_alarm(e):
    print(f"The number {e} has appeared more than {threshold} times in the last {period} events.")


def process_event(e: int):
    pass

def generate_event():
    return randint(0, 10)


if __name__ == '__main__':
    for x in range(0, 1000):
        e = generate_event()
        process_event(e)


A:
from random import randint

threshold = 5
period = 100


freq = {}
window = 0

def raise_alarm(e):
    print(f"The number {e} has appeared more than {threshold} times in the last {period} events.")


def process_event(e):
    global freq
    global window
    freq[e] = freq.get(e, 0) + 1
    window +=1
    if window > period:
        highest_v = 0
        highest_k = None
        for k,v  in freq.items():
            if v > threshold:
                if v > highest_v:
                    highest_v = v
                    highest_k = k
        #print("highest_v ", highest_v, " highest_k:", highest_k)
        raise_alarm(highest_k)
        freq = {}
        window = 0

def generate_event():
    return randint(0, 10)


if __name__ == '__main__':
    while(True):
        e = generate_event()
        process_event(e)


"""

from random import randint

threshold = 3
period = 100
freq = {}

def raise_alarm(e):
    print(f"The number {e} has appeared more than {threshold} times in the last {period} events.")


def process_event(e: int):
    # print(e)
    if e in freq:
        freq[e] += 1
    else:
        freq[e] = 1

    if freq[e] >= threshold:
        raise_alarm(e)
    # print(freq)


def generate_event():
    return randint(0, 10)


if __name__ == '__main__':
    for x in range(0, 10):
        e = generate_event()
        process_event(e)
