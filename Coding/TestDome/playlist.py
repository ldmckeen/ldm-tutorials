"""
A playlist is considered a repeating playlist if any of the songs
contain a reference to a previous song in the playlist.
Otherwise, the playlist will end with the last song which points to None

Implement a function is_in_repeating_playlist that, efficiently, with respect to time used, returns true if
a playlist is repeating or false if it is not.

For example, the following code prints "True" as both songs point to each other.
    first = Song("Hello")
    second = Song("Eye of the tiger")
    
    first.next_song(second)
    second.next_song(first)
    
    print(fourth.is_in_repeating_playlist())

"""

class Song:
    def __init__(self, name):
        self.name = name
        self.next = None
    
    def next_song(self, song):
        self.next = song
    
    def is_in_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        s_list = set()
        current = self
        while current is not None:
            if current.name in s_list:
                return True
            s_list.add(current.name)
            current = current.next
            
        return False


if __name__ == '__main__':
    first = Song("Hello")
    second = Song("Eye of the tiger")
    third = Song("Blue Eyes")
    fourth = Song("Check")
    
    first.next_song(second)
    second.next_song(third)
    # third.next_song(fourth)
    fourth.next_song(first)
    
    print(fourth.is_in_repeating_playlist())



"""
Key Note, use set instead of List for Time Complexity Optimisation
Use a list when the order of the playlist matters (like playing songs in sequence).
Use a set when you need to quickly check if a song exists in a collection.
"""
