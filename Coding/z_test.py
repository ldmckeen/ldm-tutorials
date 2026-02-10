"""
Q:

'''
 You receive a stream of events (potentially infinite). The events are just a number in the range 0 -> 10.
 If a particular number appears more than <threshold> times in the last <period> events, please call the
 raise_alarm function.  If there are multiple events in the window that exceed the threshold, only show the
 one that occurred the most times.

 Note: The period does not need to be a moving window. You may handle the events in batches of size <period>

'''
"""
from random import randint

threshold = 5
period = 100
batch = 0
events = {}


def raise_alarm(e):
    print(f"The number {e} has appeared more than {threshold} times in the last {period} events.")


def process_event(e: int):
    global batch
    global events
    
    if e in events:
        events[e] += 1
    else:
        events[e] = 1
    
    if batch == period:
        max_event_amount = threshold
        max_event = None
        print(events)
       
        for i, v in events.items():
            if v > max_event_amount:
                max_event_amount = v
                max_event = i
        print(f"Max Event: {max_event}, occurances: {max_event_amount}")
        raise_alarm(e)
        batch = 0
        events = {}
        
    batch += 1
    pass


def generate_event():
    return randint(0, 10)


if __name__ == '__main__':
    for x in range(0, 1000):
        e = generate_event()
        process_event(e)
        
