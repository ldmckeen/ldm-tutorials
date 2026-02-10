"""
Q:

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
'''
 You receive a stream of event (potentially infinite). The events are just number in the range 0 -> 100.
 If a particular number appears more than <threshold> times in the last <period> events, please call the
 raise alarm function.  If there are multiple events in the window that exceed the threshold, only show the
 one that occurred the most times.

 Note: The period does not need to be a moving window.

'''


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

"""

from random import randint

threshold = 5
period = 100
events = {}
batch = 0


def raise_alarm(e):
    print(f"The number {e} has appeared more than {threshold} times in the last {period} events.")


def process_event(e: int):
    global batch
    global events
    batch += 1
    if str(e) in events:
        events[str(e)] += 1
    else:
        events[str(e)] = 1
    
    if batch == period:
        print(events)
        max_value = threshold
        max_event = None
        for i, v in events.items():
            if v > max_value:
                max_value = v
                max_event = i
        
        raise_alarm(max_event)
        batch = 0
        events = {}


def generate_event():
    return randint(0, 10)


if __name__ == '__main__':
    for x in range(0, 1000):
        e = generate_event()
        process_event(e)